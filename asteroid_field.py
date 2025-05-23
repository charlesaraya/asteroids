import random

import pygame

from asteroid import Asteroid
from core.constants import (
    ASTEROID_MIN_RADIUS,
    ASTEROID_MAX_RADIUS,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    ASTEROID_SPAWN_RATE,
    ASTEROID_MIN_SPEED,
    ASTEROID_MAX_SPEED,
    ASTEROID_MIN_SPAWN_ANGLE, 
    ASTEROID_MAX_SPAWN_ANGLE,
    ASTEROID_KINDS,
)

class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, position, radius, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0
            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            position = edge[1](random.uniform(0, 1))
            radius = random.randint(1, ASTEROID_KINDS) * ASTEROID_MIN_RADIUS
            speed = random.randint(ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED)
            velocity = edge[0] * speed
            angle = random.randint(ASTEROID_MIN_SPAWN_ANGLE, ASTEROID_MAX_SPAWN_ANGLE)
            velocity = velocity.rotate(angle)
            self.spawn(position, radius, velocity)