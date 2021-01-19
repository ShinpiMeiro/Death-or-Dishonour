import pygame
import sys


def print_text(massage, x, y, font_cl=(0, 0, 0), font_type=None, font_size=15):
    font = pygame.font.Font(font_type, font_size)
    text = font.render(massage, True, font_cl)
    display.blit(text, (x, y))
    # функция по заданным параметрам превращает нужный текст в картинку, позволяя pygame её отобразить на плоскости


class Button:
    # класс позволяет создавать кнопки с нужными параметрами
    def __init__(self, width, height, inactive_cl, active_cl, pressed_cl):
        self.width = width
        self.height = height
        self.inactive_cl = inactive_cl
        self.active_cl = active_cl
        self.pressed_cl = pressed_cl

    def create_bt(self, x, y, text, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # создаем переменные проверки позиции курсора и нажатия кнопок мыши
        print_text(text, x + 4, y + 5)
        # отрисовываем на кнопке текст

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(display, self.active_cl, (x, y, self.width, self.height))
            # если курсор находится в области кнопки

            if click[0] == 1 and action is not None:
                pygame.draw.rect(display, self.pressed_cl, (x, y, self.width, self.height))
                # если была нажата левая кнопка мыши

                while click[0] == 1:
                    # пока нажата левая кнопка мыши мы ждем, дабы не проигрывать звук кнопки множество раз
                    # и не вызывать нужное действие
                    pass

                # play_bt_pressed_sound
                action()
                # выполняем заданное действие

        else:
            pygame.draw.rect(display, self.inactive_cl, (x, y, self.width, self.height))
        # при любом условии, мы отрисовываем кнопку с нужным текстом. однако всегда разного цвета
        # в зависимости от условия


class Menu:
    pass
