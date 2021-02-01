import pygame
import pygame.freetype
import sys
import sqlite3
from data.player_class import Player
from data.explosion_class import Explosion
from data.objects_class import Bullets, Damage
from data.enemy_class import Enemy
from data.enemy_class import Boss
from data.death_animation import Smallexplosions
from data.explosion_class import Miniexplosion
import random


def draw_text(text, font_u, color, surface, x, y):
    text_object = font_u.render(text, color)
    textrect = text_object[1]
    textrect.topleft = (x, y)
    surface.blit(text_object[0], textrect)


def play_sound(sound_p, volume_h=0.5, wait_t=0):
    pl_sound = pygame.mixer.Sound(sound_p)
    pl_sound.set_volume(volume_h)
    if is_sound:
        pl_sound.play()
        pygame.time.wait(wait_t)


pygame.init()
running_game = True
is_sound = True
menu = True
boss_done = False
game_score = 0
bullets_shot = 0
line_counter = 0
enemy_killed = 0
speed = 2
FPS = 100
width = 600
height = 800
player_name = ''
con = sqlite3.connect('resources/db/leaderboard.db')
font = pygame.freetype.Font('resources/sprites/font_main.ttf', 45)
font_table = pygame.freetype.Font('resources/sprites/font_main.ttf', 25)
font_space = pygame.freetype.Font('resources/sprites/space.ttf', 20)
font_rating = pygame.freetype.Font('resources/sprites/font_main.ttf', 150)
pygame.display.set_icon(pygame.image.load('resources/images/test_small_logo_1.bmp'))
pygame.display.set_caption('Death or Dishonour')
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()
cur = con.cursor()


def draw_controls():
    pygame.draw.rect(screen, (255, 255, 255), (0, 420, 600, 380), 4)
    pygame.draw.rect(screen, (0, 0, 0, 1), (3, 422, 595, 376))

    draw_text('controls:', font, (255, 255, 255), screen, 20, 430)

    wasd = pygame.image.load('resources/sprites/controls_1.png')
    wasd = pygame.transform.scale(wasd, (243, 100))
    screen.blit(wasd, (20, 470))
    pygame.draw.rect(screen, (255, 255, 255), (20, 646, 130, 25))
    draw_text('SPACE', font_space, (0, 0, 0), screen, 50, 651)
    draw_text(' - movement', font, (255, 255, 255), screen, 270, 522)
    mouse = pygame.image.load('resources/sprites/controls_2.png')
    mouse = pygame.transform.scale(mouse, (90, 100))
    screen.blit(mouse, (153, 590))
    draw_text(' - shoot', font, (255, 255, 255), screen, 270, 640)


def draw_leaderboard():
    table = []
    result = cur.execute("""SELECT * FROM highest_score ORDER BY score DESC LIMIT 7""")
    for elem in result:
        table.append(elem)
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
        draw_text(str(i[1]), font_table, (255, 255, 255), screen, x + 100, y)
        y += charge


def main_menu():
    click = False
    pygame.mixer.stop()
    while True:
        mx, my = pygame.mouse.get_pos()
        screen.fill((0, 0, 0))
        # ------------------------------------------ name zone draw
        pygame.draw.rect(screen, (0, 0, 0), (52, 10, 508, 50))
        pygame.draw.rect(screen, (255, 255, 255), (52, 10, 508, 50), 3)
        draw_text('Death or Dishonour', font, (255, 255, 255), screen, 85, 20)
        # ------------------------------------------ play button
        button_play = pygame.image.load('resources/sprites/button.png')
        button_play = pygame.transform.scale(button_play, (222, 105))
        b_play_mask = button_play.get_rect()
        b_play_mask.x = 50
        b_play_mask.y = 70
        screen.blit(button_play, (b_play_mask.x, b_play_mask.y))
        draw_text('play', font, (255, 255, 255), screen, 113, 100)
        # ------------------------------------------ options button
        button_options = pygame.image.load('resources/sprites/button.png')
        button_options = pygame.transform.scale(button_options, (222, 105))
        b_options_mask = button_options.get_rect()
        b_options_mask.x = 50
        b_options_mask.y = 185
        screen.blit(button_options, (b_options_mask.x, b_options_mask.y))
        draw_text('options', font, (255, 255, 255), screen, 78, 215)
        # ------------------------------------------ quit button
        button_exit = pygame.image.load('resources/sprites/button.png')
        button_exit = pygame.transform.scale(button_exit, (222, 105))
        b_exit_mask = button_exit.get_rect()
        b_exit_mask.x = 50
        b_exit_mask.y = 300
        screen.blit(button_exit, (b_exit_mask.x, b_exit_mask.y))
        draw_text('quit', font, (255, 255, 255), screen, 113, 330)
        # ------------------------------------------ draw

        draw_controls()
        draw_leaderboard()
        # ------------------------------------------ collide
        if b_play_mask.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 0, 100), (50, 70, 222, 105), 5)
            if click:
                if is_sound:
                    play_sound('resources/sounds/click_sound.mp3', 0.2)
                game_screen()
        if b_options_mask.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 0, 100), (50, 185, 222, 105), 5)
            if click:
                if is_sound:
                    play_sound('resources/sounds/click_sound.mp3', 0.2)
                options_menu()
        if b_exit_mask.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 0, 100), (50, 300, 222, 105), 5)
            if click:
                if is_sound:
                    play_sound('resources/sounds/click_sound.mp3', 0.2)
                pygame.quit()
                sys.exit()
        # ------------------------------------------ events
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
        # ------------------------------------------ update
        pygame.display.update()
        clock.tick(10)


def options_menu():
    global player_name, line_counter, is_sound
    running = True
    click = False
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill((0, 0, 0))
        # ------------------------------------------ name zone draw
        pygame.draw.rect(screen, (0, 0, 0), (52, 10, 508, 50))
        pygame.draw.rect(screen, (255, 255, 255), (52, 10, 508, 50), 3)
        draw_text('Options', font, (255, 255, 255), screen, 215, 20)
        # ------------------------------------------ button nick
        button_1 = pygame.image.load('resources/sprites/button.png')
        button_1 = pygame.transform.scale(button_1, (222, 105))
        b_1_mask = button_1.get_rect()
        b_1_mask.x = 50
        b_1_mask.y = 70
        screen.blit(button_1, (b_1_mask.x, b_1_mask.y))
        draw_text(player_name, font, (255, 255, 255), screen, 125, 100)
        # ------------------------------------------ button sound
        button_2 = pygame.image.load('resources/sprites/button.png')
        button_2 = pygame.transform.scale(button_2, (222, 105))
        b_2_mask = button_2.get_rect()
        b_2_mask.x = 50
        b_2_mask.y = 185
        screen.blit(button_2, (b_2_mask.x, b_2_mask.y))
        # ------------------------------------------ button back
        button_back = pygame.image.load('resources/sprites/button.png')
        button_back = pygame.transform.scale(button_back, (222, 105))
        b_back_mask = button_back.get_rect()
        b_back_mask.x = 50
        b_back_mask.y = 300
        screen.blit(button_back, (b_back_mask.x, b_back_mask.y))
        draw_text('back', font, (255, 255, 255), screen, 113, 330)
        # ------------------------------------------ draw
        draw_controls()
        draw_text('audio:', font, (255, 255, 255), screen, 60, 195)
        if is_sound:  # TODO плохо работает звук, я пофикшу
            draw_text('on', font, (255, 255, 255), screen, 190, 245)
        else:
            draw_text('off', font, (255, 255, 255), screen, 175, 230)
        if line_counter == 0:
            draw_text('ENTER', font, (255, 0, 0), screen, 280, 90)
            draw_text('NICKNAME', font, (255, 0, 0), screen, 280, 120)
        # ------------------------------------------ collide
        if b_2_mask.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 0, 100), (50, 185, 222, 105), 5)
            if click:
                if is_sound:
                    play_sound('resources/sounds/click_sound.mp3', 0.2)
                if is_sound:
                    is_sound = not is_sound
                    pygame.mixer.pause()
                else:
                    is_sound = not is_sound
                    pygame.mixer.unpause()
        if b_back_mask.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 0, 100), (50, 300, 222, 105), 5)
            if click:
                if is_sound:
                    play_sound('resources/sounds/click_sound.mp3', 0.2)
                running = False
        # ------------------------------------------ events
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
        # ------------------------------------------ update
        pygame.display.update()
        clock.tick(10)


def game_screen():
    global game_score, player_name, running_game, enemy_killed, bullets_shot, boss_done
    game_score = 0
    enemy_killed = 0
    bullets_shot = 0
    boss_done = False
    if player_name == '':
        player_name = 'NON'
    track_count = 0
    battle_tracks = ['resources/sounds/music/battle_music_1.mp3', 'resources/sounds/music/battle_music_2.mp3',
                     'resources/sounds/music/battle_music_3.mp3', 'resources/sounds/music/battle_music_4.mp3',
                     'resources/sounds/music/battle_music_5.mp3', 'resources/sounds/music/battle_music_6.mp3']
    ingame_music = pygame.mixer.Sound(battle_tracks[track_count])
    ingame_music.stop()
    ingame_music_sound = 0.1
    if not is_sound:
        ingame_music_sound = 0
    ingame_music.set_volume(ingame_music_sound)
    ingame_music.play()
    bs = False
    running_game = True
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    enemies = pygame.sprite.Group()
    death = False
    p = Player()
    window_holes = pygame.sprite.Group()
    bullets_count = pygame.sprite.Group()
    booms = pygame.sprite.Group()
    small_booms = pygame.sprite.Group()
    mini_booms = pygame.sprite.Group()
    phase1_score = True
    phase2_score = True
    phase3_score = True
    battle_music = True
    phase4_score = True
    skill_done = False
    col_check = 1
    boss_death = False
    level_bckgd_pos = -16800
    current_player_sprite = 'stay'
    current_level_background = pygame.image.load('resources/level_pictures/first_level_bckgd.jpg')
    screen.blit(current_level_background, (0, 0))
    last = pygame.time.get_ticks()
    cooldown = 100
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
                    if is_sound:
                        play_sound('resources/sounds/shot_sound.mp3', 0.1)
                    Bullets.shooting = True
                    bullets_shot += 2

            # просчет выстрела, но для пробела
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and p.health_count > 0:
                now = pygame.time.get_ticks()
                if now - last >= cooldown:
                    last = now
                    Bullets(bullets_count).shot((p.x + 21, p.y - 25))
                    Bullets(bullets_count).shot((p.x + 76, p.y - 25))
                    if is_sound:
                        play_sound('resources/sounds/shot_sound.mp3', 0.1)
                    Bullets.shooting = True
                    bullets_shot += 2

            # спавн врагов
            if event.type == pygame.USEREVENT and level_bckgd_pos >= -4500 and not bs:
                bs = True
                b = Boss()
            if event.type == pygame.USEREVENT and level_bckgd_pos < -4500:
                Enemy(enemies)
            if event.type == pygame.USEREVENT and death:
                ingame_music.stop()
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
        if level_bckgd_pos > 1600:
            death = True
        # передвижение игрока
        if p.health_count > 0:

            # проверка коллизии врага, игрока и пули
            for i in enemies:
                collision = pygame.sprite.collide_rect(p, i)
                if collision:
                    Explosion(booms).boom((i.rect.x, i.rect.y))
                    if is_sound:
                        play_sound('resources/sounds/explosion_sound.mp3', 0.1)
                    if i.health_count - 2 <= 0:
                        game_score += 10
                        i.kill()
                        Explosion(booms).boom((i.rect.x, i.rect.y))
                        if is_sound:
                            play_sound('resources/sounds/explosion_sound.mp3', 0.1)
                        enemy_killed += 1
                    else:
                        i.health_count -= 2
                        if is_sound:
                            play_sound('resources/sounds/collision_sound.mp3', 0.03)
                    p.health_count -= 1
                    if is_sound:
                        play_sound('resources/sounds/explosion_sound.mp3', 0.05)
                    if p.health_count > 0:
                        Damage(window_holes).taking_damage((random.randint(50, 550), random.randint(50, 750)))
                        if is_sound:
                            play_sound('resources/sounds/window_crashed.mp3', 0.1)
                            play_sound('resources/sounds/explosion_stun.mp3', 0.02)
                for j in bullets_count:
                    collision = pygame.sprite.collide_rect(j, i)
                    if collision:
                        if i.health_count - 1 <= 0:
                            game_score += 5
                            i.kill()
                            Explosion(booms).boom((i.rect.x, i.rect.y))
                            if is_sound:
                                play_sound('resources/sounds/explosion_sound.mp3', 0.1)
                            enemy_killed += 1
                        else:
                            i.health_count -= 1
                            Miniexplosion(mini_booms).boom((j.rect.x, j.rect.y))
                            if is_sound:
                                play_sound('resources/sounds/explosion_sound.mp3', 0.1)
                            if is_sound:
                                play_sound('resources/sounds/collision_sound.mp3', 0.03)
                        j.kill()

            if bs and not boss_death:
                collision = pygame.sprite.collide_rect(b, p)
                if collision and b.y > 10:
                    b.health_count -= 0.3
                    if is_sound:
                        play_sound('resources/sounds/collision_sound.mp3', 0.03)
                    p.health_count -= 0.2
                    if is_sound:
                        play_sound('resources/sounds/explosion_sound.mp3', 0.05)
                    if b.body == b.stay1 or b.body == b.stay2:
                        b.body = b.stay2
                    if b.body == b.stay3 or b.body == b.stay4:
                        b.body = b.stay4
                    if b.body == b.stay5 or b.body == b.stay6:
                        b.body = b.stay6
                    col_check += 1
                    if p.health_count > 1:
                        Damage(window_holes).taking_damage((random.randint(50, 550), random.randint(50, 750)))
                        if is_sound:
                            play_sound('resources/sounds/window_crashed.mp3', 0.1)
                            play_sound('resources/sounds/explosion_stun.mp3', 0.02)
                for j in bullets_count:
                    collision = pygame.sprite.collide_rect(b, j)
                    if collision and b.y > 10:
                        if b.body == b.stay1 or b.body == b.stay2:
                            b.body = b.stay2
                        if b.body == b.stay3 or b.body == b.stay4:
                            b.body = b.stay4
                        if b.body == b.stay5 or b.body == b.stay6:
                            b.body = b.stay6
                        col_check += 1
                        b.health_count -= 0.3
                        Miniexplosion(mini_booms).boom((j.rect.x, j.rect.y))
                        if is_sound:
                            play_sound('resources/sounds/explosion_sound.mp3', 0.1)
                        if is_sound:
                            play_sound('resources/sounds/collision_sound.mp3', 0.03)
                        j.kill()

            if bs:
                if battle_music:
                    ingame_music.stop()
                    ingame_music = pygame.mixer.Sound('resources/sounds/music/wagner_main_theme.mp3')
                    ingame_music.set_volume(ingame_music_sound)
                    ingame_music.play()
                    battle_music = False
                b.update()

                if b.body == b.stay3 and phase1_score:
                    game_score += 100
                    phase1_score = False
                if b.body == b.stay5 and phase2_score:
                    game_score += 100
                    phase2_score = False
                if b.body == b.stay7 and phase3_score:
                    game_score += 200
                    phase3_score = False

                if col_check % 40 == 0:
                    b.change_sprite()
                else:
                    col_check += 1
                if b.health_count > 0:
                    screen.blit(b.body, (b.x, b.y))
                elif b.health_count <= 0 and phase4_score:
                    boss_done = True
                    phase4_score = False
                    game_score += 350
                    if is_sound:
                        play_sound('resources/sounds/boss_defeated.mp3', 0.2)

                    Explosion(booms).boom((b.rect.x + 75, b.rect.y + 25))
                    Explosion(booms).boom((b.rect.x, b.rect.y))
                    Explosion(booms).boom((b.rect.x + 200, b.rect.y + 34))
                    Explosion(booms).boom((b.rect.x + 250, b.rect.y + 25))
                    Explosion(booms).boom((b.rect.x + 150, b.rect.y + 56))
                    if is_sound:
                        play_sound('resources/sounds/explosion_sound.mp3', 0.1)
                    boss_death = True

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
                if is_sound:
                    play_sound('resources/sounds/plane_crash.mp3', 0.05)
            p.minimize += 1
            if not death:
                if p.minimize <= 320:
                    p.death()
                    screen.blit(p.death_sp, (p.x, p.y))
                else:
                    death = True
                    Smallexplosions(small_booms).boom((p.rect.x + 3, p.rect.y + 25))
                    Smallexplosions(small_booms).boom((p.rect.x, p.rect.y))
                    Smallexplosions(small_booms).boom((p.rect.x - 22, p.rect.y + 7))
                    if is_sound:
                        play_sound('resources/sounds/explosion_sound.mp3', 0.1)
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

        mini_booms.update()
        mini_booms.draw(screen)

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


def death_screen():
    global running_game, game_score
    running = True
    click = False
    draw_counter = 0
    color_counter = 0
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    rating_kills = enemy_killed//10
    if bullets_shot < 800:
        rating_shots = 1
    else:
        rating_shots = 0
    rating = rating_kills + rating_shots

    if boss_done:
        death_music = pygame.mixer.Sound('resources/sounds/music/victory_theme.mp3')
        death_music.stop()
        death_music_sound = 0.1
        if not is_sound:
            death_music_sound = 0
        death_music.set_volume(death_music_sound)
        death_music.play()
        rating += 2
    else:
        death_music = pygame.mixer.Sound('resources/sounds/music/loose_theme.mp3')
        death_music.stop()
        death_music_sound = 0.1
        if not is_sound:
            death_music_sound = 0
        death_music.set_volume(death_music_sound)
        death_music.play()
    while True:
        if len(str(game_score)) < 6:
            game_score = '0' + str(game_score)
        else:
            break
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill((0, 0, 0))
        # ------------------------------------------ name zone draw
        pygame.draw.rect(screen, (0, 0, 0), (50, 10, 500, 50))
        pygame.draw.rect(screen, (255, 255, 255), (50, 10, 500, 50), 3)
        draw_text('End of your way', font, (255, 255, 255), screen, 120, 15)
        # ------------------------------------------ button menu
        button_menu = pygame.image.load('resources/sprites/button.png')
        button_menu = pygame.transform.scale(button_menu, (200, 70))
        b_menu_mask = button_menu.get_rect()
        b_menu_mask.x = 195
        b_menu_mask.y = 700
        screen.blit(button_menu, (b_menu_mask.x, b_menu_mask.y))
        draw_text('menu', font, (255, 255, 255), screen, 245, 730)
        # ------------------------------------------ draw
        if draw_counter >= 1:
            draw_text('Player: {}'.format(player_name), font, (255, 255, 255), screen, 50, 150)
        if draw_counter >= 2:
            draw_text('Score: {}'.format(game_score), font, (255, 255, 255), screen, 50, 230)
        if draw_counter >= 3:
            draw_text('Enemies killed: {}'.format(enemy_killed), font, (255, 255, 255), screen, 50, 310)
        if draw_counter >= 4:
            draw_text('Bullets fired: {}'.format(bullets_shot), font, (255, 255, 255), screen, 50, 390)
        if draw_counter >= 5:
            draw_text('Rating:', font, (255, 255, 255), screen, 50, 470)
        if draw_counter >= 6:
            if rating <= 4:
                draw_text('F', font_rating, (100, 100, 100), screen, 300, 470)
            elif rating == 5:
                draw_text('D', font_rating, (29, 173, 23), screen, 300, 470)
            elif rating == 6:
                draw_text('C', font_rating, (20, 20, 255), screen, 300, 470)
            elif rating == 7:
                draw_text('B', font_rating, (200, 0, 255), screen, 300, 470)
            elif rating == 8:
                draw_text('A', font_rating, (255, 200, 0), screen, 300, 470)
            elif rating == 9:
                draw_text('S', font_rating, (255, 100, 0), screen, 300, 470)
            elif rating <= 11:
                draw_text('SS', font_rating, (255, 0, 0), screen, 300, 470)
            else:
                if color_counter == 0:
                    draw_text('SSS', font_rating, (255, 0, 0), screen, 300, 470)
                elif color_counter == 1:
                    draw_text('SSS', font_rating, (0, 255, 0), screen, 300, 470)
                else:
                    draw_text('SSS', font_rating, (0, 0, 255), screen, 300, 470)
        # ------------------------------------------ collide
        if b_menu_mask.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 0, 100), (195, 700, 200, 70), 4)
            if click:
                if is_sound:
                    if is_sound:
                        play_sound('resources/sounds/click_sound.mp3', 0.2)
                else:
                    pass
                running = False
                running_game = False
        # ------------------------------------------ events
        click = False
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                draw_counter += 1
                color_counter += 1
                if color_counter == 3:
                    color_counter = 0
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                running_game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        # ------------------------------------------ update
        pygame.display.update()
        clock.tick(10)
    death_music.stop()


if __name__ == '__main__':
    main_menu()

    pygame.quit()
