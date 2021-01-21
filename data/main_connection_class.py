import pygame
import sys
from collections import defaultdict


def fadeout(W, H, screen):
    fade = pygame.Surface((W, H))
    fade.fill((255, 0, 0))
    for alpha in range(0, 254):
        fade.set_alpha(alpha)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(50)


class Game_cycle:

    def __init__(self):
        pygame.init()
        W = 432
        H = 720
        self.game_over = False
        self.screen = pygame.display.set_mode((W, H))

        pygame.display.set_caption('Death or Dishonour')
        pygame.display.set_icon(pygame.image.load('resources/images/test_small_logo_1.bmp'))
        bkgd = pygame.image.load('resources/images/background_3.jpeg').convert()
        bkgd_y = 0
        x_pos = 0
        v = 20  # пикселей в секунду
        FPS = 120
        clock = pygame.time.Clock()

        while not self.game_over:  # пока пользователь не закрыл окно или не совершил необходимиое действие в игре
            # цикл продолжается
            for event in pygame.event.get():  # в этом цикле мы принимаем сообщения, отправленные другими классами
                # вроде menu или player
                if event.type == pygame.QUIT:  # если пользователь закроет программу, игра завершится
                    fadeout(W, H, self.screen)
                    self.game_over = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            rel_y = bkgd_y % bkgd.get_rect().height  # вспомогательная переменная
            self.screen.blit(bkgd, (0, rel_y - bkgd.get_rect().height))  # установка движущегося фона
            if rel_y < H:
                self.screen.blit(bkgd, (0, rel_y))
            bkgd_y += 1
            pygame.display.update()
            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()


Game_cycle()
