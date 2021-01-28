import pygame
import sys
from data.player_class import Player
from data.explosion_class import Explosion
from data.objects_class import Bullets
from data.enemy_class import Enemy


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
width = 600
height = 800
FPS = 100
menu = True
screen = pygame.display.set_mode((width, height))
speed = 2
font = pygame.font.SysFont(None, 20)
clock = pygame.time.Clock()
# заголовок окна
pygame.display.set_caption('Death or Dishonour')
# иконка приложения
pygame.display.set_icon(pygame.image.load('resources/images/test_small_logo_1.bmp'))


def draw_text(text, font, color, surface, x, y):
    text_object = font.render(text, 1, color)
    textrect = text_object.get_rect()
    textrect.topleft = (x, y)
    surface.blit(text_object, textrect)


def main_menu():
    menu_music = pygame.mixer.Sound('resources/sounds/music/wagner_main_theme.mp3')
    menu_music.set_volume(0.2)
    menu_music.play()
    while True:
        mx, my = pygame.mouse.get_pos()
        screen.fill((0, 0, 0))
        draw_text('Death or Dishonour', font, (255, 255, 255), screen, 20, 20)
        button_play = pygame.Rect(50, 100, 200, 50)
        button_options = pygame.Rect(50, 200, 200, 50)
        button_exit = pygame.Rect(50, 300, 200, 50)
        if button_play.collidepoint((mx, my)):
            if click:
                menu_music.stop()
                game_screen()
        if button_options.collidepoint((mx, my)):
            if click:
                options_menu()
        if button_exit.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, (0, 0, 255), button_play)
        pygame.draw.rect(screen, (0, 0, 255), button_options)
        pygame.draw.rect(screen, (0, 0, 255), button_exit)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(10)


def options_menu():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('Options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.update()
        clock.tick(10)


def game_screen():
    track_count = 0
    battle_tracks = ['resources/sounds/music/battle_music_1.mp3', 'resources/sounds/music/battle_music_2.mp3',
                     'resources/sounds/music/battle_music_3.mp3', 'resources/sounds/music/battle_music_4.mp3',
                     'resources/sounds/music/battle_music_5.mp3', 'resources/sounds/music/battle_music_6.mp3']
    ingame_music = pygame.mixer.Sound(battle_tracks[track_count])
    ingame_music_sound = 0.2
    ingame_music.set_volume(ingame_music_sound)
    ingame_music.play()
    running = True
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    enemies = pygame.sprite.Group()
    p = Player()
    bullets_count = pygame.sprite.Group()
    booms = pygame.sprite.Group()
    level_bckgd_pos = -16000
    current_player_sprite = 'stay'
    current_level_background = pygame.image.load('resources/level_pictures/first_level_bckgd.jpg')
    while running:
        #  ---------------------------------------- управление
        for event in pygame.event.get():  # в этом цикле мы принимаем сообщения, отправленные другими классами

            if event.type == pygame.KEYDOWN and event.key == pygame.K_EQUALS:
                ingame_music.stop()
                track_count += 1
                if track_count > 5:
                    track_count = 0
                ingame_music = pygame.mixer.Sound(battle_tracks[track_count])
                ingame_music.set_volume(ingame_music_sound)
                ingame_music.play()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_PLUS:
                ingame_music_sound += 0.05
                if ingame_music_sound >= 1.5:
                    ingame_music_sound = 1.4
                ingame_music.set_volume(ingame_music_sound)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_MINUS:
                ingame_music_sound -= 0.05
                if ingame_music_sound < 0:
                    ingame_music_sound = 0
                ingame_music.set_volume(ingame_music_sound)

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
                p.moving_down = False
                p.moving_up = True

            elif event.type == pygame.KEYDOWN and (
                    event.key == pygame.K_s or event.key == pygame.K_DOWN) and not p.moving_up:
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

            # просчет выстрела
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                Bullets(bullets_count).shot((p.x + 21, p.y - 25))
                Bullets(bullets_count).shot((p.x + 76, p.y - 25))
                Bullets.shooting = True

            # просчет выстрела, но для пробела
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                print('+')
                Bullets(bullets_count).shot((p.x + 21, p.y - 25))
                Bullets(bullets_count).shot((p.x + 76, p.y - 25))
                Bullets.shooting = True

            # спавн врагов
            if event.type == pygame.USEREVENT:
                Enemy(enemies)
            # если пользователь закроет программу, игра завершится
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
        # передвижение заднего фона
        level_bckgd_pos += 2
        if level_bckgd_pos >= 0:
            screen.fill((0, 0, 0))
        screen.blit(current_level_background, (0, level_bckgd_pos))
        # передвижение игрока
        p.update(FPS)
        # передвижение врагов
        enemies.update(FPS)
        # отрисовка врагов
        enemies.draw(screen)
        # передвижение пули
        bullets_count.update()
        bullets_count.draw(screen)
        # смена текстур игрока
        if current_player_sprite == 'left':
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

        # проверка коллизии врага и игрока
        collision = pygame.sprite.spritecollide(p, enemies, True)
        if collision:
            play_sound('resources/sounds/explosion_stun.mp3', 0.05)

        for hit in pygame.sprite.groupcollide(bullets_count, enemies, True, True):
            play_sound('resources/sounds/explosion_sound.mp3', 0.15)

        # взрыв на месте убитого врага
        booms.update()
        booms.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main_menu()

    pygame.quit()
