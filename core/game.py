import sys

import pygame

from .constants import (SCREEN_WIDTH, SCREEN_HEIGHT, FPS, MILLISECONDS)
from .state import GameState

from player import Player
from asteroid import Asteroid
from asteroid_field import AsteroidField
from bullet import Bullet
from score import Score

class Game:

    def __init__(self):
        self.running = True
        self.state = GameState.PLAYING
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        print("Starting Asteroids...")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")

        # Create groups
        self.drawable = pygame.sprite.Group()
        self.updatable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        # Assign groups
        Player.containers = (self.drawable, self.updatable)
        Asteroid.containers = (self.drawable, self.updatable, self.asteroids)
        AsteroidField.containers = (self.updatable)
        Bullet.containers = (self.drawable, self.updatable, self.bullets)
        Score.containers = (self.drawable)

        self.player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.score = Score()
        self.score.update_lifes(self.player.lifes)
        AsteroidField()

    def run(self):
        while(self.running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            self.screen.fill("white")

            for thing in self.drawable:
                thing.draw(self.screen)
            self.updatable.update(self.dt)
            for asteroid in self.asteroids:
                if self.player.collision(asteroid):
                    self.score.update_lifes(self.player.lifes)
                    if self.player.hit() == 0:
                        print("Game Over!")
                        sys.exit()
                for bullet in self.bullets:
                    if bullet.collision(asteroid):
                        self.score.update(asteroid)
                        asteroid.split()
                        bullet.kill()

            pygame.display.flip()

            self.dt = self.clock.tick(FPS) / MILLISECONDS