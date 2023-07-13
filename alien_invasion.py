import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Overall class to manage assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()

        # Initialize settings
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Set background color
        self.bg_color = self.settings.bg_color

        # Initialize settings
        self.ship = Ship(self)

        # Initialize bullets
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Run game by calling methods
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _update_bullets(self):
        """Update position of old bullets and remove old bullets"""

        # Update bullet positions
        self.bullets.update()

        # Delete old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def _check_events(self):
        """Respond to keyboard and mouse input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                # Movement stops
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Move ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            # Fire a bullet
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Right movement stops
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Left movement stops
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
     # Make the most recent screen visible
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
