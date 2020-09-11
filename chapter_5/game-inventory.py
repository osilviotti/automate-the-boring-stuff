def display_inventory(inventory):
  total_items = 0
  print('-' * 30)
  print('Inventory:')
  
  for key, value in inventory.items():
    print(key + ': ' + str(value))
    total_items += value

  print('Total number of items: ' + str(total_items))
  print('-' * 30)

def add_to_inventory(inventory, new_items):
  for item in new_items:
    inventory.setdefault(item, 0)
    inventory[item] += 1

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

display_inventory(inv)

loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

add_to_inventory(inv, loot)

display_inventory(inv)
