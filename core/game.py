import sys

import pygame

from .constants import (SCREEN_WIDTH, SCREEN_HEIGHT, FPS, MILLISECONDS)
from .state import GameState

from player import Player
from asteroid import Asteroid
from asteroid_field import AsteroidField
from bullet import Bullet
from score import Score

from ui.menu import Menu

class Game:

    def __init__(self):
        self.running = True
        self.state = GameState.MENU
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.menu = Menu(self.screen)
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

    def start_game(self):
        self.state = GameState.PLAYING
        self.asteroid_field = AsteroidField()
        self.player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.score = Score(self.player)

    def flush_game(self):
        self.asteroid_field.kill()
        self.player.kill()
        self.score.kill()
        for asteroid in self.asteroids:
            asteroid.kill()
        for bullet in self.bullets:
            bullet.kill()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if self.state == GameState.MENU:
                    if event.key == pygame.K_SPACE:
                        self.start_game()
                elif self.state == GameState.GAME_OVER:
                    if event.key == pygame.K_SPACE:
                        self.flush_game()
                        self.start_game()
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False
                elif self.state == GameState.PLAYING:
                    pass

    def render(self):
        self.screen.fill("white")
        if self.state == GameState.MENU:
            self.menu.draw_main_menu()
        elif self.state == GameState.PLAYING:
            for thing in self.drawable:
                thing.draw(self.screen)
        elif self.state == GameState.GAME_OVER:
            self.menu.draw_game_over_menu()
        pygame.display.flip()

    def run(self):
        while self.running:
            # Handle Events
            self._handle_events()

            # Draw
            self.render()

            # Update
            if self.state == GameState.PLAYING:
                self.updatable.update(self.dt)
                for asteroid in self.asteroids:
                    if self.player.collision(asteroid):
                        self.score.update(self.player)
                        if self.player.hit() == 0:
                            self.state = GameState.GAME_OVER
                            print("Game Over!")
                    for bullet in self.bullets:
                        if bullet.collision(asteroid):
                            self.score.update(asteroid)
                            asteroid.split()
                            bullet.kill()

            self.dt = self.clock.tick(FPS) / MILLISECONDS