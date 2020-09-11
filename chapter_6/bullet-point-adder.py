#!
# Prefixes each new line in the clipboard with an asterisk and a space

import pyperclip

def add_bullet(line):
  return f'* {line}'

input = pyperclip.paste().strip().split('\n')
output = '\n'.join(map(add_bullet, input))

pyperclip.copy(output)
