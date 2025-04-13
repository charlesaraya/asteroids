import pygame

from asteroid import Asteroid

from constants import ASTEROID_KINDS, ASTEROID_BASE_SCORE

class Score(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.font = pygame.font.SysFont('monospace', 24)
        self.current_score = 0
        self.text = 'Score: 0'

    def draw(self, screen, show_hitbox=False):
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.topleft = (50, 50)
        return screen.blit(text_surface, text_rect)

    def update(self, thing):
        score = 0
        if isinstance(thing, Asteroid):
            score = (ASTEROID_KINDS - thing.kind + 1) * ASTEROID_BASE_SCORE

        self.current_score += score
        self.text = f"Score: {self.current_score}"