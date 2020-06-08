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

# default starting room 'outside' is set in the Player class itself
player = Player("Scott", inventory=[item['torch']])
userInput = None

player.whereAmI()
player.current_room.dispRoomItems(player)

while not userInput == 'q':
    # * Waits for user input and decides what to do.
    userInput = input(
        '\nChoose a direction: N, S, E, W, "Q" to quit: ').lower().strip()

    # if a 2 word input was given
    if len(userInput.split()) == 2:
        # split user input into 2 words
        userInput = userInput.split()

        # two word commands
        # grab 1st letter of the action "use, take, drop"
        action = userInput[0][0]
        noun = userInput[1]

        # grab or take
        if action == 'g' or action == 't':
            player.takeItem(noun)

        # drop
        elif action == 'd':
            player.dropItem(noun)
        # use
        elif action == 'u':
            player.useItem(noun)

        # unrecognized input
        else:
            print('\nDid not recognize that command. Try again.')

    # if a single word input was given
    elif len(userInput.split()) == 1:
        # grab 1st letter
        firstInput = userInput[0]
        # single input commands
        # directions: accepts full words (North, South etc)
        if firstInput == 'n' or firstInput == 's' or firstInput == 'e' or firstInput == 'w':
            dir = firstInput
            player.changeRooms(dir)

        elif firstInput == 'i':
            player.dispPlayerInventory()

        # quit or 'q'
        elif firstInput == 'q':
            print('\n*** Good Bye!! ***\n')
            sys.exit(1)

        # unrecognized input
        else:
            print('\nDid not recognize that command. Try again.')

    else:
        # if input is more than 2 words
        # todo: add a help menu to show cammand options
        print('\nInvalid command format, try again')
