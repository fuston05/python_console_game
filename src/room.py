# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n=None, s=None, e=None, w=None, p= None, items=[]):
        self.name = name
        self.description = description
        self.n_to = n
        self.s_to = s
        self.e_to = e
        self.w_to = w
        self.p_to= None
        self.items = items

    def dispRoomItems(self, player):
        # items
        if player.current_room.items:
            print(f'\nAs you look around you see:')
            for item in player.current_room.items:
                print(f'   {item.name}: ')
                print(f'      {item.description}')
        else:
            print('\nNo items in this room')

    def __str__(self):
        return f'{self.name}: {self.description}'
