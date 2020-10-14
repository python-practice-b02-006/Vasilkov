import pygame
import numpy as np
import datetime


screen = pygame.display.set_mode([1000,800])
clock = pygame.time.Clock()


def u(x, y):
    pygame.draw.polygon(screen, (255, 0, 0), [(x-30-10, y), (x-30, y-10),
                                (x+30, y-10), (x+30+10, y), (x+30, y+10), (x-30, y+10)])


def ru(x, y):
    pygame.draw.polygon(screen, (255, 0, 0), [(x, y - 30 - 10), (x - 10, y - 30),
                                (x - 10, y + 30), ( x, y + 30 + 10), (x+10, y + 30), (x+10, y - 30)])


def sqs(x, y):
    pygame.draw.rect(screen, (255, 0, 0), [x-20, y-50, 20 ,20])
    pygame.draw.rect(screen, (255, 0, 0), [x - 20, y+30, 20, 20])


def one(x, y):
    ru(x+46, y+46)
    ru(x+46, y-46)


def two(x, y):
    u(x, y)
    ru(x+46, y-46)
    u(x, y-92)
    ru(x-46, y+46)
    u(x, y+92)


def three(x, y):
    u(x, y)
    ru(x + 46, y - 46)
    u(x, y - 92)
    ru(x + 46, y + 46)
    u(x, y + 92)


def four(x, y):
    u(x, y)
    ru(x - 46, y - 46)
    ru(x + 46, y - 46)
    ru(x + 46, y + 46)


def five(x, y):
    u(x, y)
    ru(x - 46, y - 46)
    u(x, y - 92)
    ru(x + 46, y + 46)
    u(x, y + 92)


def six(x, y):
    u(x, y)
    ru(x - 46, y - 46)
    u(x, y - 92)
    ru(x + 46, y + 46)
    ru(x - 46, y + 46)
    u(x, y + 92)


def seven(x, y):
    u(x, y - 92)
    one(x, y)


def eight(x, y):
    six(x, y)
    ru(x+46, y-46)


def nine(x, y):
    five(x, y)
    ru(x+46, y-46)


def zero(x, y):
    seven(x, y)
    one(x-92, y)
    u(x, y+92)


def cclocks (T, x, y):

    t = T % 10
    if t == 0:
        zero(x, y)
    if t == 1:
       one(x, y)
    if t == 2:
        two(x, y)
    if t == 3:
        three(x, y)
    if t == 4:
        four(x, y)
    if t == 5:
        five(x, y)
    if t == 6:
        six(x, y)
    if t == 7:
        seven(x, y)
    if t == 8:
        eight(x, y)
    if t == 9:
        nine(x, y)
    z = (T-T % 10)/10
    if z == 0:
        zero(x-120, y)
        return
    if z == 1:
       one(x-120, y)
       return
    if z == 2:
        two(x-120, y)
        return
    if z == 3:
        three(x-120, y)
        return
    if z == 4:
        four(x-120, y)
        return
    if z == 5:
        five(x-120, y)
        return
    if z == 6:
        six(x-120, y)
        return
    if z == 7:
        seven(x-120, y)
        return
    if z == 8:
        eight(x-120 ,y)
        return
    if z == 9:
        nine(x-120, y)
        return


done = False
pygame.display.set_caption("wtf")

while not done:

    clock.tick(1)
    Now = datetime.datetime.now()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((0, 0, 0))
    if Now.second % 2 == 0:
        sqs(650, 400)
        sqs(350, 400)
    cclocks(Now.second, 850, 400)

    cclocks(Now.minute, 550, 400)
    cclocks(Now.hour, 250, 400)
    pygame.display.flip()

pygame.quit()
