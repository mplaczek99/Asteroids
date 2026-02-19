import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state


def main():
    # Start the game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        log_state()

        # Process event queue
        for event in pygame.event.get():
            # Exit the game if window is closed
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
