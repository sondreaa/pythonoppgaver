import pygame
from math import atan2, pi
from random import choice
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_w,
    K_a,
    K_s,
    K_d,
    K_RETURN
)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 150)
yellow = (255, 255, 0)


dis_width = 500
dis_height = 500

tile = 25

class Bullet(pygame.sprite.Sprite):
    def __init__(self, dir, player: pygame.sprite.Sprite, wr, er):
        super(Bullet,self).__init__()
        #self.surf = pygame.image.load(("sprites/bullet.png")) 
        #self.surf = self.surf.convert()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill(yellow)
        self.rect = self.surf.get_rect(center=player.rect.move(tile*dir[0], tile*dir[1]).center)
        self.dir = dir
        #print("Making bullet")
        if self.rect.collidelist(wr) != -1:
            #print("killing bullet")
            player.bullet = None
            self.kill()
        
        if (e := self.rect.collidelist(er)) != -1:
            enemies[e].kill()
            del enemies[e]
            player.bullet = None
            self.kill()

    def update(self, walls: list[pygame.sprite.Sprite], enemies: list[pygame.sprite.Sprite], player):
        er = [e.rect for e in enemies]
        wr = [w.rect for w in walls]
        self.rect.move_ip(self.dir[0]*tile, self.dir[1]*tile)

        if self.rect.collidelist(wr) != -1:
            player.bullet = None
            self.kill()
        
        if (e := self.rect.collidelist(er)) != -1:
            enemies[e].kill()
            del enemies[e]
            player.bullet = None
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        #self.surf = pygame.image.load(("sprites/player32.png")) 
        #self.surf = self.surf.convert()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill(white)
        self.rect = self.surf.get_rect(center=(10*tile, 10*tile))
        self.prev_pressed = {K_UP: False, K_DOWN: False, K_LEFT: False, K_RIGHT: False, K_w: False}
        self.bullet = None
        self.is_dead = False
        self.dir = 270

    def update(self, pressed_keys, walls, enemies):
        if self.is_dead:
            return False
        wr = [w.rect for w in walls]
        er = [e.rect for e in enemies]
        moved = False
        moved |= self.move(pressed_keys, wr, K_UP, (0, -tile))
        moved |= self.move(pressed_keys, wr, K_LEFT, (-tile, 0))
        moved |= self.move(pressed_keys, wr, K_DOWN, (0, tile))
        moved |= self.move(pressed_keys, wr, K_RIGHT, (tile, 0))

        self.try_shoot(pressed_keys, K_w, (0, -1), wr, er)
        self.try_shoot(pressed_keys, K_s, (0, 1), wr, er)
        self.try_shoot(pressed_keys, K_a, (-1, 0), wr, er)
        self.try_shoot(pressed_keys, K_d, (1, 0), wr, er)
        return moved 

    def try_shoot(self, pressed_keys, key, dir, wr, er):
        if pressed_keys[key] and not self.prev_pressed[key]:
            self.shoot(dir, wr, er)
            self.prev_pressed[key] = True
        if not pressed_keys[key]:
            self.prev_pressed[key] = False
       

    def shoot(self, dir, wr, er):
        if self.bullet:
            return
        self.bullet = 1
        b = Bullet(dir, self, wr, er)
        if self.bullet:
            self.bullet = b

    def move(self, pressed_keys, wr, key, dir):
        moved = False
        if pressed_keys[key] and not self.prev_pressed[key] and self.rect.move(dir[0], dir[1]).collidelist(wr) == -1:
            self.rect.move_ip(dir[0], dir[1])
            self.prev_pressed[key] = True
            moved=True
            self.dir = round(atan2(dir[1], dir[0])*180/pi)
        if not pressed_keys[key]:
            self.prev_pressed[key] = False
        return moved

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Wall, self).__init__()
        #self.surf = pygame.image.load(("sprites/wall32.png")) 
        #self.surf = self.surf.convert()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill(blue)
        self.rect = self.surf.get_rect(center=(x*tile, y*tile))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Enemy, self).__init__()
        #self.surf = pygame.image.load(("sprites/enemy.png"))
        #self.surf = self.surf.convert()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill(red)
        self.rect = self.surf.get_rect(center=(x*tile, y*tile))
        self.dir = 270
        

    def update(self, player: Player):
        wr = [w.rect for w in walls]
        self_x = self.rect.centerx
        self_y = self.rect.centery
        player_x = player.rect.centerx
        player_y = player.rect.centery
        avstand = max(abs(self_x - player_x), abs(self_y-player_y))
        if avstand > 3*tile:
            retning = choice([(0, -tile), (0, tile), (-tile, 0), (tile, 0)])
            if self.rect.move(retning).collidelist(wr) == -1:
                self.rect.move_ip(retning)
                self.dir = round(atan2(retning[1], retning[0])*180/pi)
        else:
            if self_y < player_y:
                retning = (0, tile)
            if self_y > player_y:
                retning = (0, -tile)
            if self_y == player_y and self_x < player_x:
                retning = (tile, 0)
            if self_y == player_y and self_x > player_x:
                retning = (-tile, 0)
            if self_y == player_y and self_x == player_x:
                retning = (0, 0)
                player.is_dead = True
        
            if self.rect.move(retning).collidelist(wr) == -1:
                self.rect.move_ip(retning)
                self.dir = round(atan2(retning[1], retning[0])*180/pi)
            if self.rect.center == player.rect.center:
                player.is_dead = True

pygame.init()
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('sondre spill')

titlefont = pygame.font.Font('freesansbold.ttf', 45)
titletext = titlefont.render('sondre spill', True, green, black)
titletextRect = titletext.get_rect()
titletextRect.center = (dis_width // 2, tile*7)

font12 = pygame.font.Font('freesansbold.ttf', 20)
text1 = font12.render('start: <enter>', True, green, black)
text1Rect = text1.get_rect()
text1Rect.center = (dis_width // 2, tile*10)

text2 = font12.render('avslutt: <escape>', True, green, black)
text2Rect = text2.get_rect()
text2Rect.center = (dis_width // 2, tile*12)

running = True
quitted = False
while running:
    for event in pygame.event.get():
        
        if event.type == KEYDOWN:
            
            if event.key == K_ESCAPE:
                running = False
                quitted = True

            if event.key == K_RETURN:
                running = False

        elif event.type == QUIT:
            running = False
            quitted = True
    
    pressed_keys = pygame.key.get_pressed()

    dis.fill(black)
    dis.blit(titletext, titletextRect)
    dis.blit(text1, text1Rect)
    dis.blit(text2, text2Rect)

    pygame.display.update()

deadfont = pygame.font.Font('freesansbold.ttf', 40)
deadtext = deadfont.render('Du er dau.', True, green, red)
deadtextRect = deadtext.get_rect()
deadtextRect.center = (dis_width // 2, dis_height // 2)

player = Player()

enemies = []
for i in range(1, 4):
    enemies.append(Enemy(i*5, 5))
    enemies.append(Enemy(i*5, 15))

walls = [Wall(0, 0)]
for i in range(20):
    walls.append(Wall(0, i+1))
    walls.append(Wall(i+1, 0))
    walls.append(Wall(20, i+1))
    walls.append(Wall(i+1, 20))


running = True
while running and not quitted:
    for event in pygame.event.get():
    
        if event.type == KEYDOWN:
            
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False
    
    pressed_keys = pygame.key.get_pressed()

    if player.update(pressed_keys, walls, enemies):
        if player.bullet:
            player.bullet.update(walls, enemies, player)
        for enemy in enemies:
            enemy.update(player)
        if player.bullet and (e:= player.bullet.rect.collidelist([e.rect for e in enemies])) != -1:
            del enemies[e]
            player.bullet = None
        
    dis.fill(black)

    if player.bullet:
        dis.blit(player.bullet.surf, player.bullet.rect)
    dis.blit(pygame.transform.rotate(player.surf, 270-player.dir), player.rect)

    for wall in walls:
        dis.blit(wall.surf, wall.rect)

    for enemy in enemies:
        dis.blit(pygame.transform.rotate(enemy.surf, 270-enemy.dir), enemy.rect)
    
    if player.is_dead:
        dis.blit(deadtext, deadtextRect)

    pygame.display.update()


