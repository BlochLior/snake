from game.constants import * #this is how i can import directly from game, everything that exists in game directory, and noted here can be accessed.
from game.game_loop import game_loop
# game initialization and call for the game loop
def main():
    pygame.init()
    game_loop()
    pygame.quit()

main()

# init() -> display.set_mode((800, 600))
# display.set_caption("title window")
# game loop - while..
# .quit()