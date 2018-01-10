import items


class NonPlayableCharacter:
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects.")

    def __str__(self):
        return self.name


class Trader(NonPlayableCharacter):

    def __init__(self):
        self.name = "Trader"
        self.gold = 1000000
        self.inventory = [
            items.Consumable('crusty bread'),
            items.Consumable('crusty bread'),
            items.Consumable('green apple'),
            items.Consumable('green apple'),
            items.Consumable('healing potion'),
            items.Consumable('healing potion'),
            items.Weapon('worn sword'),
            items.Weapon('fancy sword'),
            items.Weapon('lunar sword')
        ]

    # Used to pull a random sample from a list and put those into a list
    # [items.Weapon(each) for each in random.sample(list(items.WEAPONS), 2)]
