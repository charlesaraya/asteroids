import pygame

from circleshape import CircleShape
from bullet import Bullet
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOTING_SPEED,
    PLAYER_RELOAD_RATE,
    PLAYER_LIFES,
    PLAYER_HIT_TIMER,
    BLINKING_TIMER,
)

class Player(CircleShape):

    def __init__(self, x, y, radius = PLAYER_RADIUS, lifes=PLAYER_LIFES):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.reload_timer = PLAYER_RELOAD_RATE
        self.hit_timer = PLAYER_HIT_TIMER
        self.blinking_timer = BLINKING_TIMER
        self.blink = False
        self.invulnerable = False
        self.lifes = lifes

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return a, b, c

    def draw(self, screen, show_hitbox=False):
        ship_polygon = pygame.draw.polygon(screen, "black", self.triangle(), 2)
        if show_hitbox:
            pygame.draw.circle(screen, "red", self.position, self.radius, 2)

        if self.invulnerable:
            if self.blink:
                ship_polygon = pygame.draw.polygon(screen, "red", self.triangle(), 2)
            else:
                ship_polygon = pygame.draw.polygon(screen, "black", self.triangle(), 2)
        return ship_polygon

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def ticker(self, dt):
        self.reload_timer += dt
        self.hit_timer += dt
        self.blinking_timer += dt

    

    def update(self, dt):

        self.ticker(dt)

        # Set Key bindings
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

        # Invulnerability Period
        if self.hit_timer >= PLAYER_HIT_TIMER:
            self.invulnerable = False
        # Blink while invulnerable
        if self.invulnerable:
            print(self.blink)
            if self.blinking_timer <= BLINKING_TIMER and not self.blink:
                self.blink = True
            elif self.blinking_timer >= BLINKING_TIMER and self.blink:
                self.blink = False
            elif self.blinking_timer >= BLINKING_TIMER * 2:
                self.blinking_timer = 0
        else:
            self.blink = False
        return keys

    def move(self, dt):
        self.position += pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.reload_timer >= PLAYER_RELOAD_RATE:
            self.reload_timer = 0
            bullet_speed = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOTING_SPEED
            Bullet(self.position.x, self.position.y, bullet_speed)

    def hit(self):
        if self.hit_timer >= PLAYER_HIT_TIMER:
            self.hit_timer = 0
            self.invulnerable = True
            self.lifes -= 1
        return self.lifes