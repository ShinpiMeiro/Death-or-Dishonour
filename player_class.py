import pygame
from main_connection_class import Game_cycle


class Player:
    def __init__(self):
        self.moving_left = False
        self.moving_right = False
        self.hp = 3
        # Регистрация метода handle() ракетки для обработки событий клавиш
    def draw(self, surface):
        pygame.draw.rect(surface, (110, 150, 110), self.bounds)