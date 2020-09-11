import re

play_game = True
current_player = 'O' # this being global ensures same player doesn't always start

readable_positions = {
  't': 'Top',
  'm': 'Middle',
  'b': 'Bottom',
  'l': 'Left',
  'r': 'Right'
}

positions = [
  'tl',
  't',
  'tr',
  'ml',
  'm',
  'mr',
  'bl',
  'b',
  'br'
]

def get_moves_key():
  result = ''

  for i in range(len(positions)):
    prefix = ', '

    if i == 0:
      prefix = ''
    
    value = positions[i]
    readable = map(lambda k: readable_positions[k], list(value))

    result += prefix + value + ' (' + ' '.join(readable) + ')'

  return result

def print_board(current_board):
  print('\n')
  for row_start in range(0, len(positions), 3):
    if row_start != 0:
      print('--+---+--')

    print(
      current_board[positions[row_start]] + ' | ' +
      current_board[positions[row_start + 1]] + ' | ' +
      current_board[positions[row_start + 2]]
    )
  print('\n')

def check_victory(cb):
  win = False

  win = win or cb['tl'] != ' ' and cb['tl'] == cb['t'] == cb['tr']
  win = win or cb['ml'] != ' ' and cb['ml'] == cb['m'] == cb['mr']
  win = win or cb['bl'] != ' ' and cb['bl'] == cb['b'] == cb['br']

  win = win or cb['tl'] != ' ' and cb['tl'] == cb['ml'] == cb['bl']
  win = win or cb['t'] != ' ' and cb['t'] == cb['m'] == cb['b']
  win = win or cb['tr'] != ' ' and cb['tr'] == cb['mr'] == cb['br']

  win = win or cb['tl'] != ' ' and cb['tl'] == cb['m'] == cb['br']
  win = win or cb['tr'] != ' ' and cb['tr'] == cb['m'] == cb['bl']
  
  return win

def take_turn(current_board, player):
  move = None

  while not move in positions:
    print('Enter your move player ' + player + ':')
    move = input()
    if move in current_board and current_board[move] != ' ':
      print('Space occupied.')
      move = None

  current_board[move] = player

def game():
  global current_player
  remaining_turns = 9
  victory = False
  board = {}

  for position in positions:
    board.setdefault(position, ' ')

  print('Valid moves: ' + get_moves_key())
  print_board(board)

  while remaining_turns > 0 and not victory:
    current_player = 'O' if current_player == 'X' else 'X'
    take_turn(board, current_player)
    remaining_turns -= 1
    print_board(board)
    victory = check_victory(board)

  if victory:
    print('Congratulations player ' + current_player + '! You win!')
  else:
    print('NOBODY WINS.')

while play_game:
  game()
  print('Play again? (Y/n)', end='\n\n')
  new_game = input()
  play_game = re.match('y', new_game, re.IGNORECASE) or not new_game