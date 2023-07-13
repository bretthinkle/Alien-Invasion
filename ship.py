import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize ship and its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load ship image and get its rect
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()

        # Start with ship at bottom middle of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flags
        self.moving_right = False
        self.moving_left = False

        # Ship movement speed
        self.x = float(self.rect.x)

    def update(self):
        """Update ship's position based on movement flags"""
        # Move ship based on x
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at a current location"""
        self.screen.blit(self.image, self.rect)
