import pygame
from main_connection_class import Game_cycle


class Tools(Game_cycle):
    # класс создан для удобного использования часто необходимых функций

    def print_text(self, massage, x, y, font_cl=(0, 0, 0), font_type=None, font_size=15):
        font = pygame.font.Font(font_type, font_size)
        text = font.render(massage, True, font_cl)
        self.screen.blit(text, (x, y))
        # функция по заданным параметрам превращает нужный текст в картинку, позволяя pygame её отобразить на плоскости

    def play_sound(self, sound_p, volume_h, wait_t=0):
        pl_sound = pygame.mixer.Sound(sound_p)
        pygame.mixer.music.set_volume(volume_h)
        pl_sound.play()
        pygame.time.wait(wait_t)
        # функция проигрывает звук с заданными параметрами