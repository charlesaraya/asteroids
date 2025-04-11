import pygame

from circleshape import CircleShape
from bullet import Bullet
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOTING_SPEED,
    PLAYER_RELOAD_RATE,
)

class Player(CircleShape):

    def __init__(self, x, y, radius = PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.reload_timer = PLAYER_RELOAD_RATE

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
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

        self.reload_timer += dt

        return keys

    def move(self, dt):
        self.position += pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.reload_timer >= PLAYER_RELOAD_RATE:
            self.reload_timer = 0
            bullet_speed = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOTING_SPEED
            Bullet(self.position.x, self.position.y, bullet_speed)