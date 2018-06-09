from time import *

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']

inventory['backpack'].remove('dagger')

inventory['gold'] += 50

for inventor in inventory:
    print(inventor + " " + str(inventory[inventor]).replace("[", "").replace("]", ""))

sleep(3)
