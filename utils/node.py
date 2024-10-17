class Node:
  def __init__(self, state, parent, action):
      self.state = state  
      self.parent = parent
      self.action = action
      self.cost = 0  

  def __hash__(self):
      return hash(self.state)

  def __eq__(self, other):
      return self.state == other.state