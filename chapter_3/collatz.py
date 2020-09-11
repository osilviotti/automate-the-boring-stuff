def collatz(number):
  is_even = number % 2 == 0
  value = None

  if is_even:
    value = number // 2
  else:
    value = 3 * number + 1

  print(value)
  return value
    

print('Enter an integer:')
user_value = None

try:
  user_value = int(input())
  value = None

  while value != 1:
    value = collatz(value or user_value)
except:
  print('"' + str(user_value) + '" is not a valid integer.')  
