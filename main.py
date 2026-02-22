import pygame
import sys

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    # Start the game
    pygame.init()
    pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Time clock
    clock = pygame.time.Clock()
    dt = 0

    # Manage groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add stuff to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)

    # Create an AsteroidField
    AsteroidField()

    # Spawn the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        # Update delta time
        dt = clock.tick(60) / 1000

        # Clear the window
        screen.fill("black")

        # Call the logger
        log_state()

        # Update the update group
        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    # Instead of kill(), use split()
                    asteroid.split()
                    shot.kill()

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # Draw all objects in the drawable group
        for sprite in drawable:
            sprite.draw(screen)

        # Process event queue
        for event in pygame.event.get():
            # Exit the game if window is closed
            if event.type == pygame.QUIT:
                return

        # Present the window
        pygame.display.flip()


if __name__ == "__main__":
    main()
