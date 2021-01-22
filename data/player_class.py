import pygame
from data.main_connection_class import Game_cycle
from data.tools_class import Tools


class Player(Game_cycle, Tools):
    def __init__(self):
        self.moving_left = False
        self.moving_right = False
        self.pl_position = (200, 600)
        self.health_count = 3
        # Регистрация метода handle() ракетки для обработки событий клавиш - что????

    def draw(self, surface):
        pygame.draw.rect(surface, (110, 150, 110), [self.pos[0], self.pos[1], 40, 10])
