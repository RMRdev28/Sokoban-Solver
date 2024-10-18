import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self, position):
        self.position = position
        self.moves = 0
        self.pushes = 0
        
    