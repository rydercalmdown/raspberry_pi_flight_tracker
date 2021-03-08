from sprites.AlertMessageSprite import AlertMessageSprite
import pygame


class AlertMessage():
    """Class for representing a base station"""

    def __init__(self, text='LOS - Aircraft'):
        self.text = text
        screen_height, screen_width = pygame.display.Info().current_h, pygame.display.Info().current_w
        offset = 25
        self.x_coordinate = screen_height + offset
        self.y_coordinate = screen_width + offset
        self.create_sprite()

    def create_sprite(self):
        """Create the sprite for the aircraft"""
        self.sprite = AlertMessageSprite(self.text)

    def draw(self, screen):
        """Draw the aircraft on the screen"""
        screen.blit(
            self.sprite.text_surface,
            (self.x_coordinate, self.y_coordinate)
        )
