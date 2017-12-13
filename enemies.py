import random
from GameEntities import ObjectImport

class Enemy:
	def __init__(self, template):
		self.__dict__.update(ENEMIES[template])
		
	def __str__(self):
		return self.name
		
	def is_alive(self):
		return self.hp > 0
	
ENEMIES = ObjectImport.load('enemies')

def enemy_spawn():
	r = random.random()
	if r < 0.25:
		enemy = Enemy('gruesome spider')
	elif r < 0.50:
		enemy = Enemy('skeleton')
	elif r < 0.80:
		enemy = Enemy('orc')
	elif r < 0.95:
		enemy = Enemy('colony of bats')
	else:
		enemy = Enemy('rock monster')
	return enemy

skeleton = Enemy('skeleton')

