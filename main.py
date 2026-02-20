import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    # Start the game
    pygame.init()
    pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Time clock
    clock = pygame.time.Clock()
    dt = 0

    # Spawn the player in the center
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

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

        # Clear the window
        screen.fill("black")

        # Draw the player
        player.draw(screen)

        # Present the window
        pygame.display.flip()


if __name__ == "__main__":
    main()
