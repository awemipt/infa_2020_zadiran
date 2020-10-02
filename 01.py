#Задиран Б02-922 1ая задача
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))


yellow = (255, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

rect(screen, white, (0, 0, 400, 400))
circle(screen, yellow, (200, 200), 100)
circle(screen, black, (200, 200), 100, 1)
circle(screen, red, (165, 170), 20)
circle(screen, black, (165, 170), 20, 1)
circle(screen, black, (165, 170), 6)
circle(screen, red, (235, 170), 14)
circle(screen, black, (235, 170), 14, 1)
circle(screen, black, (235, 170), 6)
rect(screen, black, (155, 240, 90, 20))
polygon(screen, black, [(181, 158), (131, 133), (133, 129), (193, 159), (191, 163), (181, 158)])
polygon(screen, black, [(231, 156), (251, 151), (249, 147), (221, 154), (223, 158), (231, 156)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
