import pygame
from pygame.locals import *
import time
import random
       
class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("Snake.png").convert()
        self.x = 100
        self.y = 100
        self.direction = '' #this function is to help determine which way it will continue to move.
    def draw(self):
        self.parent_screen.fill((110,110,5)) #color assignment
        self.parent_screen.blit(self.block,(self.x,self.y))
        pygame.display.flip()
        
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
        if self.direction == 'up':
           self.y -= 10
        if self.direction == 'down':
           self.y += 10
        if self.direction == 'left':
           self.x -= 10
        if self.direction == 'right':
           self.x += 10
        self.draw()

class Mouse:
    def __init__(self, parent_screen):
        pass
        
class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1820,980))#screen size
        self.snake = Snake(self.surface)
        self.snake.draw()
        
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
            self.snake.walk()
            time.sleep(.1) #this will say how fast it will go across the screen.
            pass
    
if __name__ == "__main__":
    game = Game()
    game.run()