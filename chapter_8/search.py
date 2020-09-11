from pathlib import Path
import re
import sys

import pprint

args = sys.argv[1:]

search_dir = Path('./lyrics-to-search')

def get_matches_in_file(path, pattern):
  matches = []
  file = open(path, 'r')
  for line_number, line in enumerate(file):
    if re.search(pattern, line, re.IGNORECASE):
      matches.append((line_number + 1, line.strip()))
  file.close()
  return matches

def add_matches_to_results(results, path, matches):
  segs = str(path).split('/')[1:]
  nested_result = results
  for seg in segs:
    if re.search(r'\.txt$', seg):
      nested_result[seg] = matches
    else:
      nested_result.setdefault(seg, {})
      nested_result = nested_result[seg]

def print_results(results, level = 0):
  indent_str = '  '
  for key in results.keys():
    indent = indent_str * level
    print(f'{indent} {key}')

    if isinstance(results[key], list):
      indent = indent + indent_str
      for line_number, match in results[key]:
        print(f'{indent} Line {line_number}: {match}')
      print('')
    else:
      print_results(results[key], level + 1)

def search(pattern):
  results = {}
  paths = list(search_dir.rglob('*.txt'))

  for path in paths:
    matches = get_matches_in_file(path, pattern)
    
    if matches and len(matches) > 0:
      add_matches_to_results(results, path, matches)

  print_results(results)

if len(args) == 1:
  search(args[0])
else:
  print('Invalid options.')
