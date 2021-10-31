import pygame
from pygame.locals import *
import time
import random
   
SnakeSize = 41 #this is to help move the snake while adding sizes
   
class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("Snake.png").convert()
        self.x = [SnakeSize] * length
        self.y = [SnakeSize] * length
        self.direction = '' #this function is to help determine which way it will continue to move.
    def draw(self):
        self.parent_screen.fill((110,110,5)) #color assignment
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()
        
    def snake_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)
        
    #Everything below to Game is to help change the direction of the snake.
    def move_up(self):
        self.direction = 'up'
        
    def move_down(self):
        self.direction = 'down'
        
    def move_left(self):
        self.direction = 'left'
        
    def move_right(self):
        self.direction = 'right'
        
    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        if self.direction == 'up':
           self.y[0] -= SnakeSize
        if self.direction == 'down':
           self.y[0] += SnakeSize
        if self.direction == 'left':
           self.x[0] -= SnakeSize
        if self.direction == 'right':
           self.x[0] += SnakeSize
        self.draw()

class Mouse:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("Mouse.png").convert()
        self.parent_screen = parent_screen
        self.x = 28
        self.y = 23
        
    def move(self):
        self.x = random.randint(1, 45) * SnakeSize
        self.y = random.randint(1, 45) * SnakeSize
        
    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()
        
class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1820,980))#screen size
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.mouse = Mouse(self.surface)
        self.mouse.draw()
        
    def play(self):     #this is to display everything going on in the while loop and make things a little cleaner.
        self.snake.walk()
        self.mouse.draw()
        
        if self.collide(self.snake.x[0], self.snake.y[0], self.mouse.x, self.mouse.y):
            self.snake.snake_length()
            self.mouse.move()
        
    def collide(self, x1, y1, x2, y2):
        if x1 >=  x2 + SnakeSize and x1 <= x2 + SnakeSize:
            if y1 >= y2 + SnakeSize and y1 <= y2 + SnakeSize:
                return True
        
    def run(self):    #game loop
        running = True
    
        while running:
        #block_x += 1
        #draw_block()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key  == K_ESCAPE:
                        running = False
            
                    if event.key == K_w:
                        self.snake.move_up()
                    if event.key == K_s:
                        self.snake.move_down()
                    if event.key == K_a:
                        self.snake.move_left()
                    if event.key == K_d:
                        self.snake.move_right()
                elif event.type == QUIT:
                    running = False
            self.play()
            time.sleep(.1) #this will say how fast it will go across the screen.
            pass
    
if __name__ == "__main__":
    game = Game()
    game.run()