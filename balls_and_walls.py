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

    def __init__(self, pos, speed, radius=20):

        self.pos = pos
        self.speed = speed
        self.color = rand_color()
        self.radius = radius
        self.is_alive = True

    def refract(self):
        if self.pos[0] > 795 - self.radius:
            self.speed[0] *= -0.8
            self.pos = (self.pos[0] - 5, self.pos[1])
        if self.pos[0] < self.radius + 5:
            self.speed[0] *= -0.8
            self.pos = (self.pos[0] + 5, self.pos[1])
        if self.pos[1] > 595 - self.radius:
            self.speed[1] *= -0.8
            self.pos = (self.pos[0], self.pos[1]-5)
        if self.pos[1] < self.radius+3:
            self.speed[1] *= -0.8
            self.pos = (self.pos[0], self.pos[1]+5)

    def move(self):
        self.refract()
        self.speed[1] += 1
        self.pos = list(self.pos)
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
        if self.speed[0] ** 2 + self.speed[1] ** 2 < 5 ** 2 and self.pos[1] > SCREEN_SIZE[1] - 2 * self.radius:
            self.is_alive = False
    def draw(self):
        pg.draw.circle(screen, self.color, self.pos, self.radius)


class Cannon:

    def __init__(self, pos=[30, SCREEN_SIZE[1] // 2], angle=0, max_pow=50, min_pow=5, color=rand_color()):
        self.pos = pos
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
        ball = Ball(list(self.pos), [int(speed * np.cos(angle)), int(speed * np.sin(angle))])
        self.pow = self.min_pow
        self.active = False
        return ball

    def draw(self):
        cannon_shape = []
        vec_1 = np.array([int(5 * np.cos(self.angle - np.pi / 2)), int(5 * np.sin(self.angle - np.pi / 2))])
        vec_2 = np.array([int(self.pow * np.cos(self.angle)), int(self.pow * np.sin(self.angle))])
        cannon_pos = np.array(self.pos)
        cannon_shape.append((cannon_pos + vec_1).tolist())
        cannon_shape.append((cannon_pos + vec_1 + vec_2).tolist())
        cannon_shape.append((cannon_pos + vec_2 - vec_1).tolist())
        cannon_shape.append((cannon_pos - vec_1).tolist())
        pg.draw.polygon(screen, self.color, cannon_shape)

    def move(self, v):
        if (self.pos[1] > 30 or v > 0) and (self.pos[1] < SCREEN_SIZE[1] - 30 or v < 0):
            self.pos[1] += v

    def set_angle(self, target_pos):
        self.angle = np.arctan2(target_pos[1] - self.pos[1], target_pos[0] - self.pos[0])


class Actions:
    def __init__(self):
        self.balls = []
        self.cannon = Cannon()

    def current_ev(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.cannon.move(-5)
                elif event.key == pg.K_DOWN:
                    self.cannon.move(5)
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

    def do(self, events):
       done = self.current_ev(events)
       if pg.mouse.get_focused():
            mouse_pos = pg.mouse.get_pos()
            self.cannon.set_angle(mouse_pos)
       self.move()
       self.draw()
       return done

    def move(self):
        dead_balls = []
        for i, ball in enumerate(self.balls):
            ball.move()
            if not ball.is_alive:
                dead_balls.append(i)
        for i in reversed(dead_balls):
            self.balls.pop(i)
        self.cannon.charge()

class Target:
    pass

class Table_of_scores:
    pass


clock = pg.time.Clock()
done = False
actions = Actions()
while not done:
    clock.tick(15)
    screen.fill(BLACK)

    done = actions.do(pg.event.get())

    pg.display.flip()


pg.quit()