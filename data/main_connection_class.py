import pygame
import pygame.freetype
import sys
import sqlite3
from data.player_class import Player
from data.explosion_class import Explosion
from data.objects_class import Bullets, Damage
from data.enemy_class import Enemy
from data.death_animation import Explosions
import random


def play_sound(sound_p, volume_h=0.5, wait_t=0):
    pl_sound = pygame.mixer.Sound(sound_p)
    pl_sound.set_volume(volume_h)
    pl_sound.play()
    pygame.time.wait(wait_t)


running_game = True
con = sqlite3.connect('resources/db/leaderbord.db')
cur = con.cursor()
is_sound = True
game_score = 0
line_counter = 0
player_name = ''
pygame.init()
width = 600
height = 800
FPS = 100
menu = True
speed = 2
font = pygame.freetype.Font('resources/sprites/font_main.ttf', 45)
font_table = pygame.freetype.Font('resources/sprites/font_main.ttf', 25)
font_space = pygame.freetype.Font('resources/sprites/space.ttf', 20)
clock = pygame.time.Clock()
# заголовок окна
pygame.display.set_caption('Death or Dishonour')
# иконка приложения
pygame.display.set_icon(pygame.image.load('resources/images/test_small_logo_1.bmp'))
screen = pygame.display.set_mode((600, 800))


def draw_controls():
    pygame.draw.rect(screen, (255, 255, 255), (0, 420, 600, 380), 4)
    pygame.draw.rect(screen, (0, 0, 0, 1), (3, 422, 595, 376))

    draw_text('controls:', font, (255, 255, 255), screen, 20, 430)

    wasd = pygame.image.load('resources/sprites/controls_1.png')
    wasd = pygame.transform.scale(wasd, (243, 100))
    screen.blit(wasd, (20, 450))
    pygame.draw.rect(screen, (255, 255, 255), (20, 626, 130, 25))
    draw_text('SPACE', font_space, (0, 0, 0), screen, 50, 631)
    draw_text(' - movement', font, (255, 255, 255), screen, 270, 502)
    mouse = pygame.image.load('resources/sprites/controls_2.png')
    mouse = pygame.transform.scale(mouse, (90, 100))
    screen.blit(mouse, (153, 570))
    draw_text(' - shoot', font, (255, 255, 255), screen, 270, 620)


def draw_text(text, font_u, color, surface, x, y):
    text_object = font_u.render(text, color)
    textrect = text_object[1]
    textrect.topleft = (x, y)
    surface.blit(text_object[0], textrect)


def main_menu():
    table = []
    click = False
    pygame.mixer.stop()
    menu_music = pygame.mixer.Sound('resources/sounds/music/wagner_main_theme.mp3')
    menu_music.set_volume(0.1)
    menu_music.play()
    while True:
        result = cur.execute("""SELECT * FROM highest_score ORDER BY score DESC LIMIT 7""")
        for elem in result:
            table.append(elem)
        mx, my = pygame.mouse.get_pos()

        background = pygame.image.load('resources/images/menu_background.jpg')
        background = pygame.transform.scale(background, (600, 855))
        screen.blit(background, (0, 0))

        draw_text('Death or Dishonour', font, (255, 255, 255), screen, 50, 20)

        button_play = pygame.image.load('resources/sprites/button.png')
        button_play = pygame.transform.scale(button_play, (222, 105))
        b_play_mask = button_play.get_rect()
        b_play_mask.x = 50
        b_play_mask.y = 70
        screen.blit(button_play, (b_play_mask.x, b_play_mask.y))
        draw_text('play', font, (255, 255, 255), screen, 113, 100)

        button_options = pygame.image.load('resources/sprites/button.png')
        button_options = pygame.transform.scale(button_options, (222, 105))
        b_options_mask = button_options.get_rect()
        b_options_mask.x = 50
        b_options_mask.y = 185
        screen.blit(button_options, (b_options_mask.x, b_options_mask.y))
        draw_text('options', font, (255, 255, 255), screen, 78, 215)

        button_exit = pygame.image.load('resources/sprites/button.png')
        button_exit = pygame.transform.scale(button_exit, (222, 105))
        b_exit_mask = button_exit.get_rect()
        b_exit_mask.x = 50
        b_exit_mask.y = 300
        screen.blit(button_exit, (b_exit_mask.x, b_exit_mask.y))
        draw_text('quit', font, (255, 255, 255), screen, 113, 330)

        pygame.draw.rect(screen, (0, 0, 0), (310, 70, 250, 335))
        pygame.draw.rect(screen, (255, 255, 255), (310, 70, 250, 335), 3)
        pygame.draw.line(screen, (255, 255, 255), (310, 124), (560, 124), 3)
        pygame.draw.line(screen, (255, 255, 255), (435, 124), (435, 405), 3)
        charge = 40
        y = 124
        for i in range(1, 8):
            y += charge
            pygame.draw.line(screen, (255, 255, 255), (310, y), (560, y), 3)
        draw_text('leaderboard', font_table, (255, 255, 255), screen, 362, 80)
        x = 350
        y = 140
        for i in table:
            draw_text(str(i[0]), font_table, (255, 255, 255), screen, x, y)
            draw_text(str(i[1]), font_table, (255, 255, 255), screen, x+100, y)
            y += charge
        table.clear()

        draw_controls()

        if b_play_mask.collidepoint((mx, my)):
            if click:
                menu_music.stop()
                game_screen()
        if b_options_mask.collidepoint((mx, my)):
            if click:
                options_menu()
        if b_exit_mask.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

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
    global player_name, line_counter, is_sound

    running = True
    click = False
    while running:
        mx, my = pygame.mouse.get_pos()

        background = pygame.image.load('resources/images/menu_background.jpg')
        background = pygame.transform.scale(background, (600, 855))
        screen.blit(background, (0, 0))
        draw_text('Options', font, (255, 255, 255), screen, 50, 20)

        button_1 = pygame.image.load('resources/sprites/button.png')
        button_1 = pygame.transform.scale(button_1, (222, 105))
        b_1_mask = button_1.get_rect()
        b_1_mask.x = 50
        b_1_mask.y = 70
        screen.blit(button_1, (b_1_mask.x, b_1_mask.y))
        draw_text(player_name, font, (255, 255, 255), screen, 125, 100)
        if line_counter == 0:
            draw_text('ENTER', font, (255, 0, 0), screen, 280, 90)
            draw_text('NICKNAME', font, (255, 0, 0), screen, 280, 120)

        button_2 = pygame.image.load('resources/sprites/button.png')
        button_2 = pygame.transform.scale(button_2, (222, 105))
        b_2_mask = button_2.get_rect()
        b_2_mask.x = 50
        b_2_mask.y = 185
        screen.blit(button_2, (b_2_mask.x, b_2_mask.y))
        if is_sound:  # TODO плохо работает звук, я пофикшу
            draw_text('on', font, (255, 255, 255), screen, 140, 225)
        else:
            draw_text('off', font, (255, 255, 255), screen, 125, 210)

        button_back = pygame.image.load('resources/sprites/button.png')
        button_back = pygame.transform.scale(button_back, (222, 105))
        b_back_mask = button_back.get_rect()
        b_back_mask.x = 50
        b_back_mask.y = 300
        screen.blit(button_back, (b_back_mask.x, b_back_mask.y))
        draw_text('back', font, (255, 255, 255), screen, 113, 330)

        draw_controls()

        if b_2_mask.collidepoint((mx, my)):
            if click:
                if is_sound:
                    is_sound = not is_sound
                    pygame.mixer.pause()
                else:
                    is_sound = not is_sound
                    pygame.mixer.unpause()
        if b_back_mask.collidepoint((mx, my)):
            if click:
                running = False

        click = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                    if line_counter != 0:
                        line_counter -= 1
                elif event.key == pygame.K_SPACE:
                    pass
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_RETURN:
                    pass
                elif event.key == pygame.K_ESCAPE:
                    running = False
                elif event.mod == pygame.KMOD_NONE and event.key != pygame.K_TAB:
                    if line_counter != 3:
                        line_counter += 1
                        player_name += str(event.unicode).upper()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(10)


def death_screen():
    global running_game
    running = True
    while running:
        screen.fill((0, 0, 0))
        ds = pygame.image.load('resources/sprites/death_sentence.png')
        ds = pygame.transform.rotate(ds, 88)
        ds = pygame.transform.scale(ds, (600, 800))
        screen.blit(ds, (1, 1))
        draw_text('we need smth to show', font, (0, 0, 0), screen, 50, 50)
        draw_text('like', font, (0, 0, 0), screen, 250, 100)
        like = pygame.image.load('resources/images/death_sentence.jpg')
        like = pygame.transform.scale(like, (400, 225))
        screen.blit(like, (100, 150))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                running_game = False
        pygame.display.update()
        clock.tick(10)


def game_screen():
    global game_score, player_name, running_game
    game_score = 0
    if player_name == '':
        player_name = 'NON'
    track_count = 0
    battle_tracks = ['resources/sounds/music/battle_music_1.mp3', 'resources/sounds/music/battle_music_2.mp3',
                     'resources/sounds/music/battle_music_3.mp3', 'resources/sounds/music/battle_music_4.mp3',
                     'resources/sounds/music/battle_music_5.mp3', 'resources/sounds/music/battle_music_6.mp3']
    ingame_music = pygame.mixer.Sound(battle_tracks[track_count])
    ingame_music.stop()
    ingame_music_sound = 0.1
    ingame_music.set_volume(ingame_music_sound)
    ingame_music.play()
    running_game = True
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    enemies = pygame.sprite.Group()
    death = False
    p = Player()
    window_holes = pygame.sprite.Group()
    bullets_count = pygame.sprite.Group()
    booms = pygame.sprite.Group()
    small_booms = pygame.sprite.Group()
    level_bckgd_pos = -16000
    current_player_sprite = 'stay'
    current_level_background = pygame.image.load('resources/level_pictures/first_level_bckgd.jpg')
    screen.blit(current_level_background, (0, 0))
    last = pygame.time.get_ticks()
    cooldown = 300
    while running_game:
        #  ---------------------------------------- управление
        for event in pygame.event.get():  # в этом цикле мы принимаем сообщения, отправленные пользователем

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
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and p.health_count > 0:
                now = pygame.time.get_ticks()
                if now - last >= cooldown:
                    last = now
                    Bullets(bullets_count).shot((p.x + 21, p.y - 25))
                    Bullets(bullets_count).shot((p.x + 76, p.y - 25))
                    Bullets.shooting = True

            # просчет выстрела, но для пробела
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and p.health_count > 0:
                now = pygame.time.get_ticks()
                if now - last >= cooldown:
                    last = now
                    Bullets(bullets_count).shot((p.x + 21, p.y - 25))
                    Bullets(bullets_count).shot((p.x + 76, p.y - 25))
                    Bullets.shooting = True

            # спавн врагов
            if event.type == pygame.USEREVENT and level_bckgd_pos < 0:
                Enemy(enemies)
            if event.type == pygame.USEREVENT and death:
                death_screen()
                while True:
                    if len(str(game_score)) < 6:
                        game_score = '0' + str(game_score)
                    else:
                        break
                var = "INSERT INTO highest_score VALUES ('{}', '{}')".format(player_name, game_score)
                cur.execute(var)
                con.commit()
            # если пользователь закроет программу, игра завершится
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # выход в меню
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running_game = False
                ingame_music.stop()
                while True:
                    if len(str(game_score)) < 6:
                        game_score = '0' + str(game_score)
                    else:
                        break
                var = "INSERT INTO highest_score VALUES ('{}', '{}')".format(player_name, game_score)
                cur.execute(var)
                con.commit()


        # передвижение заднего фона
        level_bckgd_pos += 2
        if level_bckgd_pos >= 0:
            screen.fill((0, 0, 0))
        screen.blit(current_level_background, (0, level_bckgd_pos))
        # передвижение игрока
        if p.health_count > 0:

            # проверка коллизии врага, игрока и пули
            for i in enemies:
                collision = pygame.sprite.collide_rect(p, i)
                if collision:
                    Explosion(booms).boom((i.rect.x, i.rect.y))
                    i.kill()
                    game_score += 10
                    p.health_count -= 1
                    play_sound('resources/sounds/explosion_sound.mp3', 0.01)
                    if p.health_count > 0:
                        Damage(window_holes).taking_damage((random.randint(50, 550), random.randint(50, 750)))
                        play_sound('resources/sounds/explosion_stun.mp3', 0.01)
                for j in bullets_count:
                    collision = pygame.sprite.collide_rect(j, i)
                    if collision:
                        Explosion(booms).boom((i.rect.x, i.rect.y))
                        game_score += 5
                        i.kill()
                        j.kill()
                        play_sound('resources/sounds/explosion_sound.mp3', 0.01)

            p.update(FPS)
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
        else:
            if p.minimize == 0:
                play_sound('resources/sounds/plane_crash.mp3', 0.05)
            p.minimize += 1
            if not death:
                if p.minimize <= 320:
                    p.death()
                    screen.blit(p.death_sp, (p.x, p.y))
                else:
                    death = True
                    Explosions(small_booms).boom((p.rect.x + 3, p.rect.y + 25))
                    Explosions(small_booms).boom((p.rect.x, p.rect.y))
                    Explosions(small_booms).boom((p.rect.x - 22, p.rect.y + 7))
                    p.kill()
        # передвижение врагов
        window_holes.update()
        window_holes.draw(screen)

        enemies.update(FPS)
        # отрисовка врагов
        enemies.draw(screen)
        # передвижение пули
        bullets_count.update()
        bullets_count.draw(screen)

        small_booms.update()
        small_booms.draw(screen)

        # ник игрока
        draw_text('Player: {}'.format(player_name), font, (255, 255, 255), screen, 20, 20)
        # cчет игрока
        if len(str(game_score)) < 2:
            draw_text('00000' + str(game_score), font, (255, 255, 255), screen, 430, 20)
        elif len(str(game_score)) < 3:
            draw_text('0000' + str(game_score), font, (255, 255, 255), screen, 430, 20)
        elif len(str(game_score)) < 4:
            draw_text('000' + str(game_score), font, (255, 255, 255), screen, 430, 20)
        elif len(str(game_score)) < 5:
            draw_text('00' + str(game_score), font, (255, 255, 255), screen, 430, 20)
        elif len(str(game_score)) < 6:
            draw_text('0' + str(game_score), font, (255, 255, 255), screen, 430, 20)
        elif len(str(game_score)) >= 6:
            draw_text("Max score", font, (255, 255, 255), screen, 510, 20)

        # взрыв на месте убитого врага
        booms.update()
        booms.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main_menu()

    pygame.quit()
