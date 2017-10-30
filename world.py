import random
import enemies
import npc
import items

class MapTile:
	def _init__(self, x, y):
		self.x = x
		self.y = y
		
	def intro_text(self):
		raise NotImplementedError('Create a subclass instead!')
		
	def modify_player(self, player):
		pass
		
		
class StartTile(MapTile):
	def __init__(self, x, y):
		super().__init__()
		self.x = x
		self.y = y

	
	def intro_text(self):
		return '''Not much to see. It appears that you can make out some faint paths around you.'''

class EnemyTile(MapTile):
	def __init__(self, x, y):
		super().__init__()
		self.x = x
		self.y = y
		self.drop_claimed = False
		self.drop = items.drop_table()
		enemy = enemies.enemy_spawn()
		self.enemy = enemy[0]
		self.alive_text = enemy[1]
		self.dead_text = enemy[2]
			
	def modify_player(self, player):
		enemy_dmg = int(round(((self.enemy.str / 100) + 1) * random.randint(0, self.enemy.dmg)))
		if self.enemy.is_alive():
			player.hp -= enemy_dmg
			print('Enemy does {} damage. You have {} HP remaining.\n'.format(enemy_dmg, player.hp))
		elif not self.enemy.is_alive() and not self.drop_claimed:
			self.drop_claimed = True
			if isinstance(self.drop, items.Weapon) or isinstance(self.drop, items.Consumable):
				player.inventory.append(self.drop)
				print('{} was dropped by the {} and added to your inventory!\n'.format(self.drop, self.enemy))
			else:
				player.gold += self.drop
				print('{} Gold was dropped by the {} and added to your inventory!\n'.format(self.drop, self.enemy))
		
	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text
			
				
				
class NormalTile(MapTile):
	def __init__(self, x, y):
		super().__init__()
		self.x = x
		self.y = y

	def intro_text(self):
		return """This is nothing interesting here."""
		
class VictoryTile(MapTile):
	def __init__(self, x, y):
		super().__init__()
		self.x = x
		self.y = y
	
	def modify_player(self, player):
		player.victory = True

	def intro_text(self):
		return """You see a bright light in the distance...\n... it grows as you get closer. Its sunlight!\n\nVictory is yours!!"""

class TraderTile(MapTile):
	def __init__(self, x, y):
		self.trader = npc.Trader()
		super().__init__()
		self.x = x
		self.y = y

	def trade(self, player, buyer, seller):
		for i, item in enumerate(seller.inventory, 1):
			print('{}. {} - {} Gold'.format(i, item.name, item.value))
		while True:
			user_input = input('Choose and item or press Q to exit: ')
			if user_input in ['Q', 'q']:
				return
			else:
				try:
					choice = int(user_input)
					to_swap = seller.inventory[choice - 1]
					self.swap(player, seller, buyer, to_swap)
				except ValueError:
					print('Invalid Choice!')

	def swap(self, player, seller, buyer, item):
		if item.value > buyer.gold:
			print("That's too expensive")
			return
		seller.inventory.remove(item)
		buyer.inventory.append(item)
		if seller == player:
			seller.gold = seller.gold + item.value
		else:
			seller.gold = seller.gold + item.value
			buyer.gold = buyer.gold - item.value
		print('Trade complete!')

	def check_if_trade(self, player):
		while True:
			print("\nWould you like to (B)uy, (S)ell, or (Q)uit?")
			user_input = input()
			if user_input in ['Q', 'q']:
				return
			elif user_input in ['B', 'b']:
				print("\nHere's whats available to buy: (Current Gold: {})".format(player.gold))
				self.trade(player, buyer=player, seller=self.trader)
			elif user_input in ['S', 's']:
				print("\nHere's whats avaliable to sell: ")
				self.trade(player, buyer=self.trader, seller=player)
			else:
				print("Invalid choice!")

	def intro_text(self):
		return """A frail not-quit-human, not-quit-creature squats in the corner clinking his gold coins together. He looks willing to trade."""

class FindGoldTile(MapTile):
	def __init__(self, x, y):
		self.gold = random.randint(1, 50)
		self.gold_claimed = False
		super().__init__()
		self.x = x
		self.y = y

	def modify_player(self, player):
		if not self.gold_claimed:
			self.gold_claimed = True
			player.gold = player.gold + self.gold
			print('++You pick up the {} Gold++\n'.format(self.gold))

	def intro_text(self):
		if self.gold_claimed:
			return """Another unremarkable part of the cave. You must forge onwards."""
		else:
			return """Someone dropped some gold. You pick it up."""

class FindItemTile(MapTile):
	def __init__(self, x, y):
		self.item_claimed = False
		super().__init__()
		self.x = x
		self.y = y
		self.item = items.drop_table(True)
		self.claimed_text = 'An emptied chest... nothing more to find here. Better move on.'
		self.unclaimed_text = 'You spot a partially opened chest on the ground. I wonder whats inside...'


	def modify_player(self, player):
		if not self.item_claimed:
			self.item_claimed = True
			player.inventory.append(self.item)
			print('++{} added to inventory++\n'.format(self.item))

	def intro_text(self):
		text = self.unclaimed_text if not self.item_claimed else self.claimed_text
		return text

class BossTile(MapTile):
	def __init__(self, x, y):
		super().__init__()
		self.x = x
		self.y = y
		self.enemy = enemies.AncientDragon()
		self.alive_text = 'An enormous dragon rips through the air with a loud screech and slams to the ground in front of you!!'
		self.dead_text = 'A slain dragon lays at your feet.'
		self.key_claimed = False

	def modify_player(self, player):
		enemy_dmg = int(round(((self.enemy.str / 100) + 1) * random.randint(0, self.enemy.dmg)))
		if self.enemy.is_alive():
			player.hp -=  enemy_dmg
			print('Enemy does {} damage. You have {} HP remaining.\n'.format(enemy_dmg, player.hp))
		if not self.key_claimed and not self.enemy.is_alive():
			self.key_claimed = True
			player.inventory.append(items.AncientKey())
			print('An {} was dropped by the {} and added to your inventory!\n'.format(items.AncientKey(), self.enemy))
		
		
	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

class AncientChestTile(MapTile):
	def __init__(self, x, y):
		super().__init__()
		self.x = x
		self.y = y
		self.item_claimed = False
		self.claimed_text = 'Alas, my reward for slaying the beast has been claimed.'
		self.unclaimed_text = 'An enormous chest sunken into the ground. You see what looks like a dragon on the face of the chest. Looks secure....'
		self.reward = items.AncientSpear()
	
	def modify_player(self, player):
		if any(items.AncientKey().name in y.name for y in player.inventory) and not self.item_claimed:
			print('This old key seems to be a snug, but perfect fit. Lets see whats inside...?\n')
			print('You\'ve found something that looks valuable.\n')
			print('{} was added to your inventory!\n'.format(self.reward))
			self.item_claimed = True
			player.inventory.append(self.reward)
			for item in player.inventory:
				if item.name == 'Ancient Key':
					player.inventory.remove(item)
					break
		elif not self.item_claimed:
			print('The right key might open this.\n')
			
	def intro_text(self):
		text = self.claimed_text if self.item_claimed else self.unclaimed_text
		return text
			

world_map = []

#0  1  2  3  4
world_dsl = '''
|  |  |BT|  |  |  |
|EN|EN|NT|NT|EN|NT|
|NT|  |  |AC|  |EN|
|EN|FG|EN|  |FI|*T|
|*T|  |ST|  |  |EN|
|FG|  |FG|EN|NT|FG|
|NT|FI|EN|  |  |EN|
'''

#Original Map(v1)
#world_dsl = '''
#|  |VT|  |
#|  |EN|  |
#|EN|ST|EN|
#|  |EN|  |
#'''

tile_type_dict = {
	"VT" : VictoryTile,
	"NT" : NormalTile,
	"EN" : EnemyTile,
	"ST" : StartTile,
	"FG" : FindGoldTile,
	"*T" : TraderTile,
	"FI" : FindItemTile,
	"BT" : BossTile,
	"AC" : AncientChestTile,
	"  " : None
}

def is_dsl_valid(dsl):
	if dsl.count("|ST|") != 1:
		return False
	#if dsl.count("|VT|") == 0:
	#	return False
	lines = dsl.splitlines()
	lines = [l for l in lines if l]
	pipe_counts = [line.count("|") for line in lines]
	for count in pipe_counts:
		if count != pipe_counts[0]:
			return False
	return True

start_tile_location = None

def parse_world_dsl():
	if not is_dsl_valid(world_dsl):
		raise SyntaxError("DSL is invalid!")

	dsl_lines = world_dsl.splitlines()
	dsl_lines = [x for x in dsl_lines if x]

	for y, dsl_row in enumerate(dsl_lines):
		row = []
		dsl_cells = dsl_row.split("|")
		dsl_cells = [c for c in dsl_cells if c]
		for x, dsl_cell in enumerate(dsl_cells):
			tile_type = tile_type_dict[dsl_cell]
			if tile_type == StartTile:
				global start_tile_location
				start_tile_location = x, y
			row.append(tile_type(x, y) if tile_type else None)

		world_map.append(row)

def tile_at(x, y):
	if x < 0 or y < 0:
		return None
	try:
		return world_map[y][x]
	except IndexError:
		return None
