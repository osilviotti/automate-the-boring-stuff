#!

import re
import sys

try:
  _, number = sys.argv

  pattern = re.compile(r'^\d{1,3}((,\d{3})+)?$')

  print('Valid' if pattern.search(number) else 'Invalid')
except ValueError:
  print('Please supply a value to check as the first argument.')
