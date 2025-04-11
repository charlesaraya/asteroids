import pygame

from circleshape import CircleShape
from constants import BULLET_RADIUS, PLAYER_SHOOTING_SPEED

class Bullet(CircleShape):

    def __init__(self, x, y, velocity):
        super().__init__(x, y, BULLET_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        return pygame.draw.circle(screen, "black", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt 