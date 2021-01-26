import pygame
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

screen = pygame.display.set_mode((width, height))
speed = 2


def game_screen():
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    menu = True
    pygame.init()
    enemies = pygame.sprite.Group()
    p = Player()
    booms = []
    bullets_count = pygame.sprite.Group()
    level_bckgd_pos = -4800
    current_player_sprite = 'stay'
    game_over = False
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    # заголовок окна
    pygame.display.set_caption('Death or Dishonour')
    # иконка приложения
    pygame.display.set_icon(pygame.image.load('resources/images/test_small_logo_1.bmp'))
    # задний фон
    current_level_background = pygame.image.load('resources/level_pictures/first_level_bckgd.jpg')
    # фоновая музыка
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
                Bullets(bullets_count).shot((p.x + 21, p.y - 25))
                Bullets(bullets_count).shot((p.x + 76, p.y - 25))
                Bullets.shooting = True

            # нереализованная функция
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pass
            # нереализованная функция
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                pass
            # плохо реализованный спавн врагов
            if event.type == pygame.USEREVENT:
                Enemy(200, -100, enemies)
            # если пользователь закроет программу, игра завершится
            if event.type == pygame.QUIT:
                game_over = True
        # на всякий случай делаем белую заливку
        screen.fill((0, 0, 0))
        # передвижение заднего фона
        level_bckgd_pos += 1
        if level_bckgd_pos >= 0:
            level_bckgd_pos = -4800
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
        for i in enemies:
            offset = (p.x - i.rect.x, p.y - i.rect.y)
            # если есть коллизия - уничтожение врага
            if p.mask.overlap_area(i.mask, offset) > 0:
                booms.append((i.rect.x, i.rect.y))
                boom = Explosion()
                i.kill()
        # взрыв на месте убитого врага
        # TODO очень хочу есть - тут крайне корявая реализация,
        #  если протаранишь несколько самолетов оч быстро - увидишь,
        #  подумай что можно с этим сделать
        for i in booms:
            try:
                screen.blit(boom.boom(), i)
            except IndexError:
                booms.remove(i)
        # обновление экрана
        pygame.display.flip()
        # фпс таймер
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    game_screen()

    pygame.quit()
