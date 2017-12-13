import random
from GameEntities import ObjectImport

class Weapon:
	def __init__(self, template):
		self.__dict__.update(WEAPONS[template])

	def __str__(self):
		return '{} (+{} DMG)'.format(self.name, self.damage)

class Consumable:
	def __init__(self, template):
		self.__dict__.update(CONSUMABLES[template])

	def __str__(self):
		return '{} (+{} HP)'.format(self.name, self.healing_value)

class Item():
	def __init__(self, template):
		self.__dict__.update(ITEMS[template])

	def __str__(self):
		return '{}'.format(self.name)

WEAPONS = ObjectImport.load('weapons')
CONSUMABLES = ObjectImport.load('consumables')
ITEMS = ObjectImport.load('items')
TABLES = ObjectImport.load('drop_tables')

def drop(table, gold=True):
	drop = ''
	complete = False
	
	while not complete:
		pick = random.choice(TABLES[table])
		
		if pick in WEAPONS:
			drop = Weapon(pick)
		elif pick in CONSUMABLES:
			drop = Consumable(pick)
		elif pick in ITEMS:
			drop = Item(pick)
		elif gold == True and pick == 'gold':
			drop = random.randrange(10,100)
		elif gold == False and pick == 'gold':
			continue
		complete = True
	return drop
		
	#drop = random.choices(drops, weights=probs, k=1000)

# Code for creating ovveride function to provide testing!

def override_generate():
	data = {}
	for item in WEAPONS:
		data[WEAPONS[item]['name']] = Weapon(item)
	for item in CONSUMABLES:
		data[CONSUMABLES[item]['name']] = Consumable(item)
	for item in ITEMS:
		data[ITEMS[item]['name']] = Item(item)
	return data

override = override_generate()

