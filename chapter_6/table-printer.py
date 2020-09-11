from functools import reduce

COL_SPACING = 1

def get_row_widths(result, line):
  output = result

  for cell_index in range(len(line)):
    cell_width = len(line[cell_index])
    if cell_width > output[cell_index]:
      output[cell_index] = cell_width

  return output

def print_table(data):
  row_widths = reduce(get_row_widths, data, [0] * len(data[0]))

  for line_index in range(len(data)):
    line = data[line_index]
    for cell_index in range(len(line)):
      cell = line[cell_index]
      row_width = row_widths[cell_index]
      end = '\n' if cell_index == len(line) - 1 else ''
      print(f'{cell.rjust(row_width)}'.center(row_width + COL_SPACING * 2), end=end)

table_data = [
  ['apples', 'oranges', 'cherries', 'banana'],
  ['Alice', 'Bob', 'Carol', 'David'],
  ['dogs', 'cats', 'moose', 'goose']
]

print_table(table_data)