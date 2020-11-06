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


class Ball:

    def __init__(self, coord, speed, radius=20, color=None):

        self.coord = coord
        self.speed = speed
        self.color=rand_color()
        self.color = color
        self.radius = radius
        self.is_alive = True

    def refract(self):
        if self.pos[0] > 795 - self.radius:
            self.speed[0] *= -1
            self.pos = (self.pos[0] - 3, self.pos[1])
        if self.pos[0] < self.radius + 5:
            self.speed[0] *= -1
            self.pos = (self.pos[0] + 3, self.pos[1])
        if self.pos[1] > 595 - self.radius:
            self.speed[1] *= -1
            self.pos = (self.pos[0], self.pos[1] - 3)
        if self.pos[1] < self.radius + 105:
            self.speed[1] *= -1
            self.pos = (self.pos[0], self.pos[1] + 3)

    def move(self):
        self.refract()
        self.speed[1] += 1
        self.coord[0] += self.speed[0]
        self.coord[1] += self.speed[1]

    def draw(self):
        pg.draw.circle(screen, rand_color(), self.coord, self.radius)

class cannon:
    def __init__(self, coord=[30, SCREEN_SIZE[1] // 2], angle=0, max_pow=50, min_pow=5, color=rand_color()):
        self.coord = coord
        self.angle = angle
        self.max_pow = max_pow
        self.min_pow = min_pow
        self.color = color
        self.active = False
        self.pow = min_pow

    def start(self):
        self.active = True

    def charge(self):

        if self.active and self.pow < self.max_pow:
            self.pow += 4

    def boom(self):
        speed = self.pow
        angle = self.angle
        ball = Ball(list(self.coord), [int(speed * np.cos(angle)), int(speed * np.sin(angle))])
        self.pow = self.min_pow
        self.active = False
        return ball

    def draw(self):
        cannon_shape = []
        vec_1 = np.array([int(5 * np.cos(self.angle - np.pi / 2)), int(5 * np.sin(self.angle - np.pi / 2))])
        vec_2 = np.array([int(self.pow * np.cos(self.angle)), int(self.pow * np.sin(self.angle))])
        gun_pos = np.array(self.coord)
        cannon_shape.append((gun_pos + vec_1).tolist())
        cannon_shape.append((gun_pos + vec_1 + vec_2).tolist())
        cannon_shape.append((gun_pos + vec_2 - vec_1).tolist())
        cannon_shape.append((gun_pos - vec_1).tolist())
        pg.draw.polygon(screen, self.color, cannon_shape)


class actions:
    def __init__(self):
        self.balls = []
        self.cannon = cannon()

    def current_ev(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.cannon.start()
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.balls.append(self.cannon.boom())

        return done

    def draw(self):
        for i in self.balls:
            i.draw()
        self.cannon.draw()

    def do(self, event):
        done = self.current_ev(event)
        self.draw()
        return done


clock = pg.time.Clock()
done = False

Actions = actions()
while not done:
    clock.tick(15)
    screen.fill(BLACK)

    done = Actions.do(pg.event.get())

    pg.display.flip()


pg.quit()