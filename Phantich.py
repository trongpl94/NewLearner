import pygame
import time
from pygame.locals import *
width = 720
height = 355
white = (255,255,255)
black = (0,0,0)
display_on = pygame.display.set_mode((width,height))
pygame.display.set_caption('TromCho')
fps = pygame.time.Clock()
fps_s = 20
bsize = 40
count = 0
green = (0,255,0)
done = False
const_x_player = 0
const_x_poop = 3000
defult_stm = False
class Black_hole:
     def __init__(self,cord):
         self.cord = cord
     def draw_water(self):
         for pos in self.cord:
            water = pygame.image.load('waterfall.png')
            display_on.blit(water, (pos, 40))
     def draw_hole(self):
         if jump_in_black == False:
            for pos in self.cord:
                gai = pygame.image.load('gai.png')
                display_on.blit(gai, (pos, height-bsize))
         else:
             self.draw_water()
class Poop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        po = pygame.image.load('poop.png')
        display_on.blit(po,(self.x,self.y))
class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        if car_active == True:
            c1 = pygame.image.load('car2.png')
            display_on.blit(c1,(self.x,self.y))
        else:
            self.x = 0
            self.y = 0
class Horse:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
            h = pygame.image.load('bullet.png')
            display_on.blit(h, (self.x, self.y))
class Invisible_wall:
    def __init__(self,cord):
        self.cord = cord
    def draw(self):
        if hit_wall == True:
            for wallcord in self.cord:
                o = pygame.image.load('invisible_wall.png')
                display_on.blit(o, (wallcord, 0))
class Hearth:
    def __init__(self, n_life):
        self.life1 = n_life
    def draw(self):
        H = pygame.image.load('hearth.png')
        for lifetime in range(1,self.life1+1):
            display_on.blit(H, (30*lifetime, 20))
class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self):
        if image_stm == 'alive':
            if x_change > 0:
                image = 'player1.png'
                playerr = pygame.image.load(image)
                display_on.blit(playerr,(self.x,self.y))
            elif x_change < 0:
                image = 'player2.png'
                playerl = pygame.image.load(image)
                display_on.blit(playerl,(self.x,self.y))
        elif image_stm == 'crashed':
            crashed = pygame.image.load('player.png').convert_alpha()
            display_on.blit(crashed,(self.x-210,self.y+17))
        elif image_stm == 'fall':
            fall = pygame.image.load('fall.png')
            display_on.blit(fall, (self.x+100, height-10))
class Game:
    def __init__(self,Player,Ca,Hearth1,Hole,Poo,Horse,Wall):
        self.player = Player
        self.car = Ca
        self.hearth = Hearth1
        self.black_hole = Hole
        self.poop = Poo
        self.horse = Horse
        self.wall = Wall
    def draw(self):
        self.player.draw()
        self.car.draw()
        self.hearth.draw()
        self.black_hole.draw_hole()
        self.poop.draw()
        self.horse.draw()
        self.wall.draw()
image_stm = 'alive'
life = 3
move_l = False
move_r = False
movemap = 0
jump_in_black = False
hit_wall = False
x_change = 0
y_change = 0
shit_weapon = False
ready_shoot = False
car_active = True
x1 = const_x_player
y1 = height-(1.5*bsize)
xcar = 2626
ycar = height-(1.5*bsize)
hole_cord =[500,1000,1500,2000]
wall_cord =[200,600,1000,4600,5000]
xpoop = const_x_poop
ypoop = height - 45
xpoop_change = 0
xhorse = 700
yhorse = height - 21
timer = 1
background = pygame.image.load('street.jpg')
name = ''
done_name = False
jump = False
while not done:
    pygame.init()
    FONT = pygame.font.Font(None, 25)
    FONT1 = pygame.font.Font(None, 60)
    P = Player(x1, y1)
    Ca = Car(xcar, ycar)
    He = Hearth(life)
    Ho = Black_hole(hole_cord)
    Po = Poop(xpoop, ypoop)
    Hor = Horse(xhorse, yhorse)
    Wa = Invisible_wall(wall_cord)
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and done_name == False:
            name += event.unicode
            if event.key == K_RETURN:
                done_name = True
        elif event.type == KEYDOWN and done_name == True:
            if event.key == K_LEFT:
                move_l = True
            elif event.key == K_RIGHT:
                move_r = True
            elif event.key == K_SPACE and jump == False:
                timer = 1
                y_change = -110
            elif event.key == K_s and shit_weapon == True:
                xpoop_change = 20
                xpoop += xpoop_change
                if xpoop_change >= 2480:
                    xpoop = 2480
                shit_weapon = False
            elif event.key == K_r and image_stm == 'win':
                image_stm = 'alive'
                life = 10
                x1 = const_x_player
                xpoop = const_x_poop
                movemap = 0
                jump_in_black = defult_stm
                hit_wall = defult_stm
                x_change = 0
                y_change = 0
                shit_weapon = defult_stm
                ready_shoot = defult_stm
                car_active = True
                hole_cord = [500, 1000, 1500, 2000]
                wall_cord = [200, 600, 1000, 1400, 2600, 3000, 3700, 4000, 4600, 5000]
        elif event.type == KEYUP and done_name == False:
            if event.key == K_LEFT:
                move_l = False
            elif event.key == K_RIGHT:
                move_r = False
    if done_name == False:
        display_on.fill((100, 200, 150))
        require = FONT.render('Enter your name to play?', True, (255,0,0))
        name_surface = FONT.render('Dog '+name, True, (0, 0, 0))
        display_on.blit(require, (width / 4, height / 3))
        display_on.blit(name_surface,(width/3+20,height/2-20))
        pygame.display.update()
        fps.tick(1)
    if done_name == True and image_stm != 'dead'and image_stm != 'win':
        xhorse -= 15
        xpoop += xpoop_change
        if car_active == True:
            xcar -= 50
        if xcar <= 0 and car_active == True:
            xcar = 2626
        if xhorse <= 0:
            xhorse = 1000
        if image_stm == 'crashed' or image_stm == 'fall':
            life -= 1
            y1 = 10
            image_stm = 'alive'
        if life <= 0:
            image_stm = 'dead'
        if move_l == True and x1 > 1 and hit_wall != True:
            x_change = -6
            x1 += x_change
            movemap += 38
            for j in range(len(hole_cord)):
                hole_cord[j]+=36
            for q in range(len(wall_cord)):
                wall_cord[q]+=36
            xpoop += 36
        if move_r == True and x1 < 705 and hit_wall != True:
            x_change = 6
            x1 += x_change
            movemap -= 38
            for j in range(len(hole_cord)):
                hole_cord[j]-=36
            for q in range(len(wall_cord)):
                wall_cord[q]-=36
            xpoop -= 36
        if y1 == 295:
            hit_wall = False
            jump_in_black = False
        if x1 > 699:
            image_stm = 'win'
        if xcar <= x1+21 <= xcar+83 and ycar <= y1+21 <= ycar+ 60 and image_stm != 'dead' and car_active == True: #va cham oto
            image_stm = 'crashed'
        for vac in hole_cord:
            if y1 == 185 and vac-40<=x1<=vac+15: #va cham hole
                jump_in_black = True
                image_stm = 'fall'
        for hw in wall_cord:
            if y1 == 185 and hw-20<=x1<=hw+5:
                hit_wall = True
                image_stm = 'crashed'
        if xpoop <= x1+21 <= xpoop+46 and ypoop <= y1+21 <= ypoop + 45 and image_stm != 'dead' and shit_weapon == False:
            shit_weapon = True
        if shit_weapon == True:
            xpoop = x1 + 40
            ypoop = y1
        if shit_weapon == True and xcar <= xpoop+60 <= xcar+83 and ycar <= ypoop+22 <= ycar+60:
            car_active = False
        timer += 1
        if timer == 5:
            y_change = 0
            timer = 0
        if y1 < height-(1.2*bsize):
            y1 = height-(1.5*bsize)
        y1 += y_change
        name_surface = FONT.render(name, True, (0, 0, 0))
        display_on.blit(background, (movemap, 0))
        display_on.blit(name_surface,(x1,y1-25))
        Game(P,Ca,He,Ho,Po,Hor,Wa).draw()
        pygame.display.update()
        fps.tick(10)
    if image_stm == 'dead':
        display_on.fill(black)
        lost_screen = FONT.render('You are lost!,', True, (255, 255, 255))
        display_on.blit(lost_screen, (width / 2-30, 30))
        pygame.display.update()
    if image_stm == 'win':
        display_on.fill((100, 200, 150))
        victory = FONT.render('Your are victory!,R to play again!', True, (255, 0, 0))
        display_on.blit(victory, (width / 3 + 20, height / 2 - 20))
        pygame.display.update()
