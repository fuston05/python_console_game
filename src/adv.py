import sys
from player import Player
from existingRooms import room

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
# default starting room 'outside' is set in the Player class itself
player = Player("Scott")
userInput = None

# * Prints the current description (the textwrap module might be useful here).
print(f'\nCurrent Location: {player.current_room.name}')
print(f' {player.current_room.description}')

# items
if player.current_room.items:
  print(f'\nAs you look around you see:')
  for item in player.current_room.items:
    print(f'{item.name}: ')
    print(f' {item.description}')
else: print('no items in this room')

while not userInput == 'q':
    # * Waits for user input and decides what to do.
    userInput = input('\nChoose a direction: N, S, E, W, "Q" to quit: ').lower()

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    if userInput == 'n' or 's' or 'e' or 'w':
      player.changeRooms(userInput)

    elif userInput == 'q':
        print('\n*** Good Bye!! ***\n')
        sys.exit(1)
