# food gen logic - spawning at random locs at the grid once eaten. and startup with x foods.
import random
import pygame
from game.constants import *

class Food(pygame.sprite.Sprite):
    def __init__(self, snake):
        super().__init__()
        self.snake = snake
        self.random_food_position()
        
    def random_food_position(self):
        while True:
            x = random.randrange(0, SCREEN_DIMENSIONS[0], GRID_CELL_SIZE)
            y = random.randrange(0, SCREEN_DIMENSIONS[1], GRID_CELL_SIZE)
            position = (x, y)
            if position not in [segment.position for segment in self.snake.segments]:
                self.position = position
                break


    def draw_food(self, screen):
        pygame.draw.rect(screen, COLOR_RED, pygame.Rect(
                                    self.position[0],
                                    self.position[1],
                                    10,
                                    10)
        )

    def respawn(self):
        self.random_food_position()