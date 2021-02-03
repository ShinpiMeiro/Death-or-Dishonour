import pygame


class Smallexplosions(pygame.sprite.Sprite):
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
            self.image = pygame.transform.scale(self.ex_all[self.booms], (30, 30))
