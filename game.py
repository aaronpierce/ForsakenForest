import sys
from collections import OrderedDict
from player import Player
import world
import items
import extras

def play():

	GameExit = False
	while not GameExit:
		extras.title()
		world.parse_world_dsl()
		choice = ''
		player = Player()
		while choice not in ['1', '2', '3']:
			print('\nSelect an option:\n1. Start New Game\n2. Load Game\n3. Quit')
			choice = input('> ')
			if choice == '1':
				pass
			elif choice == '2':
				if player.load() == True:
					pass
				else:
					choice = ''
					continue
			elif choice == '3':
				sys.exit()
		while player.is_alive() and not player.victory:
			room = world.tile_at(player.x, player.y)
			print('\n'+room.intro_text()+'\n')
			room.modify_player(player)
			if player.is_alive() and not player.victory:
				choose_action(room, player)
			elif not player.is_alive():
				print("\nYour journey has come to an early end!\n")
				input('Press enter to continue...')
	

def get_available_actions(room, player):
	actions = OrderedDict()
	player.status()
	print('Choose an action:')
	if player.inventory:
		action_adder(actions, 'i', player.print_inventory, 'Inventory')
	if isinstance(room, world.TraderTile):
		action_adder(actions, 't', player.trade, 'Trade')
	if (isinstance(room, world.EnemyTile) or isinstance(room, world.BossTile)) and room.enemy.is_alive():
		action_adder(actions, 'a', player.attack, 'Attack')
	else:
		if world.tile_at(room.x, room.y - 1):
			action_adder(actions, 'n', player.move_north, 'Go North')
		if world.tile_at(room.x, room.y + 1):
			action_adder(actions, 's', player.move_south, 'Go South')
		if world.tile_at(room.x + 1, room.y):
			action_adder(actions, 'e', player.move_east, 'Go East')
		if world.tile_at(room.x - 1, room.y):
			action_adder(actions, 'w', player.move_west, 'Go West')
	if player.hp < 100 and any(isinstance(y, items.Consumable) for y in player.inventory):
		action_adder(actions, 'h', player.heal, 'Heal')
	
	action_adder(actions, '?', extras.game_help, '')
	action_adder(actions, '+', player.save, '')
	action_adder(actions, '-', player.load, '')

	 # Only Enable Override function for testing.
	#action_adder(actions, '~', player.override, '')
		
	return actions
		
def action_adder(action_dict, hotkey, action, name):
	action_dict[hotkey.lower()] = action
	action_dict[hotkey.upper()] = action
	if hotkey not in ['~', '-', '+', '?']:								# This is for hiding override control
		print('{}: {}'.format(hotkey, name))
def choose_action(room, player):
	action = None
	while not action:
		available_actions = get_available_actions(room, player)
		action_input = input('Action: ')
		action = available_actions.get(action_input)
		if action:
			action()
		else:
			print("\nInvalid action - Use '?' for help.\n")

play()


#NOTES:
#Add another NPC who can give a quest. Then, add another tile type where the player
#completes something and returns to completes the quest with rewards.
#Puzzle Tile?
#Give the player magic attacks that deplete mana. Allow mana to replenish a little bit each
#time the player moves into a room and/or with a potion/or over real time.
#Have health gain over time?
#Delay messages to the screen.
#Allow the player to wear armor which reduces enemy attacks by a percentage.
#Use player leveling system
#Save/Load player saves
#Offer play again
#Allow item equipping. (Currently based on strongest item)
#Add a class/tier/level to weapons
#Allow above or below ground areas

