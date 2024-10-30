

import pygame
from game.sokobanPuzzle import SokobanPuzzle
from game.visualizer import Visualizer
from algorithms.bfs import Bfs
from algorithms.astar import AStar
import time

def main():

  board = SokobanPuzzle("levels/level5.txt")
  board.load_level()
  bfs = AStar(board)
  path = bfs.aStarSearch()
  
  
  pygame.init()
  visualizer = Visualizer(board)

  for node in path.getPath():
        board = node.state  
        visualizer.board = board
        visualizer.update()  
        time.sleep(1)
  
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
