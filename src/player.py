from existingRooms import room


class Player:
    def __init__(self, name, current_room=room['outside'], inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def dispPlayerInventory(self):
        if len(self.inventory) >= 1:
            count = 1
            for i in self.inventory:
                print(f'\nitem_{count}: {i}')
                count += 1
        else:
            print('\nNothing in inventory')

    def takeItem(self, item):
        # if item is in current room
        rem = None
        room = self.current_room
        rmItems = room.items

        for i in rmItems:
            if i.name == item:
                rem = i
        if rem:
            if not rem.is_useable:
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
        rem = None
        room = self.current_room
        plrInv = self.inventory
        rmItems = room.items

        # if item is in current room
        for i in rmItems:
            if i.name == item:
                rem = i
        # if item is in player inventory
        for j in plrInv:
            if j.name == item:
                rem = j
        if rem:
            rem.on_use(self)

    def dropItem(self, item):
        rem: None
        inv = self.inventory
        for i in inv:
            if i.name == item:
                rem = i
        if rem:
            # if item is in player inventory
            # on_drop method from Item
            rem.on_drop(rem)
            # remove from player inventory
            self.inventory.remove(rem)
            rem.owner = None
            # add item to room items
            self.current_room.items.append(rem)
            # display rooom items
            self.current_room.dispRoomItems(self)

            self.dispPlayerInventory()

    def whereAmI(self):
        print(
            f'\n You look around eventually reaize you are at: {self.current_room.name}: ')
        print(f'   {self.current_room.description}')

    def displayTravelInfo(self, dir):
        print(f'\nYou head {dir},')
        print(f'  You arrive at the {self.current_room.name}: ')
        print(f'    {self.current_room.description}')

    def changeRooms(self, direction):
        dr = f'{direction}_to'

        # check if North is an option from current room
        if getattr(self.current_room, dr, False):
            newRoom = getattr(self.current_room, dr, False)
            # set the new current_room
            self.current_room = room[newRoom]
            self.displayTravelInfo('North')
            # display room items when you first enter
            self.current_room.dispRoomItems(self)
        else:
            print('\nYou cannot go that direction, try again')

    def forceTravel(self, location):
        self.current_room = room[location]
        self.whereAmI()

    def __str__(self):
        return f'{self.name}: Room: {self.current_room}, methods: {self.changeRooms}'
