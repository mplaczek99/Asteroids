import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position,
                           self.radius, LINE_WIDTH)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return  # This was a small asteroid

        log_event("asteroid_split")

        new_angle = random.uniform(20.0, 50.0)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)

        a1.velocity = self.velocity.rotate(new_angle) * 1.2
        a2.velocity = self.velocity.rotate(-new_angle) * 1.2

        self.kill()

    def update(self, dt):
        self.position += self.velocity * dt
