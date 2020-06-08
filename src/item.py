class Item:
    def __init__(self, one_word_name, description, owner=None, is_useable= None, use_effect= None):
        self.name = one_word_name
        self.description = description
        self.owner = owner
        self.is_useable= is_useable
        self.use_effect= use_effect

    def on_use(self, player):
        # if useable item
        if self.is_useable:
            instructions= self.use_effect.split()
            action= (instructions[0]).lower().strip()
            noun= instructions[1].lower().strip()
            if action == 'port':
              print('\nYou decide walk into the portal. You are shrouded in darkness, and feel as though you\'re spinning out of control completely disoriented...')
              player.forceTravel(noun)

        # not a useable item.. food, potions etc that have a 'use' method
        else: 
          print('\nYou cannot use that')

    def on_take(self, item):
        print(f'\nYou picked up: {item.name}')

    def on_drop(self, item):
        print(f'\nYou dropped: {item.name}')

    def __str__(self):
        return f'Item: {self.name}, Descr: {self.description}'
