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
        self.weight = 600
        self.height = 800
        self.game_over = False
        self.FPS = 120
        self.level_bckgd_pos = -4000
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.weight, self.height))

        pygame.display.set_caption('Death or Dishonour')
        pygame.display.set_icon(pygame.image.load('resources/images/test_small_logo_1.bmp'))

    def level_backgrounds(self, bckgd, speed):  # функция отрисовывающая двигающейся задний фон в уровнях
        self.level_bckgd_pos += speed / self.FPS
        if self.level_bckgd_pos >= 0:
            self.level_bckgd_pos = -4000
        self.screen.blit(bckgd, (0, self.level_bckgd_pos))

    def game_screen(self):
        while not self.game_over:  # пока пользователь не закрыл окно или не совершил необходимиое действие в игре
            # цикл продолжается
            for event in pygame.event.get():  # в этом цикле мы принимаем сообщения, отправленные другими классами
                # вроде menu или player
                if event.type == pygame.QUIT:  # если пользователь закроет программу, игра завершится
                    self.game_over = True
            self.screen.fill((0, 0, 0))

            self.level_backgrounds(pygame.image.load('resources/level_pictures/first_level_bckgd.jpg'), 560)

            if event.type == pygame.MOUSEMOTION:
                self.screen.blit(pygame.image.load('resources/sprites/test_player.png'), event.pos)

            pygame.display.flip()
            self.clock.tick(self.FPS)

        pygame.quit()


Game = Game_cycle()
Game.game_screen()
