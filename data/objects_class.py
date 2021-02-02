import pygame


def play_sound(sound_p, volume_h=0.5, wait_t=0):
    pl_sound = pygame.mixer.Sound(sound_p)
    pl_sound.set_volume(volume_h)
    pl_sound.play()
    pygame.time.wait(wait_t)


class Bullets(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.add(group)
        self.image = pygame.transform.scale(pygame.image.load('resources/sprites/bullet.png'), (20, 33))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.bullet_speed = 8
        self.shooting = False
        self.mask = pygame.mask.from_surface(self.image)

    def shot(self, bullet_pos):
        self.rect.x, self.rect.y = bullet_pos[0], bullet_pos[1]

    def update(self):
        if self.rect.y <= -10 or self.rect.y >= 750:
            self.kill()

        if self.rect.y > -10:
            self.rect.y -= self.bullet_speed
        else:
            self.kill()


class Bossbullets(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.add(group)
        self.image = pygame.transform.scale(pygame.image.load('resources/sprites/boss_bullet.png'), (25, 35))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.bullet_speed = 5
        self.mask = pygame.mask.from_surface(self.image)

    def shot(self, bullet_pos):
        self.rect.x, self.rect.y = bullet_pos[0], bullet_pos[1]

    def update(self):
        if self.rect.y < -10 or self.rect.y > 800:
            self.kill()

        if self.rect.y < 810:
            self.rect.y += self.bullet_speed
        else:
            self.kill()


class Damage(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.add(group)
        self.image = pygame.image.load('resources/sprites/broken_window.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.time = 0
        self.mask = pygame.mask.from_surface(self.image)

    def taking_damage(self, sprite_pos):
        self.rect.x, self.rect.y = sprite_pos[0], sprite_pos[1]

    def update(self):
        if self.time >= 900:
            self.kill()
        elif self.time < 900:
            self.time += 1
