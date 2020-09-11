import pyperclip
import re

def print_results(results):
  print('Copied to clipboard:')
  for result in results:
    print(result)

phone_pattern = re.compile(r'''
  (\d{3}|\(\d{3}\))? # area code
  (\s|-|\.)? # separator
  (\d{3}) # first 3 digits
  (\s|-|\.)? # separator
  (\d{4}) # last 4 digits
  (\s*(ext\.?|x)\s*(\d{2, 5}))? # extension
''', re.VERBOSE)

email_pattern = re.compile(r'''(
  [A-Za-z0-9._%+-]+ # username
  @ # @ symbol
  [a-zA-Z0-9.-]+ # domain name
  (\.[a-zA-Z]{2,}) # tld
)''', re.VERBOSE)

data = pyperclip.paste()

phone_number_matches = phone_pattern.findall(data)
phone_numbers = list(map(lambda groups: ''.join(groups), phone_number_matches))

email_matches = email_pattern.findall(data)
email_addresses = list(map(lambda groups: groups[0], email_matches))

result = phone_numbers + email_addresses

pyperclip.copy('\n'.join(result))
print_results(result)
