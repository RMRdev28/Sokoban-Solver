from utils.node import Node
from collections import deque

class Bfs:
    def __init__(self,state):
        self.state = state
        self.open = deque()
        self.closed = []
        self.initNode = Node(state, None, None)
        
    
    def bfsSearch(self):
        i = 1
        if self.state.isGoal():
            return self.initNode
        
        self.open.append(self.initNode)
        self.closed = []
        
        while len(self.open) > 0:
            current = self.open.popleft()
            self.closed.append(current)
            
            
            for action, state in current.state.successorFunction():
                child = Node(state, current, action)
                print(f"{child.state} Step: {i}")
                i += 1
                
                if child.state not in [node.state for node in self.closed] and child not in self.open:
                    if state.isGoal():  
                        
                        print("Goal")
                        print(child.getPath())
                        return child
                    self.open.append(child)
    
        return None
        
        
