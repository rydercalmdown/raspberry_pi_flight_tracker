from sprites.BaseStationSprite import BaseStationSprite
import helpers


class BaseStation():
    """Class for representing a base station"""

    def __init__(self, lat, lng, name='Home'):
        self.lat = lat
        self.lng = lng
        self.name = name
        x_coordinate, y_coordinate = helpers.assign_x_y_from_lat_lon(self.lat, self.lng)
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.create_sprite()

    def create_sprite(self):
        """Create the sprite for the aircraft"""
        rgb = (84, 170, 232)
        height = 15
        length = 15
        self.sprite = BaseStationSprite(rgb)

    def draw(self, screen):
        """Draw the aircraft on the screen"""
        x_pixel_buffer = 10
        screen.blit(self.sprite.point_surface, (self.x_coordinate, self.y_coordinate))
        screen.blit(
            self.sprite.text_surface,
            (self.x_coordinate + x_pixel_buffer, self.y_coordinate)
        )
