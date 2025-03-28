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
    food1 = Food(snake) # food initialization - not sure if will be here or in main
    food2 = Food(snake)
    font = pygame.font.Font(None, 36)
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
        if (
            snake.head.position[0] < 0 or
            snake.head.position[0] >= SCREEN_DIMENSIONS[0] or
            snake.head.position[1] < 0 or
            snake.head.position[1] >= SCREEN_DIMENSIONS[1] or
            snake.check_self_collision()
        ):
            print(f"Game Over!\n Score is {snake.score}!")
            running = False

        dx1 = abs(snake.head.position[0] - food1.position[0])
        dy1 = abs(snake.head.position[1] - food1.position[1])
        dx2 = abs(snake.head.position[0] - food2.position[0])
        dy2 = abs(snake.head.position[1] - food2.position[1])
        if dx1 < GRID_CELL_SIZE and dy1 < GRID_CELL_SIZE:
            print("Food eaten!")
            snake.add_segment()
            snake.score += 1
            food1.respawn()
        if dx2 < GRID_CELL_SIZE and dy2 < GRID_CELL_SIZE:
            print("Food eaten!")
            snake.add_segment()
            snake.score += 1
            food2.respawn()
        # --- Draw the frame ---  
        text_surface = font.render(f"Score: {snake.score}", True, (255,255,255))     
        screen.fill((0,0,0)) # screen cleared
        snake.draw_snake(screen) # draw snake
        # draw foods
        food1.draw_food(screen)
        food2.draw_food(screen) 
        # points_text
        screen.blit(text_surface, (10, 10)) #text at top left corner

        pygame.display.flip() # refresh display to make changes visible
        # --- Control the frame rate ---
        framerate_clock.tick(FRAMERATE)