class Settings:
    """A Class that stores all settings for the game"""

    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.0

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3.0
        self.bullet_height = 15.0
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3