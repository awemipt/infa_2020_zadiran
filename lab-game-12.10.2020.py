# Задиран Б02-922 
import pygame
from pygame.draw import *
from random import randint
from random import random
import random
import math
x = list([0, 0, 0, 0])
y = list([0, 0, 0, 0])
r = list([0, 0, 0, 0])
vx = list([0, 0, 0, 0])
vy = list([0, 0, 0, 0])
flag_exist  = list ([True, True, True, True])
color = list([(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)])
i = 0
flag_movement = False
flag_del = False
x2 = list([0, 0, 0, 0])
y2 = list([0, 0, 0, 0])
r2 = list([0, 0, 0, 0])
vx2 = list([0.0, 0.0, 0.0, 0.0])
vy2 = list([0.0, 0.0, 0.0, 0.0])
x2_0 = list([1,1,1,1])
y2_0 = list([1,1,1,1])
flag_exist2  = list ([True, True, True, True])
color2 = list([(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)])
i2 = 0
flag_movement2 = False
flag_del2 = False



pygame.init()
score = 0
FPS = 100
screen = pygame.display.set_mode((900, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, MAGENTA, CYAN]

def new_square():
    global x2, y2, r2, i2,flag_del2,flag_movement2, color2, vx2, vy2
    flag_in2 = True
    i2 += 1
    if i2 == 4:
        i2 = 0
        flag_del2 = True
        flag_movement2 = True
    if flag_del:
        rect(screen, (0, 0, 0), (x2[i2]-r2[i2], y2[i2]-r2[i2],2*r2[i2], 2*r2[i2]))

    r2[i2] = randint(40, 50)
    x2[i2] = randint(100+r2[i2], 700-r2[i2])
    y2[i2] = randint(100+r2[i2], 300-r2[i2])
    if randint(0,1):
        vx2[i2] = random.uniform(1,2)
    else:
        vx2[i2] = -random.uniform(1,2)
    vy2[i2] = random.uniform(0,5)
    while flag_in2:
        flag_in2 = False
        for j in range(4):
            if i2 != j:
                if (x2[i2] - x2[j]) ** 2 + (y2[i2] - y2[j]) ** 2 <= (r2[i2] + r2[j]) ** 2:
                    flag_in2 = True
                    x2[i2] = randint(100, 700)
                    y2[i2] = randint(100, 500)
                    r2[i2] = randint(20, 30)
    color2[i2] = COLORS[randint(0, 4)]
    rect(screen, color2[i2], (x2[i2]-r2[i2], y2[i2]-r2[i2],2*r2[i2],2*r2[i2]))
    flag_exist2[i] = True


def new_ball():
    global x, y, r, i, flag_del, flag_movement, color,vx,vy
    flag_in = True
    i += 1
    if i == 4:
        i = 0
        flag_del = True
        flag_movement  = True
    if flag_del:
        circle(screen, (0, 0, 0), (x[i], y[i]), r[i])
    x[i] = randint(100, 700)
    y[i] = randint(100, 500)
    r[i] = randint(30, 50)
    vx[i] = random.uniform(-3, 3)
    vy[i] = random.uniform(-3, 3)
    while flag_in:
        flag_in = False
        for j in range(4):
            if i != j:
                if (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 <= (r[i] + r[j]) ** 2:
                    flag_in = True
                    x[i] = randint(100, 700)
                    y[i] = randint(100, 500)
                    r[i] = randint(10, 30)
    color[i] = COLORS[randint(0, 4)]
    circle(screen, color[i], (x[i], y[i]), r[i])
    flag_exist[i] = True


def click(event):
    global x, y, r, vx, vy
    global score
    global x2, y2, r2, vx2, vy2
    for j in range(4):
        if (event.pos[0] - x[j]) ** 2 + (event.pos[1] - y[j]) ** 2 <= r[j] ** 2:
            score += 1
            circle(screen, (0, 0, 0), (x[j], y[j]), r[j])
            vx[j] = 0
            vy[j] = 0
            flag_exist[j] = False
            print_score()
        if abs(event.pos[0]-x2[j]) <= r2[j] and abs(event.pos[1]-y2[j]) <= r2[j]:
            score += 2
            rect(screen, (0, 0, 0), (x2[j]-r2[j], y2[j]-r2[j], 2*r2[j], 2*r2[j]))
            vx2[j] = 0
            vy2[j] = 0
            flag_exist2[j] = False
            print_score()

def print_score():
    global score
    text = "Score: "
    text += str(score)
    print(text)



pygame.display.update()
clock = pygame.time.Clock()
finished = False
print_score()
while not finished:
    clock.tick(FPS)


    for j in range(200):
        for k in range(4):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click(event)
            if flag_exist[k]:
                circle(screen, (0, 0, 0), (x[k], y[k]), r[k])
                x[k] += vx[k]
                y[k] += vy[k]
                x[k] = round(x[k])
                y[k] = round(y[k])
                circle(screen, color[k], (x[k], y[k]), r[k])

            if flag_exist2[k]:
                rect(screen, (0, 0, 0), (x2[k] - r2[k], y2[k] - r2[k], 2*r2[k], 2*r2[k]))
                x2[k] = round(vx2[k]+x2[k])
                y2[k] = round(vy2[k]+y2[k])
                vy2[k] += 0.05
                rect(screen, color2[k], (x2[k] - r2[k], y2[k] - r2[k],2*r2[k], 2*r2[k]) )


            pygame.display.update()
            if x[k] > 900 - r[k]:
                circle(screen, (0,0,0), (x[k], y[k]), r[k])
                vx[k] = - vx[k]
                x[k] = 900 -r[k] -1
                circle(screen, color[k], (x[k], y[k]), r[k])
            if x[k] < r[k]:
                circle(screen, (0, 0, 0), (x[k], y[k]), r[k])
                vx[k] = - vx[k]
                x[k] = r[k]+1
                circle(screen, color[k], (x[k], y[k]), r[k])
            if y[k] < 0+r[k]:
                circle(screen, (0, 0, 0), (x[k], y[k]), r[k])
                vy[k] = -vy[k]
                y[k] = r[k]+1
                circle(screen, color[k], (x[k], y[k]), r[k])
            if y[k] > 600 - r[k]:
                circle(screen, (0, 0, 0), (x[k], y[k]), r[k])
                vy[k] = -vy[k]
                y[k] = 600 - r[k] -1
                circle(screen, color[k], (x[k], y[k]), r[k])
            if x2[k] > 900 - r2[k]:
                rect(screen, (0, 0, 0), (x2[k] - r2[k], y2[k] - r2[k], 2 * r2[k], 2 * r2[k]))
                vx2[k] = -vx2[k]
                x2[k] = 900 -r2[k] -1
                rect(screen, color2[k], (x2[k] - r2[k], y2[k] - r2[k],2*r2[k], 2*r2[k]) )
            if x2[k] < 0+r2[k]:
                rect(screen, (0, 0, 0), (x2[k] - r2[k], y2[k] - r2[k], 2 * r2[k], 2 * r2[k]))
                vx2[k] = -vx2[k]
                x2[k] = r2[k]+1
                rect(screen, color2[k], (x2[k] - r2[k], y2[k] - r2[k],2*r2[k], 2*r2[k]) )
            if y2[k] < 0 + r2[k]:
                rect(screen, (0, 0, 0), (x2[k] - r2[k], y2[k] - r2[k], 2 * r2[k], 2 * r2[k]))
                y2[k] = r2[k]+1
                vy2[k] = -vy2[k]*0.9
                rect(screen, color2[k], (x2[k] - r2[k], y2[k] - r2[k],2*r2[k], 2*r2[k]) )
            if y2[k] > 600 -r2[k]:
                rect(screen, (0, 0, 0), (x2[k] - r2[k], y2[k] - r2[k], 2 * r2[k], 2 * r2[k]))
                y2[k] = 600 -r2[k]-1
                vy2[k] = -vy2[k]*0.9
                rect(screen, color2[k], (x2[k] - r2[k], y2[k] - r2[k],2*r2[k], 2*r2[k]) )
    new_square()

    new_ball()
    pygame.display.update()


pygame.quit()
