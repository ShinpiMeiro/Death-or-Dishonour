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
        for i in range(1, 66):
            self.ex_all.append(pygame.image.load('resources/sprites/65_explosions_sprite/{}.png'.format(i)))

        self.image = self.ex_all[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0

    def boom(self, ex_pos):
        self.rect.x, self.rect.y = ex_pos[0], ex_pos[1]

    def update(self):
        self.booms += 1
        if self.booms == 64:
            self.kill()
        else:
            self.image = self.ex_all[self.booms]


class Miniexplosion(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.add(group)
        self.booms = -1
        self.ex_all = []
        self.ex1 = pygame.image.load("resources/sprites/little_explosions/lit-image4.png")
        self.ex_all.append(self.ex1)
        self.ex2 = pygame.image.load("resources/sprites/little_explosions/lit-image5.png")
        self.ex_all.append(self.ex2)
        self.ex3 = pygame.image.load("resources/sprites/little_explosions/lit-image12.png")
        self.ex_all.append(self.ex3)
        self.ex4 = pygame.image.load("resources/sprites/little_explosions/lit-image13.png")
        self.ex_all.append(self.ex4)
        self.ex5 = pygame.image.load("resources/sprites/little_explosions/lit-image20.png")
        self.ex_all.append(self.ex5)
        self.ex6 = pygame.image.load("resources/sprites/little_explosions/lit-image21.png")
        self.ex_all.append(self.ex6)
        self.ex7 = pygame.image.load("resources/sprites/little_explosions/lit-image28.png")
        self.ex_all.append(self.ex7)
        self.ex8 = pygame.image.load("resources/sprites/little_explosions/lit-image29.png")
        self.ex_all.append(self.ex8)
        self.ex9 = pygame.image.load("resources/sprites/little_explosions/lit-image36.png")
        self.ex_all.append(self.ex9)
        self.ex10 = pygame.image.load("resources/sprites/little_explosions/lit-image37.png")
        self.ex_all.append(self.ex10)
        self.ex11 = pygame.image.load("resources/sprites/little_explosions/lit-image42.png")
        self.ex_all.append(self.ex11)
        self.image = self.ex1
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0

    def boom(self, ex_pos):
        self.rect.x, self.rect.y = ex_pos[0], ex_pos[1]

    def update(self):
        self.booms += 1
        if self.booms == 10:
            self.kill()
        else:
            self.image = pygame.transform.scale(self.ex_all[self.booms], (40, 40))
