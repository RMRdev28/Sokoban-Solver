# visualizer.py

import pygame

class Visualizer:
  TILE_SIZE = 64

  def __init__(self, board):
      self.board = board
      self.width = board.width * self.TILE_SIZE
      self.height = board.height * self.TILE_SIZE
      self.screen = pygame.display.set_mode((self.width, self.height))
      pygame.display.set_caption("Sokoban")
      self.load_assets()

  def load_assets(self):
     
      self.floorImg = pygame.image.load('assets/ground.png').convert()
      self.floorImg = pygame.transform.scale(self.floorImg, (self.TILE_SIZE, self.TILE_SIZE))
      self.wallImg = pygame.image.load('assets/obstacle.png').convert()
      self.wallImg = pygame.transform.scale(self.wallImg, (self.TILE_SIZE, self.TILE_SIZE))
      self.boxImg = pygame.image.load('assets/box.png').convert_alpha()
      self.boxImg = pygame.transform.scale(self.boxImg, (self.TILE_SIZE, self.TILE_SIZE))
      self.targetImg = pygame.image.load('assets/goal.png').convert_alpha()
      self.targetImg = pygame.transform.scale(self.targetImg, (self.TILE_SIZE, self.TILE_SIZE))
      self.playerImg = pygame.image.load('assets/player.png').convert_alpha()
      self.playerImg = pygame.transform.scale(self.playerImg, (self.TILE_SIZE, self.TILE_SIZE))
      self.boxOnTargetImg = pygame.image.load('assets/box_target.png').convert_alpha()
      self.boxOnTargetImg = pygame.transform.scale(self.boxOnTargetImg, (self.TILE_SIZE, self.TILE_SIZE))
      self.outside = pygame.image.load('assets/outside.png').convert_alpha()
      self.outside = pygame.transform.scale(self.outside, (self.TILE_SIZE, self.TILE_SIZE))

  def update(self):
    for y in range(self.board.height):
        for x in range(self.board.width):
            pos = (x, y)
            rect = pygame.Rect(x * self.TILE_SIZE, y * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE)
            
            if pos in self.board.obstacles:
                self.screen.blit(self.wallImg, rect)
            elif pos in self.board.outSides:
                    self.screen.blit(self.outside, rect)
            else:
                self.screen.blit(self.floorImg, rect)
                if pos in self.board.goals:
                    self.screen.blit(self.targetImg, rect)
                if pos in self.board.boxes:
                    if pos in self.board.goals:
                        self.screen.blit(self.boxOnTargetImg, rect)
                    else:
                        self.screen.blit(self.boxImg, rect)
                if pos == self.board.player:
                    self.screen.blit(self.playerImg, rect)

    pygame.display.flip()