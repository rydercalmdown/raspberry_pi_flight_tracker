import pygame


class BaseStationSprite(pygame.sprite.Sprite):
    """Visual representation of a base station"""

    def __init__(self, rgb, text='Home'):
        super(BaseStationSprite, self).__init__()
        self.rgb = rgb
        self.text = text
        self.create_point_surface()
        self.create_text_surface()

    def create_point_surface(self):
        """Creates a point"""
        container_height = 6
        container_width = 6
        radius = 3
        self.point_surface = pygame.Surface((container_height, container_width))
        pygame.draw.circle(self.point_surface, self.rgb, (container_height//2, container_width//2), radius)

    def create_text_surface(self):
        """Populates text for sprite"""
        font = pygame.font.SysFont('helvetica', 20)
        anti_aliasing = True
        self.text_surface = font.render(self.text, anti_aliasing, (255, 255, 255))
