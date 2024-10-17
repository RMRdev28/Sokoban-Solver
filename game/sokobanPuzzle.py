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
                    self.player = pos
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
        pass 
    
    def deepCopy(self):
        state = SokobanPuzzle("levels/level.txt")
        state.grid = [row[:] for row in self.grid]
        state.obstacles = self.obstacles
        state.goals = self.goals
        state.boxes = self.boxes
        state.player = self.player
        return state
        
              
              

