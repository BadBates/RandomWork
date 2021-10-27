import pygame
from pygame.locals import *
import time

if __name__ == "__main__":
    pygame.init()
    
    surface = pygame.display.set_mode((1000,500))
    surface.fill((110,110,5))
    pygame.display.flip()
    
    #time.sleep(5) this just makes the screen diseaper after the time declared.
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
            
