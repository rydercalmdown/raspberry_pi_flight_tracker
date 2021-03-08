import os
import time
import pygame
import decoder
from models.Aircraft import Aircraft
from models.BaseStation import BaseStation
from models.AlertMessage import AlertMessage


def get_screen():
    """Returns the screen object"""
    pygame.init()
    pygame.font.init()
    return pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


def draw_my_location(screen):
    """Draws the current user's location"""
    lat = float(os.environ.get('CURRENT_LAT'))
    lng = float(os.environ.get('CURRENT_LON'))
    b = BaseStation(lat, lng)
    b.draw(screen)


def display_aircraft_los(screen):
    """Draws LOS aircraft on screen"""
    a = AlertMessage('LOS - ADS-B Aircraft')
    a.draw(screen)


def run_screen():
    """Runs the screen"""
    screen = get_screen()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                running = False
        screen.fill((0, 0, 0))
        for aircraft_json in decoder.get_aircraft():
            a = Aircraft(aircraft_json)
            a.draw(screen)
        draw_my_location(screen)
        display_aircraft_los(screen)
        pygame.display.flip()
        pygame.time.wait(1000)
