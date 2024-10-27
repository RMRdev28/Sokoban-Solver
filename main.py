

import pygame
from game.sokobanPuzzle import SokobanPuzzle
from game.visualizer import Visualizer
from algorithms.bfs import Bfs
from algorithms.astar import AStar
import time

def main():

  board = SokobanPuzzle("levels/level.txt")
  board.load_level()
  bfs = AStar(board)
  path = bfs.aStarSearch()
  
  
#   print(board.grid)
  pygame.init()
  visualizer = Visualizer(board)

  for node in path.getPath():
        board = node.state  
        # board.load_level()
        print(f"Player position{board.player}") 
        visualizer.board = board
        
        visualizer.update()  
        time.sleep(0.5)
  
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
