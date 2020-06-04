# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, n=None, s=None, e=None, w=None):
    self.name= name
    self.description= description
    self.n_to= n
    self.s_to= s
    self.e_to= e
    self.w_to= w

  def __str__(self):
    return f'{self.name}: {self.description}'