class Node:
    def __init__(self, state, parent, action):
      self.state = state  
      self.parent = parent
      self.action = action
      self.g = 0  
      self.h = 0  
      self.f = 0  


    
    def getPath(self):
        node = self
        path = []
        while node:
            path.append(node)
            node = node.parent
        
        return list(reversed(path))
    
    
    def getSolution(self):
        pass
    
    def setF(self):
        pass
    
