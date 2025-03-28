# food gen logic - spawning at random locs at the grid once eaten. and startup with x foods.
import random
import pygame
from game.constants import SCREEN_DIMENSIONS, COLOR_RED
from game.snake import Snake

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.random_food_position()
        
    def random_food_position(self):
        x = random.randrange(SCREEN_DIMENSIONS[0])
        y = random.randrange(SCREEN_DIMENSIONS[1])
        position = (x, y)
        # check if snake already in the new position:
        snake = Snake() # placeholder, to be removed
        for i in range(len(snake.segments)):
            if position == snake.segments[i].position:
                self.random_food_position()
            else:
                continue
        self.position = position

    def draw_food(self, screen):
        pygame.draw.circle(screen, COLOR_RED, self.position, 3)

    def respawn(self):
        self.random_food_position()