# Write a class to hold player information, e.g. what room they are in
# currently.
from existingRooms import room

class Player:
    def __init__(self, name, current_room= room['outside'], inventory= None):
        self.name = name
        self.current_room = current_room
        self.inventory= inventory

    def displayTravelInfo(self, dir):
      print(f'\nYou head {dir},')
      print(f'You arrive: {self.current_room.name}')

    def changeRooms(self, direction):
      dir= (direction)

      if dir == 'n':
        # check if North is an option from current room
        if self.current_room.n_to:
          # set the new current_room
          self.current_room = room[self.current_room.n_to]
          self.displayTravelInfo('North')
        else: print('\nCannot go North from here, try again')

      elif dir == 's':
        # check if South is an option from current room
        if self.current_room.s_to:
          # set the new current_room
          self.current_room = room[self.current_room.s_to]
          self.displayTravelInfo('South')
        else: print('\nCannot go South from here, try again')

      elif dir == 'e':
        # check if East is an option from current room
        if self.current_room.e_to:
          # set the new current_room
          self.current_room = room[self.current_room.e_to]
          self.displayTravelInfo('East')
        else: print('\nCannot go East from here, try again')

      elif dir == 'w':
        # check if West is an option from current room
        if self.current_room.w_to:
          # set the new current_room
          self.current_room = room[self.current_room.w_to]
          self.displayTravelInfo('West')
        else: print('\nCannot go West from here, try again')

      else: 
        # if input direction is not an option from current room 
        # or if unrecognized input
        print('\nCannot move in that direction, try again\n')

    def __str__(self):
        return f'{self.name}: Room: {self.current_room}, methods: {self.changeRooms}'
