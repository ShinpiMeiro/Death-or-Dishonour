import pygame
from data.player_class import Player
from data.explosion_class import Explosion
from data.objects_class import Objects


def fadeout(W, H, scr):
    fade = pygame.Surface((W, H))
    fade.fill((255, 0, 0))
    for alpha in range(0, 254):
        fade.set_alpha(alpha)
        scr.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(50)


def play_sound(sound_p, volume_h=0.5, wait_t=0):
    pl_sound = pygame.mixer.Sound(sound_p)
    pl_sound.set_volume(volume_h)
    pl_sound.play()
    pygame.time.wait(wait_t)


def print_text(massage, x, y, font_cl=(0, 0, 0), font_type=None, font_size=15):
    font = pygame.font.Font(font_type, font_size)
    text = font.render(massage, True, font_cl)
    return screen.blit(text, (x, y))


pygame.init()
weight = 600
height = 800
FPS = 100

screen = pygame.display.set_mode((weight, height))
speed = 2


def game_screen():
    pygame.init()
    p = Player()
    e = Explosion()
    o = Objects()
    level_bckgd_pos = -4000
    current_player_sprite = 'stay'
    game_over = False
    clock = pygame.time.Clock()
    current_sprite = None
    pygame.mouse.set_visible(False)
    click = pygame.mouse.get_pressed()
    pygame.display.set_caption('Death or Dishonour')  # создание заголовка окна
    pygame.display.set_icon(pygame.image.load('resources/images/test_small_logo_1.bmp'))  # создание иконки приложения
    current_level_background = pygame.image.load('resources/level_pictures/first_level_bckgd.jpg')
    play_sound('resources/sounds/music/wagner_main_theme.mp3', 0.2)

    while not game_over:  # пока пользователь не закрыл окно или не совершил необходимиое действие в игре
        # цикл продолжается
        for event in pygame.event.get():  # в этом цикле мы принимаем сообщения, отправленные другими классами
            if event.type == pygame.KEYDOWN and (
                    event.key == pygame.K_a or event.key == pygame.K_LEFT) and not p.moving_right:
                current_player_sprite = 'left'
                p.moving_right = False
                p.moving_left = True

            elif event.type == pygame.KEYDOWN and (
                    event.key == pygame.K_d or event.key == pygame.K_RIGHT) and not p.moving_left:
                current_player_sprite = 'right'
                p.moving_left = False
                p.moving_right = True

            if event.type == pygame.KEYUP and (event.key == pygame.K_a or event.key == pygame.K_LEFT):
                current_player_sprite = 'stay'
                p.moving_right = False
                p.moving_left = False

            if event.type == pygame.KEYUP and (event.key == pygame.K_d or event.key == pygame.K_RIGHT):
                current_player_sprite = 'stay'
                p.moving_right = False
                p.moving_left = False

            if event.type == pygame.KEYDOWN and (
                    event.key == pygame.K_w or event.key == pygame.K_UP) and not p.moving_down:
                current_player_sprite = 'stay'
                p.moving_down = False
                p.moving_up = True

            elif event.type == pygame.KEYDOWN and (
                    event.key == pygame.K_s or event.key == pygame.K_DOWN) and not p.moving_up:
                current_player_sprite = 'stay'
                p.moving_up = False
                p.moving_down = True

            if event.type == pygame.KEYUP and (event.key == pygame.K_w or event.key == pygame.K_UP):
                current_player_sprite = 'stay'
                p.moving_down = False
                p.moving_up = False

            if event.type == pygame.KEYUP and (event.key == pygame.K_s or event.key == pygame.K_DOWN):
                current_player_sprite = 'stay'
                p.moving_down = False
                p.moving_up = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                current_sprite = 'shot'
                o.shot((p.x + 21, p.y - 25), (p.x + 76, p.y - 25))
                o.shooting = True

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                current_sprite = 'shot'
                o.shot((p.x + 21, p.y - 25), (p.x + 76, p.y - 25))
                o.shooting = True

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                current_sprite = None
                o.shooting = False

            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                current_sprite = None
                o.shooting = False

            if event.type == pygame.QUIT:  # если пользователь закроет программу, игра завершится
                game_over = True
        screen.fill((0, 0, 0))

        level_bckgd_pos += speed  # передвижение заднего фона
        if level_bckgd_pos >= 0:
            level_bckgd_pos = -4000
        screen.blit(current_level_background, (0, level_bckgd_pos))

        p.update(FPS)  # передвижение игрока
        o.bullets(FPS)

        if current_player_sprite == 'left':  # смена текстур игрока
            sprite = p.anim_left()
            screen.blit(sprite, (p.x, p.y))
            p.left_1 = not p.left_1
        elif current_player_sprite == 'right':
            sprite = p.anim_right()
            screen.blit(sprite, (p.x, p.y))
            p.right_1 = not p.right_1
        elif current_player_sprite == 'stay':
            sprite = p.anim_stay()
            screen.blit(sprite, (p.x, p.y))
            p.stay_1 = not p.stay_1

        if current_sprite == 'shot':
            sprite = pygame.transform.scale(pygame.image.load('resources/sprites/bullet.png'), (20, 33))
            screen.blit(sprite, (p.x + 21, p.y - 25))
            sprite = pygame.transform.scale(pygame.image.load('resources/sprites/bullet.png'), (20, 33))
            screen.blit(sprite, (p.x + 76, p.y - 25))

        # screen.blit(e.boom(), (300, 200))
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    game_screen()

    pygame.quit()
