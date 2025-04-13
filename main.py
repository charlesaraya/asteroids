import sys

import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroid_field import AsteroidField
from bullet import Bullet
from score import Score

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create groups
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    # Assign groups
    Player.containers = (drawable, updatable)
    Asteroid.containers = (drawable, updatable, asteroids)
    AsteroidField.containers = (updatable)
    Bullet.containers = (drawable, updatable, bullets)
    Score.containers = (drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    score = Score()
    score.update_lifes(player.lifes)
    AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("white")

        for thing in drawable:
            thing.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                score.update_lifes(player.lifes)
                if player.hit() == 0:
                    print("Game Over!")
                    sys.exit()
            for bullet in bullets:
                if bullet.collision(asteroid):
                    score.update(asteroid)
                    asteroid.split()
                    bullet.kill()

        pygame.display.flip()

        dt = clock.tick(FPS) / MILLISECONDS

if __name__ == "__main__":
    main()