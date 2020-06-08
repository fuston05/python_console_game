from item import Item

item = {
    'book': Item('book', "Very old and dusty, you can't make out the writing on the cover"),
    'sword': Item('sword', 'Rusty old sword'),
    'key': Item('key', 'Shiny gold skeleton key'),
    'chest': Item('chest', 'Dusty old locked chest'),
    'torch': Item('torch', 'Used wooden torch'),
    'bag': Item('bag', 'It\'s full of gold! Looks to be about 25GP.'),
    'portal': Item('portal', 'a portal of glowing blue light', is_useable=True, use_effect= 'port outside'),
}
