import pygame
from main_connection_class import Game_cycle


class Player(Game_cycle):
    def __init__(self):
        self.moving_left = False
        self.moving_right = False
        self.hp = 3
