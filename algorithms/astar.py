from utils.node import Node
from collections import deque

class AStar:
    def __init__(self, state):
        self.state = state
        self.open = deque()
        self.closed = []
        self.hFunction = None
        self.initNode = Node(state, None, None)
        self.initNode.g = 0
        self.initNode.h = self.h1(state)
        self.initNode.f = self.initNode.g + self.initNode.h
        
    def h1(self, state):
        misplaced = 0
        for box in state.boxes:
            if box not in state.goals:
                misplaced += 1
        return misplaced
    
    def manhattan_distance(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        return abs(x1 - x2) + abs(y1 - y2)
    
    def h2(self, state):
        misplaced = self.h1(state)
        misplacedCost = 2 * misplaced
        totalMinDistance = 0
        
        for box in state.boxes:
            if box not in state.goals: 
                minDistance = float('inf')
                for goal in state.goals:
                    distance = self.manhattan_distance(box, goal)
                    minDistance = min(minDistance, distance)
                totalMinDistance += minDistance
        
        return misplacedCost + totalMinDistance
    
    

    
    def h3(self, state):
        h2Value = self.h2(state)
        unmatchedBoxes = [box for box in state.boxes if box not in state.goals]
        
        if unmatchedBoxes:
           
            playerToBoxDistance = [
                self.manhattan_distance(state.player, box) 
                for box in unmatchedBoxes
            ]
            minPlayerDistance = min(playerToBoxDistance)

            return h2Value + minPlayerDistance
        
        return h2Value
            
            

    def getLowesFNode(self):
        if not self.open:
            return None
        
        lowestFNode = self.open[0]
        lowestF = lowestFNode.f
        
        for node in self.open:
            if node.f < lowestF:
                lowestF = node.f
                lowestFNode = node
                
        self.open.remove(lowestFNode)
        return lowestFNode
    
    def aStarSearch(self):
        self.open.append(self.initNode)
        if self.state.isGoal():
            return self.initNode
        i = 1
   
        
        while len(self.open) > 0:
            current = self.getLowesFNode()
            if current.state.isGoal():
                print("Number of steps to reach goal: ", i)
                return current
            self.closed.append(current)
            print("step Number: ", i)
            i+=1    
            
            for action, state in current.state.successorFunction():
                child = Node(state, current, action)
                child.g = current.g + 1  
                child.h = self.hFunction(state)
                child.f = child.g + child.h

                if child.state not in [node.state for node in self.closed] and child.state not in [node.state for node in self.open]:
                    self.open.append(child)
                    
                else:
                    existingOpen = None
                    for node in self.open:
                        if node.state == child.state and node.f > child.f:
                            existingOpen = node
                            break
                    
                    existingClose = None
                    for node in self.closed:
                        if node.state == child.state and node.f > child.f:
                            existingClose = node
                            break
                        
                    if child.state in [node.state for node in self.open] and existingOpen:
                        self.open.remove(existingOpen)
                        self.open.append(child)
                    elif child.state in [node.state for node in self.closed] and existingClose:
                        self.closed.remove(existingClose)
                        self.open.append(child)
                    
                    
                            
        return None