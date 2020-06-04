class Item:
  def __init__(self, one_word_name, description):
    self.name= one_word_name
    self.description= description


  def __str__(self):
    return f'Item: {self.name}, Descr: {self.description}'