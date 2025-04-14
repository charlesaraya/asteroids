import pygame

from asteroid import Asteroid
from player import Player

from core.constants import ASTEROID_KINDS, ASTEROID_BASE_SCORE

class Score:

    def __init__(self, player):
        self.reset_score(player)

    def reset_score(self, player):
        self.current_score = 0
        self.player_lifes = player.lifes

    def update(self, thing):
        if isinstance(thing, Asteroid):
            self.current_score += (ASTEROID_KINDS - thing.kind + 1) * ASTEROID_BASE_SCORE

        if isinstance(thing, Player):
            self.player_lifes = thing.lifes
