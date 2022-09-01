import pygame
import sys
import random

pygame.init()
width = 1600
height = 900
black = [0,0,0]
white = [255,255,255]
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
yellow = [255,255,0]
cyan = [0,255,255]
magenta = [255,0,255]

pygame.display.set_caption('DVD.py')
display = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
clock = pygame.time.Clock()

class DVD:
    def __init__(DVD,x,y,sx,sy,spd):
        DVD.x = x
        DVD.y = y
        DVD.sx = sx
        DVD.sy = sy
        DVD.spd = spd
        DVD.d = 1
        DVD.clr = white
        DVD.sprite = pygame.image.load("DVD.png").convert_alpha()
    def clrchng(DVD):
        rng = random.randint(1,7)
        if rng == 1:
            if DVD.clr == white:
                DVD.clrchng()
            else:
                DVD.clr = white
        if rng == 2:
            if DVD.clr == red:
                DVD.clrchng()
            else:
                DVD.clr = red
        if rng == 3:
            if DVD.clr == green:
                DVD.clrchng()
            else:
                DVD.clr = green
        if rng == 4:
            if DVD.clr == blue:
                DVD.clrchng()
            else:
                DVD.clr = blue
        if rng == 5:
            if DVD.clr == yellow:
                DVD.clrchng()
            else:
                DVD.clr = yellow
        if rng == 6:
            if DVD.clr == cyan:
                DVD.clrchng()
            else:
                DVD.clr = cyan
        if rng == 7:
            if DVD.clr == magenta:
                DVD.clrchng()
            else:
                DVD.clr = magenta

    def move(DVD):
        if DVD.x - DVD.spd < 0:
            if DVD.d == 4:
                DVD.d = 2
                DVD.clrchng()
            if DVD.d == 3:
                DVD.d = 1
                DVD.clrchng()
        if DVD.x + DVD.sx + DVD.spd > width:
            if DVD.d == 2:
                DVD.d = 4
                DVD.clrchng()
            if DVD.d == 1:
                DVD.d = 3
                DVD.clrchng()
        if DVD.y - DVD.spd < 0:
            if DVD.d == 4:
                DVD.d = 3
                DVD.clrchng()
            if DVD.d == 2:
                DVD.d = 1
                DVD.clrchng()
        if DVD.y + DVD.sy + DVD.spd > height:
            if DVD.d == 3:
                DVD.d = 4
                DVD.clrchng()
            if DVD.d == 1:
                DVD.d = 2
                DVD.clrchng()

        if DVD.d == 1:
            DVD.x = DVD.x + DVD.spd
            DVD.y = DVD.y + DVD.spd
        if DVD.d == 2:
            DVD.x = DVD.x + DVD.spd
            DVD.y = DVD.y - DVD.spd
        if DVD.d == 3:
            DVD.x = DVD.x - DVD.spd
            DVD.y = DVD.y + DVD.spd
        if DVD.d == 4:
            DVD.x = DVD.x - DVD.spd
            DVD.y = DVD.y - DVD.spd
    def display(DVD):
        pygame.draw.rect(display,DVD.clr,(DVD.x,DVD.y,DVD.sx,DVD.sy))
        display.blit(DVD.sprite,(DVD.x,DVD.y))

dvd = DVD(678,395,244,110,5)
while True:
    clock.tick(60)
    pygame.display.update()
    display.fill(black)

    dvd.display()
    dvd.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
               pygame.quit()
               sys.exit()