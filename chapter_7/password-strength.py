#!

import re
import sys

try:
  _, password = sys.argv

  length_pattern = re.compile(r'^.{8,}$')
  uppercase_pattern = re.compile(r'[A-Z]')
  lowercase_pattern = re.compile(r'[a-z]')
  number_pattern = re.compile(r'[0-9]')

  is_valid = (
    length_pattern.search(password) and
    uppercase_pattern.search(password) and
    lowercase_pattern.search(password) and
    number_pattern.search(password)
  )

  print('Valid' if is_valid else 'Invalid')
except ValueError:
  print('Please supply a value to check as the first argument.')
