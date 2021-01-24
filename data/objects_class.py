import pygame


def play_sound(sound_p, volume_h=0.5, wait_t=0):
    pl_sound = pygame.mixer.Sound(sound_p)
    pl_sound.set_volume(volume_h)
    pl_sound.play()
    pygame.time.wait(wait_t)


class Bullets(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.first_bullet_pos = [0, 0]
        self.second_bullet_pos = [0, 0]
        self.bullet_speed = 8
        self.shooting = False

    def shot(self, f_bullet_pos, s_bullet_pos, time=0):
        self.first_bullet_pos[0], self.first_bullet_pos[1] = f_bullet_pos[0], f_bullet_pos[1]
        self.second_bullet_pos[0], self.second_bullet_pos[1] = s_bullet_pos[0], s_bullet_pos[1]
        play_sound('resources/sounds/shot_sound.mp3', 0.1)  # проигрывание звука
        pygame.time.wait(time)

    def bullets_update(self, FPS):
        self.first_bullet_pos[1] -= self.bullet_speed
        self.second_bullet_pos[1] -= self.bullet_speed
