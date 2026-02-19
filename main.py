import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state


def main():
    # Start the game
    pygame.init()
    pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Time clock
    clock = pygame.time.Clock()
    dt = 0

    # Game loop
    while True:
        # Update delta time
        dt = clock.tick(60) / 1000

        # Call the logger
        log_state()

        # Process event queue
        for event in pygame.event.get():
            # Exit the game if window is closed
            if event.type == pygame.QUIT:
                return

        # Create a window
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
