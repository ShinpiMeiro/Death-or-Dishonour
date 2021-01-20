import pygame
import sys
from collections import defaultdict


class Game_cycle:
    def __init__(self):
        pygame.init()
        self.game_over = False
        self.screen = pygame.display.set_mode((1280, 800))

        pygame.display.set_caption('Death or Dishonour')
        pygame.display.set_icon(pygame.image.load('resources/images/test_small_logo_1.bmp'))

        x_pos = 0
        v = 20  # пикселей в секунду
        clock = pygame.time.Clock()

        while not self.game_over:  # пока пользователь не закрыл окно или не совершил необходимиое действие в игре
            # цикл продолжается

            for event in pygame.event.get():  # в этом цикле мы принимаем сообщения, отправленные другими классами
                # вроде menu или player
                if event.type == pygame.QUIT:  # если пользователь закроет программу, игра завершится
                    self.game_over = True

            self.screen.fill((255, 255, 255))  # заливка экрана

            bg = pygame.image.load("resources/images/test_background_2.png")
            self.screen.blit(bg, (0, 0))  # установка фона

            pygame.draw.circle(self.screen, (255, 0, 0), (int(x_pos), 200), 20)
            x_pos += v * clock.tick() / 1000  # v * t в секундах
            pygame.display.flip()

        pygame.quit()


Game_cycle()
