import os
import pygame


def get_screen_dimensions():
    """Returns dimensions in pixels of the current screen"""
    return (pygame.display.Info().current_h, pygame.display.Info().current_w)


def get_bounding_box_coordinates():
    """Get the lat,lon coordinates of the bounding box"""
    return {
        'lat_max': float(os.environ['LAT_MAX']),
        'lat_min': float(os.environ['LAT_MIN']),
        'lon_max': float(os.environ['LON_MAX']),
        'lon_min': float(os.environ['LON_MIN']),
    }


def assign_x_y_from_lat_lon(lat, lng):
    """Assign x and y coordinates of the sprite from lat and long"""
    screen_height, screen_width = get_screen_dimensions()
    bb_coordinates = get_bounding_box_coordinates()
    lat_percent = (lat - bb_coordinates['lat_min']) / (bb_coordinates['lat_max'] - bb_coordinates['lat_min'])
    lng_percent = (lng - bb_coordinates['lon_min']) / (bb_coordinates['lon_max'] - bb_coordinates['lon_min'])
    x_coordinate = int((1 - lng_percent) * screen_width)
    y_coordinate = int((1 - lat_percent) * screen_height)
    return x_coordinate, y_coordinate
