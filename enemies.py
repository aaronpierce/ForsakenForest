import random

class Enemy:
	def __init__(self):
		raise NotImplementedError('Do not create raw Enemy objects.')
		
	def __str__(self):
		return self.name
		
	def is_alive(self):
		return self.hp > 0
		
class GiantSpider(Enemy):
	def __init__(self):
		self.name = 'Giant Spider'
		self.hp = 10
		self.damage = 2

class Skeleton(Enemy):
	def __init__(self):
		self.name = 'Skeleton'
		self.hp = 20
		self.damage = 5
		
class Ork(Enemy):
	def __init__(self):

		self.name = 'Ogre'
		self.hp = 30
		self.damage = 10
		
class BatColony(Enemy):
	def __init__(self):
		self.name = 'Colony of Bats'
		self.hp = 70
		self.damage = 4
		
class RockMonster(Enemy):
	def __init__(self):
		self.name = 'Rock Monster'
		self.hp = 60
		self.damage = 15
		
class Boss(Enemy):
	def __init__(self):
		raise NotImplementedError('Do not create raw Boss objects.')

class AncientDragon(Boss):
	def __init__(self):
		self.name = 'Ancient Dragon'
		self.hp = 150
		self.damage = 25

		

def enemy_spawn():
	r = random.random()
	if r < 0.25:
		return [GiantSpider(),
				'A giant spider jumps down from its web in front of you!',
				'The corpse of a dead spider rots on the ground.']
	elif r < 0.50:
		return [Skeleton(),
				'Bones are thrown your way. A skeletal being comes your way.',
				'A collection of bones cover the ground.n']
	elif r < 0.80:
		return [Ork(),
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
				
				
