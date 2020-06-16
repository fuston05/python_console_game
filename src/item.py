from useEffects import *

class Item:
    def __init__(self, one_word_name, description, owner=None, is_useable=None, use_effect=None):
        self.name = one_word_name
        self.description = description
        self.owner = owner
        self.use_effect = use_effect

    def on_use(self, player):

        # if useable item
        if self.use_effect:
            instructions = self.use_effect.split()
            action = (instructions[0]).lower().strip()
            noun = instructions[1].lower().strip()
            # use effect from useEffects.py
            if action == 'port':
                port(player, noun)
        # if not useable item
        else:
            print('\nYou cannot "use" that')

    def on_take(self, item):
        print(f'\nYou picked up: {item.name}')

    def on_drop(self, item):
        print(f'\nYou dropped: {item.name}')

    def __str__(self):
        return f'Item: {self.name}, Descr: {self.description}'
