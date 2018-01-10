import random
import extras


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


class Item:
    def __init__(self, template):
        self.__dict__.update(ITEMS[template])

    def __str__(self):
        return '{}'.format(self.name)


WEAPONS = extras.load('weapons')
CONSUMABLES = extras.load('consumables')
ITEMS = extras.load('items')
TABLES = extras.load('drop_tables')


def drop(table, gold=True):
    item_drop = ''
    complete = False

    while not complete:
        pick = random.choice(TABLES[table])

        if pick in WEAPONS:
            item_drop = Weapon(pick)
        elif pick in CONSUMABLES:
            item_drop = Consumable(pick)
        elif pick in ITEMS:
            item_drop = Item(pick)
        elif gold and pick == 'gold':
            item_drop = random.randrange(10, 100)
        elif not gold and pick == 'gold':
            continue
        complete = True
    return item_drop


# drop = random.choices(drops, weights=probabilities, k=1000)

# Code for creating override function to provide testing!

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
