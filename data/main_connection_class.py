import pygame
import sys
from collections import defaultdict


class Game_cycle:
    def __init__(self):
        pygame.init()
        self.game_over = False
        self.screen = pygame.display.set_mode((400, 800))
        self.clock = pygame.time.Clock()
        self.background_image = pygame.image.load('data/images/background1.jpg')  # TODO выбрать картинку
        self.frame_rate = 60
        self.game_over = False
        self.objects = []
        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode((400, 800))
        pygame.display.set_caption('Death or Dishonour')
        self.clock = pygame.time.Clock()
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []

    def update(self):
        for o in self.objects:
            o.update()

    def draw(self):
        for o in self.objects:
            o.draw(self.surface)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type in (pygame.MOUSEBUTTONDOWN,
                                pygame.MOUSEBUTTONUP,
                                pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def run(self):
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))
            self.handle_events()  # метод заключает в себя действия которые
            # будут сделаны на этом ходу программы в соотв. с нажатыми кнопками
            self.update()  # обновление objects
            self.draw()  # отрисовка objects
            pygame.display.update()
            self.clock.tick(self.frame_rate)
