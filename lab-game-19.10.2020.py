# Задиран Б02-922 
import pygame
from pygame.draw import *
from random import randint
from random import random
import random
import math

#Описание глобальных переменных
#параметры для описания мишеней типа круг

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

#параметры для описания мишеней типа квадрат

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

print("Введите ваш ник: ")
name = input()
pygame.init()
score = 0
FPS = 100
screen = pygame.display.set_mode((900, 700))

#Цвета для мишеней
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, MAGENTA, CYAN]



# основная логика программы
def new_square():
    '''
    создание новой мишени типа квадрат
    :return: отсутвует
    '''
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
    if randint(0,1) == 1:
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
    flag_exist2[i] = True


def new_ball():
    '''
    Создание новой мишени типа круг
    :return: отсутвует
    '''
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
    '''
    Обработка клика по экрану
    :param event: объект pygame.event
    :return: отсутвует
    '''
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
    '''
    вывод очков
    :return:  отсутвует
    '''
    global score
    text = "Score: "
    text += str(score)
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render(text, 0, (0, 0, 0))
    rect(screen, (255, 255, 255), (0, 610, 500, 200) )
    screen.blit(text1, (50,650))

def print_time(time):
    '''
    :time: время полученное в теле программы
    вывод времени на экран
    :return: отсутвует
    '''
    text = "Time: "
    text += str(int((60000-time)/1000))
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render(text, 0, (0, 0, 0))
    rect(screen, (255, 255, 255), (400, 610, 500, 200))
    screen.blit(text1, (600, 650))

pygame.display.update()
clock = pygame.time.Clock()
finished = False


print_score()
while not finished:
    clock.tick(FPS)
    new_square()
    new_ball()
    if pygame.time.get_ticks() > 60000:
        finished = True
    for j in range(200):

        if j % 100 == 0:
            print_time(pygame.time.get_ticks())

        for k in range(4):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                    pygame.quit()
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
            #обработка соударений
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
                rect(screen, color2[k], (x2[k] - r2[k], y2[k] - r2[k], 2*r2[k], 2*r2[k]) )
            if y2[k] > 600 -r2[k]:
                rect(screen, (0, 0, 0), (x2[k] - r2[k], y2[k] - r2[k], 2 * r2[k], 2 * r2[k]))
                y2[k] = 600 -r2[k]-1
                vy2[k] = -vy2[k]*0.9
                rect(screen, color2[k], (x2[k] - r2[k], y2[k] - r2[k],2*r2[k], 2*r2[k]) )
    pygame.display.update()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            finished = True
    f1 = pygame.font.Font(None, 80)
    text = "GAME OVER YOUR SCORE: "
    text += str(score)
    text1 = f1.render(text, 0, (255, 255, 255))
    screen.blit(text1, (50, 300))
    pygame.display.update()

pygame.quit()
f = open("scorelist.txt", "a")
f.close()
f = open("scorelist.txt", "r")

string = f.read()
y = string.split()
f.close()
names = []
scores = []
k = 0
for i in y:
    if k % 2 == 0:
        names.append(i)
    else:
        scores.append(int(i))
    k += 1
names.append(name)
scores.append(score)
amount = len(names)
if amount > 6:
    amount = 6
for i in range(amount):
    for j in range(amount-i-1):
        if scores[j] < scores[j+1]:
            scores[j], scores[j+1] = scores[j+1],scores[j]
            names[j], names[j+1] = names[j+1], names[j]
f = open("scorelist.txt", "w")
if amount > 5:
    amount = 5
for i in range (amount):
    f.write(names[i]+" "+ str(scores[i])+'\n')

f.close()
