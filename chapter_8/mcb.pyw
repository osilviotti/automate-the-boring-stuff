#! /usr/bin/env python3

import pyperclip
import shelve
import sys

args = sys.argv[1:]
clipboard = shelve.open('clipboard')

def print_help():
  print('''
    mcb.py list - lists saved keywords
    mcb.py [keyword] - copies the saved value for [keyword] to your clipboard
    mcb.py save [keyword] - saves the current value of your clipboard to [keyword]
  ''')

def save_current_clipboard(keyword):
  clipboard[keyword] = pyperclip.paste()

def copy_value_for_keyword_to_clipboard(keyword):
  pyperclip.copy(clipboard[keyword])

def copy_saved_keywords_to_clipboard():
  keys = '\n'.join(clipboard.keys())
  pyperclip.copy(keys)

def clear_clipboard():
  clipboard.clear()

def clear_keyword_from_clipboard(keyword):
  del clipboard[keyword]

if len(args) == 0:
  print_help()
elif len(args) == 1:
  if args[0].lower() == 'list':
    copy_saved_keywords_to_clipboard()
  elif args[0].lower() == 'delete':
    clear_clipboard()
  elif args[0] in clipboard:
    copy_value_for_keyword_to_clipboard(args[0])
  else:
    print(f'No value saved for keyword "{args[0]}"')
elif len(args) == 2:
  if args[0].lower() == 'save':
    save_current_clipboard(args[1])
  elif args[0].lower() == 'delete':
    clear_keyword_from_clipboard(args[1])
  else:
    print('Invalid argument(s) provided.')
else:
  print('Invalid argument(s) provided.')

clipboard.close()
