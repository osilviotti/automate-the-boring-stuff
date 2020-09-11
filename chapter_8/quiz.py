from datetime import datetime
from pathlib import Path
import random
import sys

ASCII_OFFSET = 65

CAPITALS = {
  'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
  'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
  'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
  'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
  'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
  'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
  'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
  'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
  'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
  'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
  'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
  'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
  'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
  'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
  'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
  'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
  'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}

def generate_quiz_data():
  states = list(CAPITALS.keys())
  random.shuffle(states)
  quiz_data = []

  for state_index in range(len(states)):
    state = states[state_index]
    capital = CAPITALS[state]
    answers = []

    while len(answers) < 3:
      false_key = states[random.randint(0, len(states) - 1)]

      if false_key != state and false_key not in answers:
        answers.append(false_key)

    true_key_index = random.randint(0, len(answers) - 1)
    answers.insert(true_key_index, capital)
    quiz_data.append({
      'state': state,
      'answers': answers,
      'correct_answer_index': true_key_index
    })

  return quiz_data

def generate_files(build_time, quiz_number, quiz_data):
  formatted_date = build_time.strftime('%Y-%m-%dT%H:%M:%S')
  dir_path = Path(f'./quizzes/{formatted_date}')
  dir_path.mkdir(parents=True, exist_ok=True)

  quiz_sheet = get_quiz_sheet(quiz_data)
  answer_sheet = get_answer_sheet(quiz_data)

  write_file(dir_path, f'quiz-{quiz_number}', quiz_sheet)
  write_file(dir_path, f'answers-{quiz_number}', answer_sheet)

def get_quiz_sheet(quiz_data):
  output = 'Name:\n\nDate:\n\nPeriod:\n\n'
  output += 'State Capitals Quiz (Form 1)'.center(60)
  output += '\n'

  for index in range(len(quiz_data)):
    data = quiz_data[index]
    state = data['state']
    answers = data['answers']

    output += '\n'
    output += f'{index + 1}. What is the capital of {state}?'

    for answer_index in range(len(answers)):
      answer_label = get_answer_label(answer_index)
      answer = answers[answer_index]
      output += '\n\t'
      output += f'{answer_label}. {answer}'
    output += '\n'
  
  return output

def get_answer_sheet(quiz_data):
  output = ''

  for index in range(len(quiz_data)):
    data = quiz_data[index]
    correct_answer_index = data['correct_answer_index']
    correct_answer = get_answer_label(correct_answer_index)
    output += f'{index + 1}. {correct_answer}\n'

  return output

def get_answer_label(answer_index):
  return chr(answer_index + ASCII_OFFSET)

def write_file(dir_path, filename, contents):
  filename = Path(f'{dir_path}/{filename}.txt')
  filename.touch(exist_ok=True)
  file = open(filename, 'w+')
  file.write(contents)
  file.close()

try:
  _, number = sys.argv
  build_time = datetime.now()
  
  for index in range(int(number)):
    quiz_number = index + 1
    quiz_data = generate_quiz_data()
    generate_files(build_time, quiz_number, quiz_data)

except ValueError:
  print('Please supply a number of quizzes to generate.')
