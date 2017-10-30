import items
import world
import random

class Player:
	
	def __init__(self):
		self.inventory = [
			items.RustyDagger(),
			items.CrustyBread(),
			items.GreenApple()
			]
		self.x = world.start_tile_location[0]
		self.y = world.start_tile_location[1]
		self.hp = 100
		self.gold = 0
		self.str = 1
		self.victory = False

	def is_alive(self):
		return self.hp > 0

	def print_inventory(self):
		print('\nInventory:')
		for item in self.inventory:
			if item == self.most_powerful_weapon():
				print('* {} +'.format(item)) # ◂
			else:
				print('* {}'.format(item))

	def status(self):
		print('_________Status_________')
		print('Health: {}/100  Gold: {}'.format(self.hp, self.gold))
		print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')

	def most_powerful_weapon(self):
		max_damage = 0
		best_weapon = None
		for item in self.inventory:
			try:
				if item.damage > max_damage:
					best_weapon = item
					max_damage = item.damage
			except AttributeError:
					pass
		if best_weapon == None:
			return items.Fist()
		return best_weapon
		
	def attack(self):
		weapon = self.most_powerful_weapon()
		room = world.tile_at(self.x, self.y)
		enemy = room.enemy
		player_dmg = int(round(((self.str / 100) + 1.04) * random.randint(0, weapon.damage)))
		player_max = int(round(((self.str / 100) + 1.04) * weapon.damage))
		if player_dmg == player_max:
			print('\nYou use your {} against the {} dealing {}* damage!!\n'.format(weapon.name, enemy.name, player_dmg))
		else:
			print('\nYou use {} against {} dealing {} damage!!\n'.format(weapon.name, enemy.name, player_dmg))
		enemy.hp -= player_dmg
		if not enemy.is_alive():
			print('You killed the {}'.format(enemy.name))
		else:
			print('{} HP is {}.'.format(enemy.name, enemy.hp))
			
	def heal(self):
		consumables = [item for item in self.inventory if isinstance(item, items.Consumable)]
		if not consumables:
			print('\nYou don\'t have any items to heal you!')
			return
		print('\nHere is what\'s avaliable to heal: ')
		for i, item in enumerate(consumables, 1):
			print('{}. {}'.format(i, item))

		valid = False
		while not valid:
			choice = input('\nChoose an item or press Q to exit: ')
			if choice in ['Q', 'q']:
				return
			else:
				try:
					to_eat = consumables[int(choice) - 1]
					self.hp = min(100, self.hp + to_eat.healing_value)
					self.inventory.remove(to_eat)
					print('\nYou\'ve gained {} health!'.format(to_eat.healing_value))
					valid = True
				except (ValueError, IndexError):
					print('Invalid choice, try again.')
				
	def trade(self):
		room = world.tile_at(self.x, self.y)
		room.check_if_trade(self)
		
		
	def move(self, dx, dy):
		self.x += dx
		self.y += dy
		
	def move_north(self):
		self.move(dx=0, dy=-1)
		
	def move_south(self):
		self.move(dx=0, dy=1)
		
	def move_east(self):
		self.move(dx=1, dy=0)
		
	def move_west(self):
		self.move(dx=-1, dy=0)

	#Built to allow for giving player any items.
	def override(self):
		item = input(':: ')
		if item in items.override.keys():
			self.inventory.append(items.override[item])
			print('\n{} overridden to player!'.format(items.override[item].name))
