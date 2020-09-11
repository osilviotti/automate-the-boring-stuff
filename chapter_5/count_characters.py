import pprint

string = 'The quick brown fox jumps over the lazy dog'
count = {}

for character in string:
  count.setdefault(character, 0)
  count[character] += 1

pprint.pprint(count)
