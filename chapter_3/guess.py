import random
import re

play_game = True

def game(max_guesses = 10):
  number = random.randint(1, 100)
  guesses_remaining = max_guesses
  last_guess = None

  print('What number between 1 and 100 am I thinking of?')
  while guesses_remaining > 0:
    guesses_remaining -= 1

    print('What is your guess?')
    last_guess = int(input())

    if last_guess == number:
      print('You win! It took you ' + str(max_guesses - guesses_remaining) + ' guesses.')

    diff = last_guess - number
    
    if diff > 20:
      print('Way too high')
    elif diff > 5:
      print('Too high')
    elif diff > 0:
      print('Slightly too high')
    elif diff < -20:
      print('Way too low')
    elif diff < -5:
      print('Too low')
    elif diff < 0:
      print('Slightly too low')

  if guesses_remaining == 0:
    print('You didn\'t guess the correct number. It was ' + str(number) + '.')

while play_game:
  game()
  print('Play again? (Y/n)', end='\n\n')
  new_game = input()
  play_game = re.match('y', new_game, re.IGNORECASE) or not new_game
