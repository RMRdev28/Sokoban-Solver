class SokobanPuzzle:
    def __init__(self, level_file):
      self.width = 0
      self.level = level_file
      self.height = 0
      self.obstacles = set()
      self.goals = set()
      self.boxes = set()
      self.outSides = set()
      self.player = None
      self.grid = []
      self.deadLockGrid = []
      self.deadLockPositions = set()
      self.rows_with_goals = set()
      self.cols_with_goals = set()
      

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
                elif char == 'T':
                    row.append('T')
                    self.outSides.add(pos)
                else:
                    row.append(' ')  

            self.grid.append(row)
        
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.generateCornerDeadLock()
        self.generateLineDeadLock()
        for i in self.grid:
            print(i)
        print("--------------------")
        for i in self.deadLockGrid:
            print(i)

    
    
    def generateCornerDeadLock(self):
        self.deadLockGrid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
                for x in range(self.width):
                    pos = (x, y)
                    cell = self.grid[y][x]
                    if cell == ' ' or cell == 'R' and pos not in self.goals:
                        if (self.isWallOrObstacle(x - 1, y) and self.isWallOrObstacle(x, y - 1)) or \
                           (self.isWallOrObstacle(x + 1, y) and self.isWallOrObstacle(x, y - 1)) or \
                           (self.isWallOrObstacle(x - 1, y) and self.isWallOrObstacle(x, y + 1)) or \
                           (self.isWallOrObstacle(x + 1, y) and self.isWallOrObstacle(x, y + 1)):
                            self.deadLockGrid[y][x] = 'D'
                            self.deadLockPositions.add(pos)
                            
    
    def generateLineDeadLock(self):
        for y in range(self.height):
            deadLockXPositions = [x for x in range(self.width) if self.deadLockGrid[y][x] == 'D']
            deadLockXPositions.sort()
            for i in range(len(deadLockXPositions) - 1):
                x1 = deadLockXPositions[i]
                x2 = deadLockXPositions[i + 1]
                isWallTop = all(self.isWallOrObstacle(x, y - 1) for x in range(x1 + 1, x2))
                isWallBottom = all(self.isWallOrObstacle(x, y + 1) for x in range(x1 + 1, x2))
                if isWallTop or isWallBottom:
                    for x in range(x1 + 1, x2):
                        pos = (x, y)
                        if self.grid[y][x] == ' ' and pos not in self.goals:
                            self.deadLockGrid[y][x] = 'D'
                            self.deadLockPositions.add(pos)

        for x in range(self.width):
            deadLockYPositions = [y for y in range(self.height) if self.deadLockGrid[y][x] == 'D']
            deadLockYPositions.sort()
            for i in range(len(deadLockYPositions) - 1):
                y1 = deadLockYPositions[i]
                y2 = deadLockYPositions[i + 1]
                isWallLeft = all(self.isWallOrObstacle(x - 1, y) for y in range(y1 + 1, y2))
                isWallRight = all(self.isWallOrObstacle(x + 1, y) for y in range(y1 + 1, y2))
                if isWallLeft or isWallRight:
                    for y in range(y1 + 1, y2):
                        pos = (x, y)
                        if self.grid[y][x] == ' ' and pos not in self.goals:
                            self.deadLockGrid[y][x] = 'D'
                            self.deadLockPositions.add(pos)
                            
                            
    

    def checkIfBoxeIsDeadLock(self):
        return any(box in self.deadLockPositions for box in self.boxes)   
                
    def isWallOrObstacle(self, x, y):
        pos = (x, y)
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return True 
        if pos in self.obstacles:
            return True
        if self.grid[y][x] == 'O':
            return True
        return False
    
 
    def isGoal(self):
        return self.boxes == self.goals
    
    
    def deepCopy(self):
        state = SokobanPuzzle(self.level) 
        state.width = self.width
        state.height = self.height
        state.deadLockGrid = self.deadLockGrid
        state.deadLockPositions = self.deadLockPositions.copy()
        state.grid = [row[:] for row in self.grid]
        state.obstacles = self.obstacles.copy()
        state.outSides = self.outSides.copy()
        state.goals = self.goals.copy()
        state.boxes = self.boxes.copy()
        state.player = self.player
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
            px, py = self.player
            nextPx = px + dx
            nextPy = py + dy
            
            if 0 <= nextPy < len(self.grid) and 0 <= nextPx < len(self.grid[0]):
                nextCell = self.grid[nextPy][nextPx] 
                
                if nextCell == ' ' or nextCell == 'S':
                    successorState = self.deepCopy()
                    successorState.movePlayer((nextPx, nextPy))
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
        oldX, oldY = self.player 
        newX, newY = direction 
        
        if self.grid[oldY][oldX] == 'R':
            self.grid[oldY][oldX] = ' '
        elif self.grid[oldY][oldX] == '.':
            self.grid[oldY][oldX] = 'S'
        
        if self.grid[newY][newX] == ' ':
            self.grid[newY][newX] = 'R'
        elif self.grid[newY][newX] == 'S':
            self.grid[newY][newX] = '.'
            
        self.player = direction

    def moveBox(self, playerDirection, boxDirection):
        oldX, oldY = playerDirection 
        newX, newY = boxDirection    
        self.movePlayer(playerDirection)

        if (oldX, oldY) in self.boxes:
            self.boxes.remove((oldX, oldY))
        if self.grid[oldY][oldX] == 'B':  
            self.grid[oldY][oldX] = ' '
        elif self.grid[oldY][oldX] == '*':
            self.grid[oldY][oldX] = 'S'
        
        if self.grid[newY][newX] == ' ':
            self.grid[newY][newX] = 'B'
        elif self.grid[newY][newX] == 'S':
            self.grid[newY][newX] = '*'
        
        self.boxes.add(boxDirection)