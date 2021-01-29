import pygame


def play_sound(sound_p, volume_h=0.5, wait_t=0):
    pl_sound = pygame.mixer.Sound(sound_p)
    pl_sound.set_volume(volume_h)
    pl_sound.play()
    pygame.time.wait(wait_t)


class Explosion(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.add(group)
        self.booms = -1
        self.ex_all = []
        self.ex1 = pygame.image.load("resources/sprites/65_explosions_sprite/1.png")
        self.ex2 = pygame.image.load("resources/sprites/65_explosions_sprite/2.png")
        self.ex3 = pygame.image.load("resources/sprites/65_explosions_sprite/3.png")
        self.ex4 = pygame.image.load("resources/sprites/65_explosions_sprite/4.png")
        self.ex5 = pygame.image.load("resources/sprites/65_explosions_sprite/5.png")
        self.ex6 = pygame.image.load("resources/sprites/65_explosions_sprite/6.png")
        self.ex7 = pygame.image.load("resources/sprites/65_explosions_sprite/7.png")
        self.ex8 = pygame.image.load("resources/sprites/65_explosions_sprite/8.png")
        self.ex9 = pygame.image.load("resources/sprites/65_explosions_sprite/9.png")
        self.ex10 = pygame.image.load("resources/sprites/65_explosions_sprite/10.png")
        self.ex11 = pygame.image.load("resources/sprites/65_explosions_sprite/11.png")
        self.ex12 = pygame.image.load("resources/sprites/65_explosions_sprite/12.png")
        self.ex13 = pygame.image.load("resources/sprites/65_explosions_sprite/13.png")
        self.ex14 = pygame.image.load("resources/sprites/65_explosions_sprite/14.png")
        self.ex15 = pygame.image.load("resources/sprites/65_explosions_sprite/15.png")
        self.ex16 = pygame.image.load("resources/sprites/65_explosions_sprite/16.png")
        self.ex17 = pygame.image.load("resources/sprites/65_explosions_sprite/17.png")
        self.ex18 = pygame.image.load("resources/sprites/65_explosions_sprite/18.png")
        self.ex19 = pygame.image.load("resources/sprites/65_explosions_sprite/19.png")
        self.ex20 = pygame.image.load("resources/sprites/65_explosions_sprite/20.png")
        self.ex21 = pygame.image.load("resources/sprites/65_explosions_sprite/21.png")
        self.ex22 = pygame.image.load("resources/sprites/65_explosions_sprite/22.png")
        self.ex23 = pygame.image.load("resources/sprites/65_explosions_sprite/23.png")
        self.ex24 = pygame.image.load("resources/sprites/65_explosions_sprite/24.png")
        self.ex25 = pygame.image.load("resources/sprites/65_explosions_sprite/25.png")
        self.ex26 = pygame.image.load("resources/sprites/65_explosions_sprite/26.png")
        self.ex27 = pygame.image.load("resources/sprites/65_explosions_sprite/27.png")
        self.ex28 = pygame.image.load("resources/sprites/65_explosions_sprite/28.png")
        self.ex29 = pygame.image.load("resources/sprites/65_explosions_sprite/29.png")
        self.ex30 = pygame.image.load("resources/sprites/65_explosions_sprite/30.png")
        self.ex31 = pygame.image.load("resources/sprites/65_explosions_sprite/31.png")
        self.ex32 = pygame.image.load("resources/sprites/65_explosions_sprite/32.png")
        self.ex33 = pygame.image.load("resources/sprites/65_explosions_sprite/33.png")
        self.ex34 = pygame.image.load("resources/sprites/65_explosions_sprite/34.png")
        self.ex35 = pygame.image.load("resources/sprites/65_explosions_sprite/35.png")
        self.ex36 = pygame.image.load("resources/sprites/65_explosions_sprite/36.png")
        self.ex37 = pygame.image.load("resources/sprites/65_explosions_sprite/37.png")
        self.ex38 = pygame.image.load("resources/sprites/65_explosions_sprite/38.png")
        self.ex39 = pygame.image.load("resources/sprites/65_explosions_sprite/39.png")
        self.ex40 = pygame.image.load("resources/sprites/65_explosions_sprite/40.png")
        self.ex41 = pygame.image.load("resources/sprites/65_explosions_sprite/41.png")
        self.ex42 = pygame.image.load("resources/sprites/65_explosions_sprite/42.png")
        self.ex43 = pygame.image.load("resources/sprites/65_explosions_sprite/43.png")
        self.ex44 = pygame.image.load("resources/sprites/65_explosions_sprite/44.png")
        self.ex45 = pygame.image.load("resources/sprites/65_explosions_sprite/45.png")
        self.ex46 = pygame.image.load("resources/sprites/65_explosions_sprite/46.png")
        self.ex47 = pygame.image.load("resources/sprites/65_explosions_sprite/47.png")
        self.ex48 = pygame.image.load("resources/sprites/65_explosions_sprite/48.png")
        self.ex49 = pygame.image.load("resources/sprites/65_explosions_sprite/49.png")
        self.ex50 = pygame.image.load("resources/sprites/65_explosions_sprite/50.png")
        self.ex51 = pygame.image.load("resources/sprites/65_explosions_sprite/51.png")
        self.ex52 = pygame.image.load("resources/sprites/65_explosions_sprite/52.png")
        self.ex53 = pygame.image.load("resources/sprites/65_explosions_sprite/53.png")
        self.ex54 = pygame.image.load("resources/sprites/65_explosions_sprite/54.png")
        self.ex55 = pygame.image.load("resources/sprites/65_explosions_sprite/55.png")
        self.ex56 = pygame.image.load("resources/sprites/65_explosions_sprite/56.png")
        self.ex57 = pygame.image.load("resources/sprites/65_explosions_sprite/57.png")
        self.ex58 = pygame.image.load("resources/sprites/65_explosions_sprite/58.png")
        self.ex59 = pygame.image.load("resources/sprites/65_explosions_sprite/59.png")
        self.ex60 = pygame.image.load("resources/sprites/65_explosions_sprite/60.png")
        self.ex61 = pygame.image.load("resources/sprites/65_explosions_sprite/61.png")
        self.ex62 = pygame.image.load("resources/sprites/65_explosions_sprite/62.png")
        self.ex63 = pygame.image.load("resources/sprites/65_explosions_sprite/63.png")
        self.ex64 = pygame.image.load("resources/sprites/65_explosions_sprite/64.png")
        self.ex65 = pygame.image.load("resources/sprites/65_explosions_sprite/65.png")
        self.ex_all.append(self.ex1)
        self.ex_all.append(self.ex2)
        self.ex_all.append(self.ex3)
        self.ex_all.append(self.ex4)
        self.ex_all.append(self.ex5)
        self.ex_all.append(self.ex6)
        self.ex_all.append(self.ex7)
        self.ex_all.append(self.ex8)
        self.ex_all.append(self.ex9)
        self.ex_all.append(self.ex10)
        self.ex_all.append(self.ex11)
        self.ex_all.append(self.ex12)
        self.ex_all.append(self.ex13)
        self.ex_all.append(self.ex14)
        self.ex_all.append(self.ex15)
        self.ex_all.append(self.ex16)
        self.ex_all.append(self.ex17)
        self.ex_all.append(self.ex18)
        self.ex_all.append(self.ex19)
        self.ex_all.append(self.ex20)
        self.ex_all.append(self.ex21)
        self.ex_all.append(self.ex22)
        self.ex_all.append(self.ex23)
        self.ex_all.append(self.ex24)
        self.ex_all.append(self.ex25)
        self.ex_all.append(self.ex26)
        self.ex_all.append(self.ex27)
        self.ex_all.append(self.ex28)
        self.ex_all.append(self.ex29)
        self.ex_all.append(self.ex30)
        self.ex_all.append(self.ex31)
        self.ex_all.append(self.ex32)
        self.ex_all.append(self.ex33)
        self.ex_all.append(self.ex34)
        self.ex_all.append(self.ex35)
        self.ex_all.append(self.ex36)
        self.ex_all.append(self.ex37)
        self.ex_all.append(self.ex38)
        self.ex_all.append(self.ex39)
        self.ex_all.append(self.ex40)
        self.ex_all.append(self.ex41)
        self.ex_all.append(self.ex42)
        self.ex_all.append(self.ex43)
        self.ex_all.append(self.ex44)
        self.ex_all.append(self.ex45)
        self.ex_all.append(self.ex46)
        self.ex_all.append(self.ex47)
        self.ex_all.append(self.ex48)
        self.ex_all.append(self.ex49)
        self.ex_all.append(self.ex50)
        self.ex_all.append(self.ex51)
        self.ex_all.append(self.ex52)
        self.ex_all.append(self.ex53)
        self.ex_all.append(self.ex54)
        self.ex_all.append(self.ex55)
        self.ex_all.append(self.ex56)
        self.ex_all.append(self.ex57)
        self.ex_all.append(self.ex58)
        self.ex_all.append(self.ex59)
        self.ex_all.append(self.ex60)
        self.ex_all.append(self.ex61)
        self.ex_all.append(self.ex62)
        self.ex_all.append(self.ex63)
        self.ex_all.append(self.ex64)
        self.ex_all.append(self.ex65)
        self.image = self.ex1
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0

    def boom(self, ex_pos):
        self.rect.x, self.rect.y = ex_pos[0], ex_pos[1]
        play_sound('resources/sounds/explosion_sound.mp3', 0.1)

    def update(self):
        self.booms += 1
        if self.booms == 64:
            self.kill()
        else:
            self.image = self.ex_all[self.booms]

