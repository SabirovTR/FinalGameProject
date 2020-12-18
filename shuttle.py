import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 1000))
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
screen.fill (BLACK)

def shuttle (x=150,y=375,l=450,h=50):
    def benzobak ():
        rect (screen, GREY,(1.1*x,0.9*y, 1.25*l, h+0.2*y), width = 0)
        ellipse(screen, GREY, ((1.1*x+1.25*l)*0.83, 0.9*y, 2*0.17*(1.1*x+1.25*l), h+0.2*y))
    benzobak()
    def corpus ():
        rect (screen, WHITE,(x, y, l, h ))
        rect (screen, WHITE, (0.73*x, 0.93*y, 0.27*x, h+2*0.07*y))
        ellipse(screen, WHITE, ((x+l)*0.83, y, 2*0.17*(x+l), h), width = 0)
    corpus()
    def bokovushki():
        rect (screen, WHITE, ((x+l)/2, y-h, 0.05*l, 3*h ))
        rect (screen, WHITE, (x, y - 1.66*h, 1.2*l, 0.66*h))
        ellipse(screen, WHITE, (0.83*(x+1.2*l), y-1.66*h,2*0.17*(x+1.2*l), 0.66*h))
        rect (screen, WHITE, (x, y + 2*h, 1.2*l, 0.66*h))
        ellipse(screen, WHITE, (0.83*(x+1.2*l), y+2*h,2*0.17*(x+1.2*l), 0.66*h ))
    bokovushki()
    
shuttle ()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
