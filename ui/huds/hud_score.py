import pygame

class ScoreHUD(pygame.sprite.Sprite):

    def __init__(self, score):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.score = score
        self.font = pygame.font.SysFont('monospace', 24)
        self.scoring = f"Score: {self.score.current_score}"
        self.player_lifes = f"Lifes: {self.score.player_lifes}"

    def draw(self, screen):
        scoring_text_surface = self.font.render(self.scoring, True, (0, 0, 0))
        scoring_text_rect = scoring_text_surface.get_rect()
        scoring_text_rect.topleft = (50, 50)
        screen.blit(scoring_text_surface, scoring_text_rect)

        player_lifes_text_surface = self.font.render(self.player_lifes, True, (0, 0, 0))
        player_lifes_text_rect = player_lifes_text_surface.get_rect()
        player_lifes_text_rect.topleft = (50, 75)
        screen.blit(player_lifes_text_surface, player_lifes_text_rect)

    def update(self, dt):
        self.scoring = f"Score: {self.score.current_score}"
        self.player_lifes = f"Lifes: {self.score.player_lifes}"
