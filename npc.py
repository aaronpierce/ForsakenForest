import items


class NonPlayableCharacter():
	def __init__(self):
		raise NotImplementedError("Do not create raw NPC objects.")

	def __str__(self):
		return self.name

class Trader(NonPlayableCharacter):
	def __init__(self):
		self.name = "Trader"
		self.gold = 1000000
		self.inventory = [
			items.CrustyBread(),
			items.CrustyBread(),
			items.GreenApple(),
			items.GreenApple(),
			items.HealingPotion(),
			items.HealingPotion(),
			items.WornSword(),
			items.FancySword(),
			items.LunarSword()
		]
