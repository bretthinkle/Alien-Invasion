import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class which represents a single alien in the fleet"""

    def __init__(self, ai_game):
        super.__init()
        self.screen = ai_game

        # Load image of alien and set its rect attribute
        self.image = self.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        # Set location of alien
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store aliens horizontal position
        self.x = float(self.rect.x)