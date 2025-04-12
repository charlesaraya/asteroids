import random

import pygame

from circleshape import CircleShape
from constants import (
    ASTEROID_MIN_RADIUS,
    ASTEROID_MIN_SPAWN_ANGLE,
    ASTEROID_MAX_SPAWN_ANGLE,
    ASTEROID_SPAWN_SPEED_BOOST,
    ASTEROID_BASE_SCORE,
)

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.kind = self.radius // ASTEROID_MIN_RADIUS
        self.score = self.kind * ASTEROID_BASE_SCORE

    def draw(self, screen):
        return pygame.draw.circle(screen, "black", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.kind == 1:
            self.kill()
            return
        new_kind = self.kind - 1
        new_radius = new_kind * ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        angle = random.uniform(ASTEROID_MIN_SPAWN_ANGLE, ASTEROID_MAX_SPAWN_ANGLE)
        asteroid_one.velocity = self.velocity.rotate(-angle) * ASTEROID_SPAWN_SPEED_BOOST
        asteroid_two.velocity = self.velocity.rotate(angle) * ASTEROID_SPAWN_SPEED_BOOST
        self.kill()