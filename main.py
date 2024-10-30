

import pygame
from game.sokobanPuzzle import SokobanPuzzle
from game.visualizer import Visualizer
from algorithms.bfs import Bfs
from algorithms.astar import AStar
import time
import sys


def main():
  fileName = "levels/level"
  extension = ".txt"

  if len(sys.argv) > 2:
      if sys.argv[1].isdigit():
          fileName += sys.argv[1] + extension
          board = SokobanPuzzle(fileName)
          board.load_level()
      else:
          print("Invalid level number")
          sys.exit()

      if sys.argv[2] == "bfs":
          bfs = Bfs(board)
          path = bfs.bfsSearch()
      elif sys.argv[2] == "a*":
          astar = AStar(board)
      else:
          print("Invalid algorithm")
          sys.exit()

      if len(sys.argv) > 3 and sys.argv[2] == "a*":
          if sys.argv[3] == "h1":
              astar.hFunction = astar.h1
              path = astar.aStarSearch()
          elif sys.argv[3] == "h2":
              astar.hFunction = astar.h2
              path = astar.aStarSearch()
          elif sys.argv[3] == "h3":
              astar.hFunction = astar.h3
              path = astar.aStarSearch()
          else:
              print("Invalid heuristic function")
              sys.exit()
  else:
      print("Invalid arguments")
      sys.exit()
  
  
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
