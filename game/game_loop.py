# core game-loop logic - snake movements, collision checks, turning mechanics.
from game import pygame, SCREEN_DIMENSIONS, FRAMERATE
from snake import Snake
from food import Food

def game_loop():
    snake = Snake() # will remove later on, snake init will be in main
    food = Food() # food initialization - not sure if will be here or in main
    running = True
    while running:
        # --- Process input ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # key handling:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))
        
        # --- Update snake logic ---
        snake.move()
        # --- Check collision logic if needed ---
        if snake.head.position == food.position:
            food.respawn()
        # --- Draw the frame ---
        screen = pygame.display.set_mode(SCREEN_DIMENSIONS) # will be a var inside main.py, to be removed then
        framerate_clock = pygame.time.Clock() # var inside main.py, will be removed
        
        screen.fill((0,0,0)) # screen cleared
        snake.draw_snake(screen) # draw snake
        # food to be drawn and other objects to be drawn here

        pygame.display.flip() # refresh display to make changes visible
        # --- Control the frame rate ---
        framerate_clock.tick(FRAMERATE)