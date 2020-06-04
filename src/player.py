# Write a class to hold player information, e.g. what room they are in
# currently.
from existingRooms import room

class Player:
    def __init__(self, name, current_room= room['outside']):
        self.name = name
        self.current_room = current_room

    def changeRooms(self, direction):
      dir= (direction).lower()

      if dir == 'n':
        # check if North is an option from current room
        if self.current_room.n_to:
          self.current_room = room[self.current_room.n_to]
          print('\nYou head north.')
          print(f'You arrive: {self.current_room}')
        else: print('\nCannot go North from here, try again')

      elif dir == 's':
        # check if South is an option from current room
        if self.current_room.s_to:
          self.current_room = room[self.current_room.s_to]
          print('\nYou head South.')
          print(f'You arrive: {self.current_room}')
        else: print('\nCannot go South from here, try again')

      elif dir == 'e':
        # check if East is an option from current room
        if self.current_room.e_to:
          self.current_room = room[self.current_room.e_to]
          print('\nYou head East.')
          print(f'You arrive: {self.current_room}')
        else: print('\nCannot go East from here, try again')

      elif dir == 'w':
        # check if West is an option from current room
        if self.current_room.w_to:
          self.current_room = room[self.current_room.w_to]
          print('\nYou head into the wild, wild West.')
          print(f'You arrive: {self.current_room}')
        else: print('\nCannot go West from here, try again')

      else: 
        # if input is not an option from current room 
        # or if unrecognized input
        print('\nCannot move in that direction, try again\n')

    def __str__(self):
        return f'{self.name}: Room: {self.current_room}'
