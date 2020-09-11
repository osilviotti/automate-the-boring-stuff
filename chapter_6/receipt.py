# should actually use the Decimal class for prices
price_format = '{:.2f}'

def print_receipt(cart):
  total_cost = 0

  for item in cart:
    if item['qty'] > 1:
      line_total = item['qty'] * item['cost']
      total_cost += line_total

      print(item['name'].ljust(32, '.'))
      print(
        str(item['qty']).rjust(8) + ' @' +
        price_format.format(item['cost']).rjust(7) +
        price_format.format(line_total).rjust(15)
      )
    else:
      print(item['name'].ljust(25, '.') + price_format.format(item['cost']).rjust(7, '.'))
  
  print(('Total: ' + price_format.format(total_cost)).rjust(32))
  print('\n')
  print(' Come again! '.center(32, '='))

cart = [
  { 'name': 'Bread', 'qty': 3, 'cost': 1.99 },
  { 'name': 'Peanut Butter', 'qty': 1, 'cost': 3.49 },
  { 'name': 'Beer', 'qty': 12, 'cost': 2.50 },
  { 'name': 'Cheese', 'qty': 2, 'cost': 1.79 },
  { 'name': 'Football Stickers', 'qty': 8, 'cost': 0.79 },
  { 'name': 'Crisps', 'qty': 1, 'cost': 1.29 }
]

print_receipt(cart)
