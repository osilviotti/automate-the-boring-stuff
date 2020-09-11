from datetime import datetime
import inquirer
from pathlib import Path
import re

template_path = Path('./madlibs_templates')
output_path = Path('./madlibs')

def path_to_filename_without_extension(path):
  return path.split('/')[-1].split('.')[0]

def path_to_label(path):
  filename_without_extension = path_to_filename_without_extension(path)
  return filename_without_extension.replace('-', ' ').title()

def get_message(type):
  return f'Enter {"an" if type[0] in "AEIOU" else "a"} {type.lower()}'

def save_file(template_path, filled_template):
  output_path.mkdir(parents=True, exist_ok=True)
  formatted_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
  template_name = path_to_filename_without_extension(template_path)
  path = Path(f'{output_path}/{template_name}-{formatted_date}.txt')
  path.touch(exist_ok=True)
  file = open(path, 'w')
  file.write(filled_template)
  file.close()

template_filename = inquirer.prompt([
  inquirer.List(
    'template',
    message='Choose your MadLib',
    choices=[
      (path_to_label(str(path)), str(path)) for path in template_path.glob('*.txt')
    ]
  )
])['template']

if template_filename:
  pattern = r'ADJECTIVE|NOUN|ADVERB|VERB'
  template_file = open(template_filename, 'r')
  template = template_file.read()
  template_file.close()

  matches = re.findall(pattern, template)
  questions = [
    inquirer.Text(f'{i}', message=get_message(match)) for i, match in enumerate(matches)
  ]
  answer_dictionary = inquirer.prompt(questions)
  answer_keys = [int(key) for key in answer_dictionary.keys()]
  answer_keys.sort()
  answers = [answer_dictionary[str(key)] for key in answer_keys]

  print('\n')
  filled_template = re.sub(pattern, lambda _: answers.pop(0), template)

  print(filled_template)

  save_file(template_filename, filled_template)
