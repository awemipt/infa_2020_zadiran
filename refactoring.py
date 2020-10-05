# Б02-922 Задиран Николай рефакторинг

# Б02-010 Сапаев Руслан задача 2 лабораторная 4

import pygame
from pygame.draw import *


def flower(screen, surface, x, y, angle, zoom):
    '''
    Всмпомогательная фунция для bush рисует цветы на кусте
    :param screen: поверхность для рисования - pygame.display
    :param surface: типовой рисунок цветка - pygame.surface
    :param x: координата x - int
    :param y: координата у - int
    :param angle: угол поворота - int
    :param zoom: маштабный коэффицент - float

    '''
    flower_rot = pygame.transform.rotozoom(surface, angle, zoom)
    flower_rot.set_colorkey((0, 0, 0))
    screen.blit(flower_rot, (x, y))


def Bush(screen, x, y, zoom, bush_color, flower_color, border_color):
    '''
    Функция рисует куст с цветами на нем
    :param screen: поверхность для рисования - pygame.display
    :param x: координата x куста - int
    :param y: координата у кустsG, B) - (int, int, int)
    :param border_color: цвет границы (R, G, B) - (int, int, int)
    :return: отсутсвует
    '''
    flower_surf = pygame.Surface((int(70 * zoom), int(35 * zoom)))
    flower_surf.fill((0, 0, 0))
    ellipse(flower_surf, flower_color, ( int(17 * zoom) , 0 ,  int(25 * zoom), int(13 * zoom)))
    ellipse(flower_surf, border_color, ( int(17 * zoom),int( 0 * zoom), int(25 * zoom), int(13 * zoom)), 1)
    ellipse(flower_surf, flower_color, (int(5 * zoom),int( 4 * zoom), int(25 * zoom), int(13 * zoom)))
    ellipse(flower_surf, border_color, (int(5 * zoom),int( 4 * zoom), int(25 * zoom), int(13 * zoom)), 1)
    ellipse(flower_surf, flower_color, (int(32 * zoom),int( 3 * zoom), int(25 * zoom), int(13 * zoom)))
    ellipse(flower_surf, border_color, (int(32 * zoom),int( 3 * zoom), int(25 * zoom), int(13 * zoom)), 1)
    ellipse(flower_surf, (255, 255, 0), (int(21 * zoom), int(11 * zoom), int(25 * zoom), int(13 * zoom)))
    ellipse(flower_surf, flower_color, (int(0 * zoom), int(13 * zoom), int(25 * zoom), int(13 * zoom)))
    ellipse(flower_surf, border_color, (int(0 * zoom), int(13 * zoom), int(25 * zoom), int(13 * zoom)), 1)
    ellipse(flower_surf, flower_color, (int(39 * zoom),int( 9 * zoom), int(25 * zoom), int(13 * zoom)))
    ellipse(flower_surf, border_color, (int(39 * zoom),int( 9 * zoom), int(25 * zoom), int(13 * zoom)), 1)
    ellipse(flower_surf, flower_color, (int(13 * zoom), int(17 * zoom), int(25 * zoom), int(13 * zoom)))
    ellipse(flower_surf, border_color, (int(13 * zoom), int(17 * zoom), int(25 * zoom), int(13 * zoom)), 1)
    ellipse(flower_surf, flower_color, (int(32 * zoom), int(18 * zoom), int(25 * zoom), int(13 * zoom)))
    ellipse(flower_surf, border_color, (int(32 * zoom), int(18 * zoom), int(25 * zoom), int(13 * zoom)), 1)
    circle(screen, bush_color, (x, y), int(100 * zoom))
    flower(screen, flower_surf, x - int(80*zoom), y - int(30*zoom), 15, 0.8)
    flower(screen, flower_surf, x - int(10*zoom), y - int(70*zoom), 0, 0.8)
    flower(screen, flower_surf, x - int(10*zoom), y - int(20*zoom), -15, 0.8)
    flower(screen, flower_surf, x - int(60*zoom), y + int(20*zoom), 8, 0.8)
    flower(screen, flower_surf, x - int(80*zoom), y - int(60*zoom), 15, 0.6)
    flower(screen, flower_surf, x + int(50*zoom), y - int(10*zoom), -70, 0.8)


def Body(screen, x, y, zoom, color_body):
    '''
    Вспомогательная функция для Kozel рисует тело козла
    :param screen: поверхность для рисования - pygame.display
    :param x: координата x куста - int
    :param y: координата у куста - int
    :param zoom: маштабный коэффицент - float
    :param color_body: цвет тела козла (R, G, B) - (int, int, int)
    :return: отсутствует
    '''
    ellipse(screen, color_body, (x - int(68 * zoom), y - int(32 * zoom), int(140 * zoom), int(64 * zoom)))
    ellipse(screen, color_body, (x + int(38 * zoom), y - int(120 * zoom), int(40 * zoom), int(105 * zoom)))
    ellipse(screen, color_body, (x + int(43 * zoom), y - int(140 * zoom), int(50 * zoom), int(32 * zoom)))


def Eyes(screen: pygame.display, x, y, zoom, color_body, color_eye_1, color_eye_2):
    '''
    Вспомогательная функция для Kozel рисует глаза козла
    :param screen: поверхность для рисования - pygame.display
    :param x: координата x куста - int
    :param y: координата у куста - int
    :param zoom: маштабный коэффицент - float
    :param color_body: цвет (R, G, B) - (int, int, int)
    :param color_eye_1: цвет первого глаза (R, G, B) - (int, int, int)
    :param color_eye_2: цвет второго глаза (R, G, B) - (int, int, int)
    :return: отсутствует
    '''
    ellipse(screen, color_eye_2, (x + int(52 * zoom), y - int(138 * zoom), int(24 * zoom), int(20 * zoom)))
    ellipse(screen, color_eye_1, (x + int(65 * zoom), y - int(133 * zoom), int(10 * zoom),int( 8 * zoom)))
    glasik = pygame.Surface((int(12 * zoom),int( 6 * zoom)), pygame.SRCALPHA)
    ellipse(glasik, color_body, (0, 0, int(11 * zoom), int(11 * zoom)))
    glasik_rot = pygame.transform.rotate(glasik, -30)
    screen.blit(glasik_rot, (x + int(58 * zoom), y - int(138 * zoom)))


def Horns(screen, x, y, zoom, color_body):
    '''
    Вспомогаительная функция для Kozel рисует рога козла
    :param screen: поверхность для рисования - pygame.display
    :param x: координата x куста - int
    :param y: координата у куста - int
    :param zoom: маштабный коэффицент - float
    :param color_body: цвет рогов (R, G, B) - (int, int, int)
    :return: отсутсвует
    '''
    polygon(screen, color_body, [(x, y), (x - int(10 * zoom), y - int(10 * zoom)),
                                 (x - int(15 * zoom), y - int(20 * zoom)), (x - int(18 * zoom), y - int(30 * zoom)),
                                 (x - int(10 * zoom), y - int(20 * zoom)), (x, y - int(10 * zoom)),
                                 (x +int( 5 * zoom), y - int(11 * zoom))])
    polygon(screen, color_body, [(x + int(14 * zoom), y -int( 4 * zoom)), (x +int( 4 * zoom), y - int(14 * zoom)),
                                 (x -int( 1 * zoom), y - int(24 * zoom)), (x -int( 4 * zoom), y - int(34 * zoom)),
                                 (x +int( 4 * zoom), y - int(24 * zoom)), (x + int(14 * zoom), y - int(14 * zoom)),
                                 (x + int(19 * zoom), y -int( 4 * zoom))])


def Legs(screen, x, y, zoom, color_body):
    '''
    Вспомогательная функция рисует ноги козла
    :param screen: поверхность для рисования - pygame.display
    :param x: координата x куста - int
    :param y: координата у куста - int
    :param zoom: маштабный коэффицент - float
    :param color_body: цвет ног (R, G, B) - (int, int, int)
    :return: отсутсвует
    '''
    ellipse(screen, color_body, (x - int(10 * zoom), y + int(20 * zoom), int(20 * zoom), int(48 * zoom)))
    ellipse(screen, color_body, (x - int(10 * zoom), y - int(25 * zoom), int(20 * zoom), int(50 * zoom)))
    ellipse(screen, color_body, (x -int( 5 * zoom), y + int(65 * zoom), int(20 * zoom), int(15 * zoom)))


def Kozel(screen, x, y, zoom, color_body, color_eye_1, color_eye_2):
    '''
    Рисует козла на координате x,y за размер отвечат параметр zoom, сolor_body color_eve_1 color_eve_2 цвета теа и глаз
    :param screen: поверхность для рисования - pygame.display
    :param x: координата x куста - int
    :param y: координата у куста - int
    :param zoom: маштабный коэффицент - float
    :param color_body: цвет тела (R, G, B) - (int, int, int)
    :param color_eye_1: цвет первого глаза (R, G, B) - (int, int, int)
    :param color_eye_2: цвет второго глаза (R, G, B) - (int, int, int)
    :return: отсутствует
   '''
    Body(screen, x, y, zoom, color_body)
    Eyes(screen, x, y, zoom, color_body, color_eye_1, color_eye_2)
    Horns(screen, x + int(50 * zoom), y - int(130 * zoom), zoom / 1.5, color_body)
    Legs(screen, x + int(45 * zoom), y + int(38 * zoom), zoom, color_body)
    Legs(screen, x - int(25 * zoom), y + int(38 * zoom), zoom, color_body)
    Legs(screen, x - int(51 * zoom), y + int(13 * zoom), zoom, color_body)
    Legs(screen, x + int(23 * zoom), y + int(13 * zoom), zoom, color_body)


pygame.init()

pixels_x = 600
pixels_y = 900
FPS = 30
Screen = pygame.display.set_mode((pixels_x, pixels_y))

Screen.fill((170, 220, 135))
rect(Screen, (175, 220, 230), (0, 0, pixels_x, 400))


polygon(Screen, ((180, 180, 180)), [(-1, 280), (70, 90), (125, 220), (205, 120),
                                    (360, 360), (470, 110), (500, 160), (600, 30),
                                    (600, 530), (345, 530), (340, 525), (340, 480),
                                    (335, 470), (330, 460), (326, 455), (320, 450),
                                    (320, 450), (130, 450), (75, 460), (55, 460),
                                    (30, 460), (-1, 480)])


polygon(Screen, ((0, 0, 0)), [(-1, 280), (70, 90), (125, 220), (205, 120),
                              (360, 360), (470, 110), (500, 160), (600, 30),
                              (600, 530), (345, 530), (340, 525), (340, 480),
                              (335, 470), (330, 460), (326, 455), (320, 450),
                              (320, 450), (130, 450), (75, 460), (55, 460),
                              (30, 460), (-1, 480)], 1)



Bush(Screen, 460, 650, 0.3, (110, 200, 60), (255, 255, 255), (180, 180, 180))
Bush(Screen, 100, 650, 0.5, (110, 200, 60), (255, 255, 255), (180, 180, 180))
Bush(Screen, 200, 400, 0.6, (110, 200, 60), (255, 255, 255), (180, 180, 180))
Bush(Screen, 300, 500, 0.8, (110, 200, 60), (255, 255, 255), (180, 180, 180))

Kozel(Screen, 200, 500, 0.8, (255, 255, 255), (0, 0, 0), (230, 130, 255))
Kozel(Screen, 700, 400, 0.6, (255, 255, 255), (0, 0, 0), (230, 130, 255))
Kozel(Screen, 400, 600, 0.4, (255, 255, 255), (0, 0, 0), (230, 130, 255))
Kozel(Screen, 150, 450, 0.4, (255, 255, 255), (0, 0, 0), (230, 130, 255))
Kozel(Screen, 50, 900, 2, (255, 255, 255), (0, 0, 0), (230, 130, 255))


pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
