import pygame
from data.main_connection_class import Game_cycle
from data.tools_class import Tools
import sys


class Button(Game_cycle, Tools):
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
        self.print_text(text, x + 4, y + 5)
        # отрисовываем на кнопке текст

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(self.screen, self.active_cl, (x, y, self.width, self.height))
            # если курсор находится в области кнопки

            if click[0] == 1 and action is not None:
                pygame.draw.rect(self.screen, self.pressed_cl, (x, y, self.width, self.height))

                while click[0] == 1:
                    # пока нажата левая кнопка мыши мы ждем, дабы не проигрывать звук кнопки множество раз
                    # и не вызывать нужное действие
                    pass

                self.play_sound('resources/sounds/click_sound.mp3', 0.5)  # проигрывание звука кнопки
                action()
                # выполняем заданное действие

        else:
            pygame.draw.rect(self.screen, self.inactive_cl, (x, y, self.width, self.height))
        # при любом условии, мы отрисовываем кнопку с нужным текстом. однако всегда разного цвета
        # в зависимости от условия


class Menu:
    pass
    # меню программы, а также её мини-меню
