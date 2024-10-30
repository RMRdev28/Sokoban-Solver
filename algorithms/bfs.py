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
        
        while len(self.open) > 0:
            print("step Number: ", i)
            i+=1
            current = self.open.popleft()
            self.closed.append(current)
            for action, state in current.state.successorFunction():
                child = Node(state, current, action)

                if child.state not in [node.state for node in self.closed] and child.state not in [node.state for node in self.open]:
                    if child.state.isGoal(): 
                        print("Number of steps to reach goal: ", i) 
                        return child
                    else:
                
                        self.open.append(child)

        return None
        
        
