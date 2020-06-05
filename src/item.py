class Item:
    def __init__(self, one_word_name, description):
        self.name = one_word_name
        self.description = description

    def on_take(self, item):
      print(f'\nYou picked up: {item.name}')

    def on_drop(self, item):
      print(f'\nYou dropped: {item.name}')

    def __str__(self):
        return f'Item: {self.name}, Descr: {self.description}'
