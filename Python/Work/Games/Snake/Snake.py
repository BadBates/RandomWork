import pygame
from pygame.locals import *
import time
import random
       
class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((10,10))
        self.surface.fill((110,110,5))
        self.snake = Snake(self.surface)
        self.snake.draw()
    def run(self):
        pass

def draw_block():
    surface.fill((110,110,5))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()
    
def draw_food():
    surface.fill((110,110,5))
    surface.flit(flock, (flock_x, flock_y))
    pygame.display.flip()
    
if __name__ == "__main__":
    pygame.init()
    
    #window
    surface = pygame.display.set_mode((1000,1000))
    surface.fill((110,110,5))
    #player display
    block = pygame.image.load("Snake.png").convert()
    block_x = 100
    block_y = 100
    surface.blit(block,(block_x,block_y))
    pygame.display.flip()
    #food display
    flock= pygame.image.load("Mouse.png").convert()
    flock_x = random.randint(0,1000)
    flock_y = random.randint(0,1000)
    
    
    running = True
    
    while running:
        block_x += 1
        draw_block()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key  == K_ESCAPE:
                    running = False
            
                if event.key == K_w:
                    block_y -= 10
                    draw_block()
                if event.key == K_s:
                    block_y += 10
                    draw_block()
                if event.key == K_a:
                    block_x -= 10
                    draw_block()
                if event.key == K_d:
                    block_x += 10
                    draw_block()
            elif event.type == QUIT:
                running = False
                
                
            