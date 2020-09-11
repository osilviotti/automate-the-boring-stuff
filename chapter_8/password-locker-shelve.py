#!
# Stores passwords in passwords.txt and copies them to the clipboard when retrieved

import sys
import pyperclip
import shelve

if len(sys.argv) < 2:
  print('Usage:')
  print('python password-locker.py [account] - retrieves a password')
  print('python password-locker.py [account] [password] - adds or updates a password')
  sys.exit()

PASSWORDS = shelve.open('passwords')

args = sys.argv[1:]
account = args[0]

if len(args) > 1:
  password = args[1]
  verb = 'updated in the' if account in PASSWORDS else 'added to the'

  PASSWORDS[account] = password

  print(f'Password for account "{account}" {verb} locker.')
else:
  try:
    pyperclip.copy(PASSWORDS[account])
    print(f'Password for account "{account}" copied to the clipboard.')
  except KeyError:
    print(f'No password for account "{account}".')

PASSWORDS.close()
