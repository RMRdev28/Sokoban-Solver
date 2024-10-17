class SokobanPuzzle:
  def __init__(self, level_file):
      self.width = 0
      self.height = 0
      self.obstacles = set()
      self.goals = set()
      self.boxes = set()
      self.player = None
      self.load_level(level_file)

  def load_level(self, level_file):
      with open(level_file, 'r') as f:
          lines = f.readlines()

      self.height = len(lines)
      self.width = max(len(line.rstrip('\n')) for line in lines)

      for y, line in enumerate(lines):
          for x, char in enumerate(line.rstrip('\n')):
              pos = (x, y)
              if char == 'O':
                  self.obstacles.add(pos)
              elif char == ' ':
                  pass  
              elif char == 'S':
                  self.goals.add(pos)
              elif char == 'B':
                  self.boxes.add(pos)
              elif char == '*':
                  self.boxes.add(pos)
                  self.goals.add(pos)
              elif char == 'R':
                  self.player = pos
              elif char == '.':
                  self.player = pos
                  self.goals.add(pos)
              else:
                  pass  
              
              

