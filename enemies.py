import random

class Enemy:
	def __init__(self):
		raise NotImplementedError('Do not create raw Enemy objects.')
		
	def __str__(self):
		return self.name
		
	def is_alive(self):
		return self.hp > 0
		
class GruesomeSpider(Enemy):
	def __init__(self):
		self.name = 'Gruesome Spider'
		self.hp = 10
		self.str = 1
		self.dmg = 5

class Skeleton(Enemy):
	def __init__(self):
		self.name = 'Skeleton'
		self.hp = 20
		self.str = 2
		self.dmg = 10
		
class Orc(Enemy):
	def __init__(self):

		self.name = 'Orc'
		self.hp = 30
		self.str = 5
		self.dmg = 12
		
class BatColony(Enemy):
	def __init__(self):
		self.name = 'Colony of Bats'
		self.hp = 70
		self.str = 2
		self.dmg = 6
		
class RockMonster(Enemy):
	def __init__(self):
		self.name = 'Rock Monster'
		self.hp = 60
		self.str = 10
		self.dmg = 20
		
class Boss(Enemy):
	def __init__(self):
		raise NotImplementedError('Do not create raw Boss objects.')

class AncientDragon(Boss):
	def __init__(self):
		self.name = 'Ancient Dragon'
		self.hp = 150
		self.str = 10
		self.dmg = 30
		

def enemy_spawn():
	r = random.random()
	if r < 0.25:
		return [GruesomeSpider(),
				'A gruesome spider jumps down from its web in front of you!',
				'The corpse of a dead spider rots on the ground.']
	elif r < 0.50:
		return [Skeleton(),
				'Suddenly bones coming flying toward you. A erie looking skeletal starts running toward you!',
				'A collection of bones cover the ground.']
	elif r < 0.80:
		return [Orc(),
				'An ork is blocking your path!',
				'A dead ork reminds you of your triumph.']
	elif r < 0.95:
		return [BatColony(),
				'You hear a squeaking noise growing louder... Suddenly you are lost in a swarm if bats!',
				'Dozens of dead bats are scattered on the ground.']
	else:
		return [RockMonster(),
				'You\'ve disturbed a rock monster from his slumber!',
				'Defeated, the monster has reverted into an ordinary rock.']
				
				
