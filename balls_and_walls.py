import numpy as np
import pygame as pg
from random import randint, gauss

pg.init()
pg.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SCREEN_SIZE = (800, 600)

screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("Khiryanov cannon")

def rand_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


class Ball():

    def __init__(self, coord, vel, rad=20, color=None):


        self.coord = coord
        self.vel = vel
        if color == None:
            color = rand_color()
        self.color = color
        self.rad = rad
        self.is_alive = True
done = False
clock = pg.time.Clock()
class cannon:
    pass
class actions:
    pass
class scores:
    pass
while not done:
    clock.tick(15)
    screen.fill(BLACK)

    pg.display.flip()


pg.quit()
