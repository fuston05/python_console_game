# Write a class to hold player information, e.g. what room they are in
# currently.
from existingRooms import room


class Player:
    def __init__(self, name, current_room=room['outside'], inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def whereAmI(self):
        print(
            f'\n You look around eventually reaize you are at: {self.current_room.name}: ')
        print(f'   {self.current_room.description}')

    def dispPlayerInventory(self):
        if len(self.inventory) >= 1:
            count = 1
            for i in self.inventory:
                print(f'\nitem_{count}: {i}')
                count += 1
        else:
            print('\nNothing in inventory')

    def getItem(self, item):
        # if item is in current room
        rem = None
        room = self.current_room
        rmItems = room.items

        for i in rmItems:
            if i.name == item:
                rem = i
        if rem:
            if not rem.is_global:
                # add item to player inventory
                self.inventory.append(rem)
                rem.owner = self
                rem.on_take(rem)
                # remove item from current room items
                rmItems.remove(rem)
            else: 
              print('You cannot "take" that. Maybe try "use"?')
        else:
            print('\nItem is not in this room')

    def useItem(self, item):
        # if item is in the current room
        rem = None
        room = self.current_room
        rmItems = room.items

        for i in rmItems:
            if i.name == item:
                rem = i
        if rem:
            rem.on_use(self)

    def dropItem(self, item):
        # if item is in inventory
        rem: None
        inv = self.inventory
        for i in inv:
            if i.name == item:
                rem = i
        if rem:
            # on_drop method from Item
            i.on_drop(i)
            # remove from player inventory
            self.inventory.remove(i)
            rem.owner = None
            # add item to room items
            self.current_room.items.append(i)
            self.current_room.dispRoomItems(self)

            self.dispPlayerInventory()

    def displayTravelInfo(self, dir):
        print(f'\nYou head {dir},')
        print(f'  You arrive at the {self.current_room.name}: ')
        print(f'    {self.current_room.description}')

    def changeRooms(self, direction):
        dir = (direction)

        if dir == 'n':
            # check if North is an option from current room
            if self.current_room.n_to:
                # set the new current_room
                self.current_room = room[self.current_room.n_to]
                self.displayTravelInfo('North')
                # display room items when you first enter
                self.current_room.dispRoomItems(self)
            else:
                print('\nCannot go North from here, try again')

        elif dir == 's':
            # check if South is an option from current room
            if self.current_room.s_to:
                # set the new current_room
                self.current_room = room[self.current_room.s_to]
                self.displayTravelInfo('South')
            else:
                print('\nCannot go South from here, try again')

        elif dir == 'e':
            # check if East is an option from current room
            if self.current_room.e_to:
                # set the new current_room
                self.current_room = room[self.current_room.e_to]
                self.displayTravelInfo('East')
            else:
                print('\nCannot go East from here, try again')

        elif dir == 'w':
            # check if West is an option from current room
            if self.current_room.w_to:
                # set the new current_room
                self.current_room = room[self.current_room.w_to]
                self.displayTravelInfo('West')
            else:
                print('\nCannot go West from here, try again')

        else:
            # if input direction is not an option from current room
            # or if unrecognized input
            print('\nCannot move in that direction, try again\n')

    def forceTravel(self, location):
      self.current_room= room[location]
      self.whereAmI()

    def __str__(self):
        return f'{self.name}: Room: {self.current_room}, methods: {self.changeRooms}'
