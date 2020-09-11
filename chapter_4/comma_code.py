def commarise(list):
  result = ''

  for i in range(len(list)):
    prefix = ', '

    if i == len(list) - 1:
      prefix = ', and '
    elif i == 0:
      prefix = ''

    result += prefix + str(list[i])
  
  return result


print(commarise([1, 2, 3, 4, 5]))

print(commarise(['a', 'b', 'c']))
