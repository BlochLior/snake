from game import * #this is how i can import directly from game, everything that exists in game directory, and noted here can be accessed.

# game initialization and call for the game loop
def main():
    pygame.init()
    window = pygame.display.set_mode(SCREEN_DIMENSIONS)
    window.fill(COLOR_WHITE)
    pygame.draw.rect(window, COLOR_BLUE, SQUARE_CENTER_DIMENSIONS, 2)
    pygame.display.set_caption("Snake")
    pygame.display.update()
    framerate_clock = pygame.time.Clock()
    running = True
    while running:
        framerate_clock.tick(FRAMERATE)
        if DEBUG_FRAMERATE:
            print(framerate_clock.get_fps())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

main()

# init() -> display.set_mode((800, 600))
# display.set_caption("title window")
# game loop - while..
# .quit()