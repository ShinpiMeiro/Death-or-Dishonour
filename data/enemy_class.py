import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.add(group)

        check = random.randint(1, 20)
        if check <= 6:
            self.stay1 = pygame.image.load('resources/sprites/enemy_2.png')
            self.health_count = 2
        elif 15 >= check > 6:
            self.stay1 = pygame.image.load('resources/sprites/enemy_1.png')
            self.health_count = 3
        elif 15 < check:
            self.stay1 = pygame.image.load('resources/sprites/enemy_3.png')
            self.health_count = 4

        self.stay1 = pygame.transform.scale(self.stay1, (89, 75))
        self.image = self.stay1
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, 500)
        self.rect.y = -100
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


class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.stay1 = pygame.transform.scale(pygame.image.load('resources/sprites/boss_full.png'), (357, 150))
        self.stay2 = pygame.transform.scale(pygame.image.load('resources/sprites/boss_first_damage.png'),
                                            (357, 150))
        self.stay3 = pygame.transform.scale(pygame.image.load('resources/sprites/boss_only_right_side.png'),
                                            (357, 150))
        self.stay4 = pygame.transform.scale(pygame.image.load('resources/sprites/boss_second_damage.png'), (357, 150))
        self.stay5 = pygame.transform.scale(pygame.image.load('resources/sprites/boss_only_gun.png'), (357, 150))
        self.stay6 = pygame.transform.scale(pygame.image.load('resources/sprites/boss_gun_damage.png'), (357, 150))
        self.stay7 = pygame.transform.scale(pygame.image.load('resources/sprites/boss_last_phase.png'),
                                            (357, 150))

        self.body = self.stay1

        self.x = 97
        self.y = -155
        self.xvel = 0
        self.yvel = 0
        self.speed = 0.5

        self.rect = self.stay1.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.health_count = 55
        self.minimize = 0

        self.first_moove = False
        self.second_moove = False
        self.third_moove = False
        self.fourth_moove = False
        self.first_time = True

        self.win = False

    def change_sprite(self):
        if self.health_count >= 45:
            self.body = self.stay1
        if self.health_count < 45:
            self.body = self.stay3
        if self.health_count < 35:
            self.body = self.stay5
        if self.health_count < 20:
            self.body = self.stay7

    def update(self):

        self.yvel, self.xvel = 0, 0

        if not self.win:

            if self.first_time:
                if self.y + self.speed < 70:
                    self.yvel = self.speed
                elif self.y + self.speed >= 70:
                    self.first_time = False
                    self.first_moove = True

            if self.first_moove:
                if self.x + self.speed < 240:
                    self.xvel = self.speed
                elif self.x + self.speed >= 240 and self.y + self.speed >= 600:
                    self.first_moove = False
                    self.second_moove = True

                if self.y + self.speed < 600:
                    self.yvel = self.speed
                elif self.x + self.speed >= 240 and self.y + self.speed >= 600:
                    self.first_moove = False
                    self.second_moove = True

            if self.second_moove:
                if self.x + self.speed > 3:
                    self.xvel = -self.speed
                elif self.x + self.speed <= 3 and self.y + self.speed <= 600:
                    self.second_moove = False
                    self.third_moove = True

                if self.y > 600:
                    self.yvel = self.speed
                elif self.x + self.xvel <= 3 and self.y + self.yvel <= 600:
                    self.second_moove = False
                    self.third_moove = True

            if self.third_moove:
                if self.x + self.speed < 240:
                    self.xvel = self.speed
                elif self.x + self.speed >= 240 and self.y + self.speed >= 500:
                    self.third_moove = False
                    self.fourth_moove = True

                if self.y - self.speed > 3:
                    self.yvel = -self.speed
                elif self.x + self.speed >= 240 and self.y + self.speed >= 3:
                    self.third_moove = False
                    self.fourth_moove = True

            if self.fourth_moove:
                if self.x > 3:
                    self.xvel = -self.speed
                elif self.x - self.speed <= 3 and self.y - self.speed <= 3:
                    self.fourth_moove = False
                    self.first_moove = True

                if self.y > 3:
                    self.yvel = -self.speed
                elif self.x - self.speed <= 3 and self.y - self.speed <= 3:
                    self.fourth_moove = False
                    self.first_moove = True
        else:
            if self.x < 97:
                self.xvel = self.speed
            elif self.x > 97:
                self.xvel = -self.speed

            if self.y < 1000:
                self.yvel = self.speed
            else:
                self.kill()

        self.x += self.xvel
        self.y += self.yvel
        self.rect.x = self.x
        self.rect.y = self.y
