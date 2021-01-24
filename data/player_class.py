import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.stay1 = pygame.image.load('resources/sprites/player_stay1.png')
        self.stay1 = pygame.transform.scale(self.stay1, (119, 100))
        self.stay2 = pygame.image.load('resources/sprites/player_stay2.png')
        self.stay2 = pygame.transform.scale(self.stay2, (119, 100))
        self.stay_1 = True

        self.left1 = pygame.image.load('resources/sprites/player_left1.png')
        self.left1 = pygame.transform.scale(self.left1, (109, 100))
        self.left2 = pygame.image.load('resources/sprites/player_left2.png')
        self.left2 = pygame.transform.scale(self.left2, (109, 100))
        self.left_1 = True

        self.right1 = pygame.image.load('resources/sprites/player_right1.png')
        self.right1 = pygame.transform.scale(self.right1, (109, 100))
        self.right2 = pygame.image.load('resources/sprites/player_right2.png')
        self.right2 = pygame.transform.scale(self.right2, (109, 100))
        self.right_1 = True

        self.x = 241
        self.y = 650
        self.speed = 3
        self.xvel = 0
        self.yvel = 0

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.health_count = 3
        self.status = True
        self.body = self.stay1

    def anim_stay(self):
        if self.stay_1:
            self.body = self.stay1
        else:
            self.body = self.stay2
        return self.body

    def anim_left(self):
        if self.left_1:
            self.body = self.left1
        else:
            self.body = self.left2
        return self.body

    def anim_right(self):
        if self.right_1:
            self.body = self.right1
        else:
            self.body = self.right2
        return self.body

    def update(self, FPS):
        if self.moving_up:
            self.yvel = -self.speed

        if self.moving_down:
            self.yvel = self.speed

        if self.moving_left:
            self.xvel = -self.speed

        if self.moving_right:
            self.xvel = self.speed

        if not(self.moving_left or self.moving_right):
            self.xvel = 0

        if not(self.moving_up or self.moving_down):
            self.yvel = 0

        self.x += self.xvel
        self.y += self.yvel
