from utils.node import Node
from collections import deque

class AStar:
    def __init__(self, state):
        self.state = state
        self.open = deque()
        self.closed = []
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
        misplaced_cost = 2 * misplaced
        total_min_distances = 0
        
        for box in state.boxes:
            if box not in state.goals: 
                min_distance = float('inf')
                for goal in state.goals:
                    distance = self.manhattan_distance(box, goal)
                    min_distance = min(min_distance, distance)
                total_min_distances += min_distance
        
        return misplaced_cost + total_min_distances
    
    def get_lowest_f_node(self):
        if not self.open:
            return None
        
        lowest_f_node = self.open[0]
        lowest_f = lowest_f_node.f
        
        for node in self.open:
            if node.f < lowest_f:
                lowest_f = node.f
                lowest_f_node = node
                
        self.open.remove(lowest_f_node)
        return lowest_f_node
    
    def aStarSearch(self):
        if self.state.isGoal():
            return self.initNode
        
        self.open.append(self.initNode)
        
        while len(self.open) > 0:
            current = self.get_lowest_f_node()
            self.closed.append(current)
            print(f"Current : {current.state.player}, f={current.f}")

            for action, state in current.state.successorFunction():
                child = Node(state, current, action)
                child.g = current.g + 1  
                child.h = self.h2(state)
                child.f = child.g + child.h

                if child.state not in [node.state for node in self.closed]:
                    
                    existing_open = None
                    for node in self.open:
                        if node.state == child.state:
                            existing_open = node
                            break
                    
                    if existing_open is None: 
                        if child.state.isGoal():
                            return child
                        self.open.append(child)
                    else:  
                        if child.g < existing_open.g: 
                            self.open.remove(existing_open)
                            self.open.append(child)

        return None