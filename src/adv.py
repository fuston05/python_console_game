import sys

from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     n= "foyer"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                n= "overlook",
                s= "outside",
                e= "narrow"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                s= "foyer"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                n= "treasure",
                w= "foyer"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                s= "narrow"),
}


# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Scott", room['outside'])

# Write a loop that:

userInput= None

# while not userInput == 'q':
currRoom= player.current_room
#
# * Prints the current room name


# * Prints the current description (the textwrap module might be useful here).
print(f'\nLocation: {currRoom.name}')
print(f' {currRoom.description}')
while not userInput == 'q':
  # * Waits for user input and decides what to do.
  userInput= input('\nChoose a direction: N, S, E, W: ').lower()
  # If the user enters a cardinal direction, attempt to move to the room there.
  # Print an error message if the movement isn't allowed.
  if userInput == 'n': 
    # check current room for directions
    if player.current_room.n_to:
      print('\nYou head north.')
      player.current_room= room[player.current_room.n_to]
      print(f'You arrive: {player.current_room}')
    else: print('\nCannot go North from here, try again')

  elif userInput == 's': 
      # check current room for directions
      if player.current_room.s_to:
        print('You head South.')
        player.current_room= room[player.current_room.s_to]
        print(f'You arrive: {player.current_room}')
      else: print('\nCannot go South from here, try again')

  elif userInput == 'e':
      # check current room for directions
      if player.current_room.e_to:
        print('You head East.')
        player.current_room= room[player.current_room.e_to]
        print(f'You arrive: {player.current_room}')
      else: print('\nCannot go East from here, try again')

  elif userInput == 'w':
      # check current room for directions
      if player.current_room.w_to:
        print('You head West.')
        player.current_room= room[player.current_room.w_to]
        print(f'You arrive: {player.current_room}')
      else: print('\nCannot go West from here, try again')

  elif userInput == 'q':
    print('\n*** Good Bye!! ***\n')
    sys.exit(1)

  else: 
    print('\nCannot move in that direction, try again\n')

# If the user enters "q", quit the game.
