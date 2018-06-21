import random
import pygame
w_screen = 600
h_screen = 600
displaysurf = pygame.display.set_mode((w_screen,h_screen))
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
pygame.init()
leadx = w_screen/2
leady = h_screen/2
xchange = 0
ychange = 0
one_circle = 7
fps = 15
snake_tail = []
one_cell = 20
x_food = random.randint(15, w_screen)
y_food = random.randint(15, h_screen)
gameover = False
clock = pygame.time.Clock()
length_snake = 5
move = ''
class Snake:
    def __init__(self,snake_length,snake_tail,leadx,leady,xchange,ychange,game_over,move):
        self.leadx = leadx
        self.leady = leady
        self.snakepos = snake_tail
        self.length = snake_length
        self.snake_head = []
        self.xchange = xchange
        self.ychange = ychange
        self.gameover = game_over
        self.move = move
    def draw(self):
        self.leadx += self.xchange
        self.leady += self.ychange
        self.snake_head.append(self.leadx)
        self.snake_head.append(self.leady)
        snake_tail.append(self.snake_head)
        if len(snake_tail) > self.length:
            del snake_tail[0]
        for cord in self.snakepos:
            x = cord[0]
            y = cord[1]
            pygame.draw.rect(displaysurf,white,(x,y,one_cell,one_cell))
            pygame.draw.rect(displaysurf,green,(x+5,y+5,10,10))
    def eatself(self):
        for tail in self.snakepos[:-1]:
            if tail == self.snake_head:
                self.gameover = True
    def hitwall(self):
        if self.leadx < 0 or self.leady < 0 or self.leadx > w_screen or self.leady > h_screen:
            self.gameover = True

class Food(Snake):
    def __init__(self,xfood,yfood,foodeat):
        self.x = xfood
        self.y = yfood
        self.foodeat = foodeat
    def draw(self):
        pygame.draw.circle(displaysurf,red,(self.x, self.y), one_circle)
    def was_eat(self):
        if leadx <= self.x <=leadx+one_cell and leady <= self.y <= leady+one_cell:
            pygame.draw.circle(displaysurf, red, (self.x,self.y), one_circle)
            length += 1
def main():
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and move != 'left':
                    xchange = one_cell
                    ychange = 0
                    move = 'right'
                elif event.key == pygame.K_LEFT and move != 'right':
                    xchange = -one_cell
                    ychange = 0
                    move = 'left'
                elif event.key == pygame.K_UP and move != 'down':
                    ychange = -one_cell
                    xchange = 0
                    move = 'dup'
                elif event.key == pygame.K_DOWN and move != 'up':
                    ychange = one_cell
                    xchange = 0
                    move = 'down'
            elif event.type == pygame.quit():
                gameover = True
        displaysurf.fill(black)
        Snake(length_snake,snake_tail,leadx,leady,xchange,ychange,gameover,move)
        Food(x_food,y_food)
        pygame.display.update()
        clock.tick(fps)
if __name__ == '__main__':
    main()