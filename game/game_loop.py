# core game-loop logic - snake movements, collision checks, turning mechanics.
from game.constants import *
from game.snake import Snake
from game.food import Food

def game_loop():
    screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
    screen.fill(COLOR_BLACK)
    pygame.draw.rect(screen, COLOR_BLUE, SQUARE_CENTER_DIMENSIONS, 2)
    pygame.display.set_caption("Snake")
    pygame.display.update()
    framerate_clock = pygame.time.Clock()
    snake = Snake() # will remove later on, snake init will be in main
    food1 = Food() # food initialization - not sure if will be here or in main
    food2 = Food()
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
        if snake.head.position == food1.position:
            food1.respawn()
        elif snake.head.position == food2.position:
            food2.respawn()
        # --- Draw the frame ---       
        screen.fill((0,0,0)) # screen cleared
        snake.draw_snake(screen) # draw snake
        # food to be drawn and other objects to be drawn here

        pygame.display.flip() # refresh display to make changes visible
        # --- Control the frame rate ---
        framerate_clock.tick(FRAMERATE)