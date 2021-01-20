import pygame
class Tools:
    # класс создан для удобного использования часто необходимых функций

    def print_text(self, massage, x, y, font_cl=(0, 0, 0), font_type=None, font_size=15):
        font = pygame.font.Font(font_type, font_size)
        text = font.render(massage, True, font_cl)
        self.screen.blit(text, (x, y))
        # функция по заданным параметрам превращает нужный текст в картинку, позволяя pygame её отобразить на плоскости
