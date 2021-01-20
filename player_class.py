import pygame
from main_connection_class import Game_cycle
from tools_class import Tools


class Player(Game_cycle, Tools):
    def __init__(self):
        self.moving_left = False
        self.moving_right = False
        self.pos = (200, 600)
        self.hp = 3
        # Регистрация метода handle() ракетки для обработки событий клавиш

    def draw(self, surface):
        pygame.draw.rect(surface, (110, 150, 110), [self.pos[0], self.pos[1], 40, 10])
