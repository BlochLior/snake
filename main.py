from game import PACKAGE_NAME, pygame #this is how i can import directly from game, everything that exists in game directory, and noted here can be accessed.

# game initialization and call for the game loop
def main():
    print("this is snake game")
    print(PACKAGE_NAME)
    print(pygame.ver)

main()