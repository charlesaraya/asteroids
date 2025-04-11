import pygame
from constants import *
from player import Player

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
    # Assign groups
    Player.containers = (drawable, updatable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("white")

        for thing in drawable:
            thing.draw(screen)
        updatable.update(dt)

        pygame.display.flip()

        dt = clock.tick(FPS) / MILLISECONDS

if __name__ == "__main__":
    main()