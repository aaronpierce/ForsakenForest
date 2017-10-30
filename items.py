import random

class Weapon:
	def __init__(self):
		raise NotImplementedError('Do not create raw Weapon objects!')

	def __str__(self):
		return '{} (+{} DMG)'.format(self.name, self.damage)


class Rock(Weapon):
	def __init__(self):
		self.name = 'Rock'
		self.description = 'A fist-sized rock, suitable for bludgeoning.'
		self.damage = 5
		self.value = 1

class Fist(Weapon):
	def __init__(self):
		self.name = "your fist"
		self.description = 'Bare hands'
		self.damage = 3
		self.value = 0

class RustyDagger(Weapon):
	def __init__(self):
		self.name = 'Rusty Dagger'
		self.description = 'A small dagger with a little rust.'
		self.damage = 10
		self.value = 20

class RustySword(Weapon):
	def __init__(self):
		self.name = 'Rusty Sword'
		self.description = 'This sword is starting to rust.'
		self.damage = 15
		self.value = 50

class WornSword(Weapon):
	def __init__(self):
		self.name = 'Worn Sword'
		self.description = 'This sword is showing its age.'
		self.damage = 20
		self.value = 100

class FancySword(Weapon):
	def __init__(self):
		self.name = 'Fancy Sword'
		self.description = 'A noble sword once held by someone important.'
		self.damage = 50
		self.value = 250

class AncientSpear(Weapon):
	def __init__(self):
		self.name = 'Ancient Spear'
		self.description = 'An old spear with great hidden power'
		self.damage = 70
		self.value = 550

class LunarSword(Weapon):
	def __init__(self):
		self.name = 'Lunar Sword'
		self.description = 'A powerful sword that is powered by the moon.'
		self.damage = 65
		self.value = 500

class Potato(Weapon):
	def __init__(self):
		self.name = 'Potato'
		self.description = 'Just a \'tato.'
		self.damage = 10000000
		self.value = 0


class Consumable:
	def __init__(self):
		raise NotImplementedError('Do not create raw consumables object.')

	def __str__(self):
		return '{} (+{} HP)'.format(self.name, self.healing_value)

class CrustyBread(Consumable):
	def __init__(self):
		self.name = 'Crusty Bread'
		self.healing_value = 10
		self.value = 12

class GreenApple(Consumable):
	def __init__(self):
		self.name = 'Green Apple'
		self.healing_value = 25
		self.value = 30

class HealingPotion(Consumable):
	def __init__(self):
		self.name = 'Healing Potion'
		self.healing_value = 50
		self.value = 60

class Item():
	def __init__(self):
		raise NotImplementedError('Do not create raw Item objects!')

	def __str__(self):
		return '{}'.format(self.name)

class AncientKey(Item):
	def __init__(self):
		self.name = 'Ancient Key'



def drop_table(itemOnly = False):
	if not itemOnly:
		r = random.random()
	else:
		r = (random.randint(5, 10) / 10)
	if r < 0.50:
		drop = random.randint(1, 50)
	elif r < .52:
		drop = Rock()
	elif r < 0.71:
		drop = GreenApple()
	elif r < 0.90:
		drop = RustySword()
	elif r < 0.94:
		drop = HealingPotion()
	elif r < 0.98:
		drop = FancySword()
	else:
		drop = rare_drop_table()
	return drop

def rare_drop_table():
	r = random.random()
	if r < 0.70:
		drop = LunarSword()
	else:
		drop = AncientSpear()
	return drop

#Dict for using override function for player
override = {
	Potato().name: Potato(),
	LunarSword().name: LunarSword(),
	HealingPotion().name: HealingPotion(),
	AncientSpear().name: AncientSpear(),
	AncientKey().name: AncientKey()
}