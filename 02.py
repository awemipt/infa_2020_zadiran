#Задиран Б02-922 2ая задача
import  math
import pygame
from pygame.draw import *
from pygame.math import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((720, 480))


yellow = (255, 255, 0)
red = (235, 47, 68)
black = (0, 0, 0)
white = (254, 249, 249)
green = (15, 83, 14)
pink = (249, 194, 194)
orange = (181, 98, 17)
light_green = (14, 147, 37)
brown = (147, 107, 14)
blue = (158, 234, 245, 0.97)
blue_chill = (14, 147, 145)

rect(screen, blue, (0, 0, 720, 240))
rect(screen, light_green, (0, 240, 720, 240))


def tree(x, y, scale=1):
    x1 = int(x+16*scale)
    y1 = int(y-2*50*scale)
    r = 34
    rect(screen, black, (x, y, int(16*scale), int(70*scale)))
    circle(screen, green, (int((x1 + x)/2), y1), int(r*scale))
    circle(screen, black, (int((x1 + x)/2), y1), int(r*scale), 1)
    circle(screen, green, (int((x1 + x)/2+(r+4)*scale), int(y1+r*scale)), int(r*scale))
    circle(screen, green, (int((x1 + x)/2-(r+4)*scale), int(y1+(r+2)*scale)), int(r*scale))
    circle(screen, black, (int((x1 + x)/2+(r+4)*scale), int(y1+r*scale)), int(r*scale),1)
    circle(screen, black, (int((x1 + x)/2-(r+4)*scale), int(y1+(r+2)*scale)), int(r*scale),1)
    circle(screen, green, (int((x1 + x) / 2), int(y1 + (2*r-16) * scale)), int(r * scale))
    circle(screen, black, (int((x1 + x) / 2), int(y1 + (2*r-16) * scale)), int(r * scale),1)
    circle(screen, green, (int((x1 + x) / 2-(r-7)*scale), int(y1 + (2*r+10) * scale)), int(r * scale))
    circle(screen, black, (int((x1 + x) / 2-(r-7)*scale), int(y1 + (2*r+10) * scale)), int(r * scale),1)
    circle(screen, green, (int((x1 + x) / 2+(r-10)*scale), int(y1 + (2*r+15) * scale)), int(r * scale))
    circle(screen, black, (int((x1 + x) / 2+(r-10)*scale), int(y1 + (2*r+15) * scale)), int(r * scale),1)
    pass


def cloud(x, y, scale=1):
    r = 30*scale
    for i in range(4):
        circle(screen, white, (int(x+r*i*1.15), int(y)), int(r))
        circle(screen, black, (int(x+r*i*1.15), int(y)), int(r), 1)

    for i in range(2):
        circle(screen, white, (int(x-r*i*1.2+r*2.3), int(y-r*0.9)), int(r))
        circle(screen, black, (int(x-r*i*1.2+r*2.3), int(y-r*0.9)), int(r), 1)
    pass


def house(x, y, scale=1):
    width = int(160*scale)
    height = int(0.75*width)
    x1 = x + width
    y2 = int(y + height/3)
    x2 = int(x + width/3)

    polygon(screen, red, [(x, y), (int((x+x1)/2), int(y-height*0.7)), (x1, y), (x, y)])
    polygon(screen, black, [(x, y), (int((x+x1)/2), int(y-height*0.7)), (x1, y), (x, y)], 1)
    rect(screen, brown, (x, y, width, height))
    rect(screen, black, (x, y, width, height), 1)
    rect(screen, blue_chill, (x2, y2, int(width / 3), int(height / 3)))
    rect(screen, orange, (x2, y2, int(width / 3), int(height / 3)), 1)
    pass


def sun(x, y, scale=1):
    r = 37
    R = 40
    v = []
    N = 20
    for i in range(N):
        y1 = int(y - r*math.sin(i*2*math.pi/(N-1)))
        y2 = int(y - R*math.sin(i*2*math.pi/(N-1) + math.pi/(N-1)))
        x1 = int(x + r*math.cos(i*2*math.pi/(N-1)))
        x2 = int(x + R*math.cos(i*2*math.pi/(N-1) + math.pi/(N-1)))
        v.append((x1, y1))
        v.append((x2, y2))
    polygon(screen, pink, v)
    polygon(screen, black, v, 1)
    pass


house(100, 210)
cloud(400, 100)
sun(650, 80)

tree(550, 255)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
