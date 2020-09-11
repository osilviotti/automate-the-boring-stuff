#!
# Stores passwords in passwords.txt and copies them to the clipboard when retrieved

import sys
import pyperclip
from pathlib import Path
from functools import reduce

def add_password_to_dictionary(dictionary, item):
  delimiter_index = item.index('=')
  key = item[:delimiter_index]
  value = item[delimiter_index + 1:]
  dictionary[key] = value

  return dictionary

def serialize_dictionary(dictionary):
  result = ''

  for k, v in dictionary.items():
    result += f'{k}={v}\n'

  return result


if len(sys.argv) < 2:
  print('Usage:')
  print('python password-locker.py [account] - retrieves a password')
  print('python password-locker.py [account] [password] - adds or updates a password')
  sys.exit()

filename = Path('passwords.txt')
filename.touch(exist_ok=True)
file = open(filename, 'r+')

PASSWORDS = reduce(add_password_to_dictionary, file.read().strip().split('\n'), {})

args = sys.argv[1:]
account = args[0]

if len(args) > 1:
  password = args[1]
  verb = 'updated in the' if account in PASSWORDS else 'added to the'

  PASSWORDS[account] = password

  file.seek(0)
  file.write(serialize_dictionary(PASSWORDS))
  file.truncate()

  print(f'Password for account "{account}" {verb} locker.')
else:
  try:
    pyperclip.copy(PASSWORDS[account])
    print(f'Password for account "{account}" copied to the clipboard.')
  except KeyError:
    print(f'No password for account "{account}".')

file.close()
