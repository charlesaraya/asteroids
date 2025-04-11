from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
import pygame

class Player(CircleShape):

    def __init__(self, x, y, radius = PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return a, b, c

    def draw(self, screen, show_hitbox=False):
        if show_hitbox:
            pygame.draw.circle(screen, "red", self.position, self.radius, 2)
        return pygame.draw.polygon(screen, "black", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        return keys

    def move(self, dt):
        self.position += pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED * dt