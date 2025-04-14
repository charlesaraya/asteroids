import pygame

class Menu:

    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.SysFont('monospace', 32)
        self.options_font = pygame.font.SysFont('monospace', 24)
        self.offset = 50
        screen_width, screen_height = self.screen.get_size()
        self.screen_center_width, self.screen_center_height = screen_width // 2, screen_height // 2

    def draw_main_menu(self):
        self.screen.fill("white")

        menu_title = "Main Menu"
        menu_title_text_surface = self.title_font.render(menu_title, True, (0, 0, 0))
        menu_title_text_rect = menu_title_text_surface.get_rect()
        menu_title_text_rect.center = (self.screen_center_width, self.screen_center_height)
        self.screen.blit(menu_title_text_surface, menu_title_text_rect)

        menu_option = "Start New Game [Space bar]"
        menu_option_text_surface = self.options_font.render(menu_option, True, (0, 0, 0))
        menu_option_text_rect = menu_option_text_surface.get_rect()
        menu_option_text_rect.center = (self.screen_center_width, self.screen_center_height + self.offset)
        self.screen.blit(menu_option_text_surface, menu_option_text_rect)

    def draw_game_over_menu(self):
        menu_title = "Game Over"
        menu_title_text_surface = self.title_font.render(menu_title, True, (0, 0, 0))
        menu_title_text_rect = menu_title_text_surface.get_rect()
        menu_title_text_rect.center = (self.screen_center_width, self.screen_center_height)
        self.screen.blit(menu_title_text_surface, menu_title_text_rect)

        menu_start_game = "Start New Game [Space bar]"
        menu_start_game_text_surface = self.options_font.render(menu_start_game, True, (0, 0, 0))
        menu_start_game_text_rect = menu_start_game_text_surface.get_rect()
        menu_start_game_text_rect.center = (self.screen_center_width, self.screen_center_height + self.offset)
        self.screen.blit(menu_start_game_text_surface, menu_start_game_text_rect)

        menu_quit_game = "Quit [Escape]"
        menu_quit_game_text_surface = self.options_font.render(menu_quit_game, True, (0, 0, 0))
        menu_quit_game_text_rect = menu_quit_game_text_surface.get_rect()
        menu_quit_game_text_rect.center = (self.screen_center_width, self.screen_center_height + self.offset * 2)
        self.screen.blit(menu_quit_game_text_surface, menu_quit_game_text_rect)