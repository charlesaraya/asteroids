import pygame

from asteroid import Asteroid

from constants import ASTEROID_KINDS, ASTEROID_BASE_SCORE

class Score(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.font = pygame.font.SysFont('monospace', 24)
        self.current_score = 0
        self.scoring = f"Score: {self.current_score}"
        self.player_lifes = 0

    def draw(self, screen, show_hitbox=False):
        scoring_text_surface = self.font.render(self.scoring, True, (0, 0, 0))
        scoring_text_rect = scoring_text_surface.get_rect()
        scoring_text_rect.topleft = (50, 50)
        screen.blit(scoring_text_surface, scoring_text_rect)

        player_lifes_text_surface = self.font.render(self.player_lifes, True, (0, 0, 0))
        player_lifes_text_rect = player_lifes_text_surface.get_rect()
        player_lifes_text_rect.topleft = (50, 75)
        screen.blit(player_lifes_text_surface, player_lifes_text_rect)

    def update(self, thing):
        score = 0
        if isinstance(thing, Asteroid):
            score = (ASTEROID_KINDS - thing.kind + 1) * ASTEROID_BASE_SCORE

        self.current_score += score
        self.text = f"Score: {self.current_score}"

    def update_lifes(self, lifes):
        self.player_lifes = f"Lifes: {lifes}"
