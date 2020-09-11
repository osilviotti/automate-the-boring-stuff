import re

test_string_1 = '''     
    abcde

'''
test_string_2 = 'testABCDEtest'

print(test_string_1)
print(test_string_2)

def strip(string, pattern = r'\s'):
  return re.sub(pattern, '', string)

stripped_string_1 = strip(test_string_1)
stripped_string_2 = strip(test_string_2, 'test')

print(stripped_string_1)
print(stripped_string_2)
