
import pygame
from game.sokobanPuzzle import SokobanPuzzle
from game.visualizer import Visualizer

def main():

  board = SokobanPuzzle("levels/level.txt")
  sucs = board.successorFunction()
  print(sucs)
  
#   print(board.grid)


  pygame.init()
  visualizer = Visualizer(board)


  visualizer.update()
  running = True
  clock = pygame.time.Clock()

  while running:
      
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False


      clock.tick(60)

  pygame.quit()

if __name__ == "__main__":
  main()