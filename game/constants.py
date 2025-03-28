import pygame
import random

PACKAGE_NAME = "MySnakeGame"
AUTHOR = "Lior"
VERSION = "alpha"

SCREEN_DIMENSIONS = (800, 600)
SCREEN_CENTER = (SCREEN_DIMENSIONS[0] / 2, SCREEN_DIMENSIONS[1] / 2)

SQUARE_CENTER_DIMENSIONS = (SCREEN_CENTER[0] - 20, SCREEN_CENTER[1] - 20, 40, 40)

COLOR_RED = (255, 0, 0)
COLOR_GREEN = (60, 179, 113)
COLOR_YELLOW = (255, 165, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_PINK = (238, 130, 238)
COLOR_PURPLE = (106, 90, 205)
COLOR_GRAY_DARK = (60, 60, 60)
COLOR_GRAY_LIGHT = (210, 210, 210)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

SNAKE_SPEED = 3

FRAMERATE = 30

GRID_CELL_SIZE = 10

DEBUG_FRAMERATE = False

# a base for importing from, for ease of access.