from room import Room
from existingItems import item

# Declare all the rooms
# Room("name", "description", "n", "s", "e", "w", )

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", n="foyer", items= [item['sword']], is_lit= True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", n="overlook", s="outside", e="narrow", items= [item['key']], is_lit= True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", s="foyer", items= [item['chest']], is_lit= True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", n="treasure", w="foyer", items= [item['book']], is_lit= True),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",n= 'portal', s="narrow",items= [item['bag']], is_lit= True),

    'portal': Room("Portal Room", """As you approach you see a glowing blue light that seems to be producing a low whirring sound. It's coming from a large magical portal in the center of the room. The only way out is back to the South... or is it?""", s="treasure", items= [item['portal']], is_lit= True),
}
