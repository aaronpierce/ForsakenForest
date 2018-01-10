import os
import json
import random
import items, world, extras


class Player:

    def __init__(self):
        self.inventory = [
            items.Weapon('rusty dagger'),
            items.Consumable('crusty bread'),
            items.Consumable('green apple')
        ]
        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.hp = 100
        self.level = 1
        self.exp = 0
        self.gold = 0
        self.str = 1
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        print('\nInventory:')
        for item in self.inventory:
            if item == self.most_powerful_weapon():
                print('* {} +'.format(item))  # ◂
            else:
                print('* {}'.format(item))

    def status(self):
        left, right, bottom = 9, 9, 24
        if self.gold >= 1000:
            left += 1
            right += 1
            bottom += 2
        elif self.gold >= 100:
            left += 1
            right += 0
            bottom += 1

        # if self.gold >= 1000:
        #     left, right, bottom = 10, 10, 26
        # elif self.gold >= 100:
        #     left, right, bottom = 10, 9, 25
        # else:
        #     left, right, bottom = 9, 9, 24

        print('_' * left + 'Status' + '_' * right)
        print('Health: {}/100  Gold: {}'.format(self.hp, self.gold, self.exp, self.level))
        print('¯' * bottom)

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
        if best_weapon is None:
            return items.Weapon('fist')
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
            self.gain_exp(enemy.max_hp)
        else:
            print('{} HP is {}.'.format(enemy.name, enemy.hp))

    def heal(self):
        consumables = [item for item in self.inventory if isinstance(item, items.Consumable)]
        if not consumables:
            print('\nYou don\'t have any items to heal you!')
            return
        print('\nHere is what\'s available to heal: ')
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

    def check_levelup(self):
        if self.exp > extras.exp_table[self.level]:
            return True

    def gain_exp(self, enemy_hp):
        self.exp += enemy_hp * 2
        print('\nYou gained {} experience.'.format(enemy_hp * 2))
        if self.check_levelup():
            self.level += 1
            print('\nYou had advanced to a new level!! You are level {}!'.format(self.level))

    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)

    def load(self):
        save_file = extras.check_appdata()
        if os.path.exists(save_file):
            with open(save_file, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    if key == 'inventory':
                        for i in range(len(value)):
                            item = value[i]
                            for k, v in item.items():
                                if k in items.WEAPONS:
                                    obj = items.Weapon(k)
                                elif k in items.CONSUMABLES:
                                    obj = items.Consumable(k)
                                elif k in items.ITEMS:
                                    obj = items.Item(k)
                            value[i] = obj
                    self.__dict__[key] = value

                print('\nLoad Successful!')
                return True
        else:
            print('\nNo game saves found...')

    def save(self):
        save_file = extras.check_appdata()

        def to_json(obj):
            return obj.__dict__

        def inv_catch(obj):
            return {'{}'.format(obj.name.lower()): obj.__dict__}

        json_data = to_json(self)

        with open(save_file, 'w+') as f:
            f.write(json.dumps(json_data, indent=4, default=inv_catch))

        print('\nSave Successful!')

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

    # Built to allow for giving player any items.
    def override(self):
        item = input(':: ')
        if 'Gold' in item:
            gold, amount = item.split()
            self.gold += int(amount)
            print('\n{} gold overridden to player!'.format(amount))
        elif 'Health' in item:
            health, amount = item.split()
            self.hp += int(amount)
            print('\n{} health overriden to player!'.format(amount))
        elif item in items.override.keys():
            self.inventory.append(items.override[item])
            print('\n{} overridden to player!'.format(items.override[item].name))
