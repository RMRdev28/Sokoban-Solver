class SokobanPuzzle:
    def __init__(self, level_file):
      self.width = 0
      self.height = 0
      self.obstacles = set()
      self.goals = set()
      self.boxes = set()
      self.player = None
      self.grid = []
      self.load_level(level_file)

    def load_level(self, level_file):
        with open(level_file, 'r') as f:
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
        pass
    
    
    def successorFunction(self):
        actions = {
            'UP': (-1, 0),
            'DOWN': (1, 0),
            'LEFT': (0, -1),
            'RIGHT': (0, 1)
        }
        successors = []

        for action, (dx, dy) in actions.items():
           
            px, py = self.player
            nextPx = px + dx
            nextPy = py + dy
            nextCell = self.grid[nextPx][nextPy]

            if nextCell == ' ' or nextCell == 'S':
                
                successorState = self.deepCopy()
                nextPosition = (nextPx, nextPy)
                successorState.movePlayer(nextPosition)
                successors.append((action, successorState))
            elif nextCell == 'B' or nextCell == '*':
               
                nextBx = nextPx + dx
                nextBy = nextPy + dy


                nextBoxCell = self.grid[nextBx][nextBy]
                if nextBoxCell == ' ' or nextBoxCell == 'S':
                    successorState = self.copy()
                    playerPosition = (nextPx, nextPy)
                    boxPosition = (nextBx, nextBy)
                    successorState.moveBox(playerPosition,boxPosition)
                    successors.append((action, successorState))
                else:
                    continue  
            else:
                continue  

        return successors
    
    def deepCopy(self):
        state = SokobanPuzzle("levels/level.txt")
        state.grid = [row[:] for row in self.grid]
        state.obstacles = self.obstacles
        state.goals = self.goals
        state.boxes = self.boxes
        state.player = self.player
        return state
    
    
    def movePlayer(self,direction):
        oldX, oldY = self.player
        newX, newY = direction
        if self.grid[oldX][oldY] == 'R':
            self.grid[oldX][oldY] = ' '
        elif self.grid[oldX][oldY] == '.':
            self.grid[oldX][oldY] = 'S'
            
        if self.grid[newX][newY] == ' ':
            self.grid[newX][newY] = 'R'
        elif self.grid[newX][newY] == 'S':
            self.grid[newX][newY] = '.'
            
        self.player = direction
    
    
    def moveBox(self, box, playerDirection,boxDirection):
        oldX, oldY = box
        newX, newY = boxDirection

        self.movePlayer(playerDirection)
        
        if self.grid[oldX][oldY] == 'B':
            self.grid[oldX][oldY] = ' '
        elif self.grid[oldX][oldY] == '*':
            self.grid[oldX][oldY] = 'S'
            
        if self.grid[newX][newY] == ' ':
            self.grid[newX][newY] = 'B'
        elif self.grid[newX][newY] == 'S':
            self.grid[newX][newY] = '*'
            
        self.boxes.remove(box)
        self.boxes.add(boxDirection)
        
              
              

