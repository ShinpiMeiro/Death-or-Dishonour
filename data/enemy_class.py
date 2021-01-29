import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.add(group)
        self.stay1 = pygame.image.load('resources/sprites/enemy_1.png')
        self.stay1 = pygame.transform.scale(self.stay1, (89, 75))
        self.stay2 = pygame.image.load('resources/sprites/enemy_2.png')
        self.stay2 = pygame.transform.scale(self.stay2, (89, 75))
        self.stay_1 = True
        self.image = self.stay1
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, 500)
        self.rect.y = -100
        self.health_count = 2
        self.xvel = 0
        self.yvel = 5
        self.movement = True
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, FPS):
        if self.movement:
            self.movement = not self.movement
            self.rect.x += self.xvel
            if self.rect.y < -100 or self.rect.y > 900:
                self.kill()
            if self.rect.y < 800:
                self.rect.y += self.yvel
            else:
                self.kill()
        else:
            self.movement = not self.movement
