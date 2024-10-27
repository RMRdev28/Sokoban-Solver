class SokobanPuzzle:
    def __init__(self, level_file):
      self.width = 5
      self.level = level_file
      self.height = 5
      self.obstacles = set()
      self.goals = set()
      self.boxes = set()
      self.player = None
      self.grid = []
      

    def __eq__(self, other):
        return self.boxes == other.boxes and self.player == other.player and self.grid == other.grid

    def load_level(self):
        with open(self.level, 'r') as f:
            lines = f.readlines()

        self.height = len(lines)
        self.width = max(len(line.rstrip('\n')) for line in lines)

        self.grid = []  

        for y, line in enumerate(lines):
            row = []
            line = line.rstrip('\n')
            for x in range(self.width):
                if x < len(line):
                    char = line[x]
                else:
                    char = ' '  
                pos = (x, y)

                if char == 'O':
                    self.obstacles.add(pos)
                    row.append('O')
                elif char == ' ':
                    row.append(' ')
                elif char == 'S':
                    self.goals.add(pos)
                    row.append('S')
                elif char == 'B':
                    self.boxes.add(pos)
                    row.append('B')
                elif char == '*':
                    self.boxes.add(pos)
                    self.goals.add(pos)
                    row.append('*')
                elif char == 'R':
                    player = pos
                    self.player = player
                    row.append('R')
                elif char == '.':
                    self.player = pos
                    self.goals.add(pos)
                    row.append('.')
                else:
                    row.append(' ')  

            self.grid.append(row)
              
    def isGoal(self):
        print(f"Boxes {self.boxes}")
        print(f"Goals {self.goals}")
        return self.boxes == self.goals
    
    
    def deepCopy(self):
        state = SokobanPuzzle("levels/level.txt") 
        state.grid = [row[:] for row in self.grid]
        state.obstacles = self.obstacles.copy()
        state.goals = self.goals.copy()
        state.boxes = self.boxes.copy()
        state.player = self.player
        print(state.player)
        return state
    
    def successorFunction(self):
        actions = {
            'UP': (0, -1),    
            'RIGHT': (1, 0),
            'LEFT': (-1, 0),
            'DOWN': (0, 1)
        }
        successors = []
        
        for action, (dx, dy) in actions.items():
            px, py = self.player  # Unpack as x,y to match how we stored it
            nextPx = px + dx
            nextPy = py + dy
            
            # Check bounds first
            if 0 <= nextPy < len(self.grid) and 0 <= nextPx < len(self.grid[0]):
                nextCell = self.grid[nextPy][nextPx]  # Grid is accessed [y][x]
                
                if nextCell == ' ' or nextCell == 'S':
                    successorState = self.deepCopy()
                    successorState.movePlayer((nextPx, nextPy))  # Pass (x,y)
                    successors.append((action, successorState))
                    
                elif nextCell == 'B' or nextCell == '*':
                    nextBx = nextPx + dx
                    nextBy = nextPy + dy
                    
                    if (0 <= nextBy < len(self.grid) and 
                        0 <= nextBx < len(self.grid[0])):
                        nextBoxCell = self.grid[nextBy][nextBx]
                        if nextBoxCell == ' ' or nextBoxCell == 'S':
                            successorState = self.deepCopy()
                            successorState.moveBox((nextPx, nextPy), (nextBx, nextBy))
                            successors.append((action, successorState))
        
        return successors

    def movePlayer(self, direction):
        oldX, oldY = self.player  # Unpack as x,y
        newX, newY = direction    # Receive as x,y
        
        if self.grid[oldY][oldX] == 'R':  # Access grid as [y][x]
            self.grid[oldY][oldX] = ' '
        elif self.grid[oldY][oldX] == '.':
            self.grid[oldY][oldX] = 'S'
        
        if self.grid[newY][newX] == ' ':   # Access grid as [y][x]
            self.grid[newY][newX] = 'R'
        elif self.grid[newY][newX] == 'S':
            self.grid[newY][newX] = '.'
            
        self.player = direction

    def moveBox(self, playerDirection, boxDirection):
        oldX, oldY = playerDirection  # Unpack as x,y
        newX, newY = boxDirection    # Receive as x,y
        
        print(f"Before change {self.boxes}")
        self.movePlayer(playerDirection)
        
        # Update box position
        if (oldX, oldY) in self.boxes:
            self.boxes.remove((oldX, oldY))
        if self.grid[oldY][oldX] == 'B':   # Access grid as [y][x]
            self.grid[oldY][oldX] = ' '
        elif self.grid[oldY][oldX] == '*':
            self.grid[oldY][oldX] = 'S'
        
        if self.grid[newY][newX] == ' ':    # Access grid as [y][x]
            self.grid[newY][newX] = 'B'
        elif self.grid[newY][newX] == 'S':
            self.grid[newY][newX] = '*'
        
        self.boxes.add(boxDirection)