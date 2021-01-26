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

    def shot(self, bullet_pos):
        self.rect.x, self.rect.y = bullet_pos[0], bullet_pos[1]
        play_sound('resources/sounds/shot_sound.mp3', 0.1)  # проигрывание звука

    def update(self):
        if self.rect.y < -100 or self.rect.y > 700:
            self.kill()

        if self.rect.y < 800:
            self.rect.y -= self.bullet_speed
        else:
            self.kill()
