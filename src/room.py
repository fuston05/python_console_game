# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n=None, s=None, e=None, w=None, items=[], is_lit=False):
        self.name = name
        self.description = description
        self.n_to = n
        self.s_to = s
        self.e_to = e
        self.w_to = w
        self.items = items
        self.is_lit = is_lit

    def dispRoomItems(self, player):
        # if there are items in the room
        if player.current_room.items:
            # if room or player has light
            if self.is_lit == True:
                print(f'\nAs you look around you see:')
                for item in player.current_room.items:
                    print(f'   {item.name}: ')
                    print(f'      {item.description}')
            # if no light
            else:
                print('\nYou cannot see anything, it\'s too dark.')
        else:
            print('\nNo items in this room')

    def __str__(self):
        return f'{self.name}: {self.description}'
