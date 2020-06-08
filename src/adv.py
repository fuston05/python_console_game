import sys
from player import Player
from existingRooms import room
from existingItems import item

# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].n_to = room['portal']
# room['portal'].s_to = room['treasure']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# default starting room 'outside' is set in the Player class itself
player = Player("Scott", inventory=[item['torch']])
userInput = None

# * Prints the current description (the textwrap module might be useful here).
# print(f'\nCurrent Location: {player.current_room.name}')
# print(f' {player.current_room.description}')
player.whereAmI()
player.current_room.dispRoomItems(player)

while not userInput == 'q':
    # * Waits for user input and decides what to do.
    userInput = input(
        '\nChoose a direction: N, S, E, W, "Q" to quit: ').lower()

    # if a 2 word input was given
    if len(userInput.split()) == 2:
        userInput = userInput.split()
        # dual input commands
        # grab 1st letter
        action = userInput[0][0].lower().strip()
        noun = userInput[1].lower().strip()

        if action == 'g' or action == 't':
            player.takeItem(noun)

        elif action == 'd':
            player.dropItem(noun)
        elif action == 'u':
            player.useItem(noun)
        
        # unrecognized input
        else: 
          print('\nDid not recognize that command. Try again.')

    # if a single word input was given
    elif len(userInput.split()) == 1:
        # grab 1st letter
        firstInput= userInput[0]
        # single input commands
        if firstInput == 'n' or firstInput == 's' or firstInput == 'e' or firstInput == 'w':
            dir= firstInput
            player.changeRooms(dir)

        elif firstInput == 'i':
            player.dispPlayerInventory()

        elif firstInput == 'q':
            print('\n*** Good Bye!! ***\n')
            sys.exit(1)

    else:
        print('\nInvalid command, try again')
