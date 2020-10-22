
import pygame
import numpy as np
from pygame.draw import *
from random import randint, random

pygame.init()
pygame.font.init()

FPS = 40
screen = pygame.display.set_mode((1200, 750))
font = pygame.font.SysFont("Times New Roman", 25)
font_1 = pygame.font.SysFont("Times New Roman", 20)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (155, 150, 90)

hearts = pygame.Surface((1200, 100))
hearts.fill(WHITE)

x, y = 0, 0

clock = pygame.time.Clock()


def super_sort(l):
    if l==[]:
        return l
    dict = {}
    temp = {}
    array = []
    for s in l:
        xx = ""
        i = 0
        for i in range(len(s)):
            if s[len(s)-i-1] == ' ':
                break
            else:
                xx += s[len(s)-i-1]
            i += 1
        xx=xx[::-1]
        xx = int(xx)
        dict[xx] = s
    array = list(dict.keys())
    array.sort()
    array.reverse()
    for a in array:
        temp[a] = dict[a]
    l.clear()
    for item in temp:
        l.append(temp[item])
    return l


class Ball:
    def __init__(self):
        self.pos = (randint(100, 1100), randint(100, 500))
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.radius = randint(10, 40)
        self.b_radius = self.radius
        self.speed = [randint(-10, 10), randint(-10, 10)]
        self.score=0

    def make(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)

    def refract(self):
       if self.pos[0] > 1195-self.radius:
            self.speed[0]*=-1
            self.pos = (self.pos[0]-3, self.pos[1])
       if self.pos[0] < self.radius+5:
           self.speed[0] *= -1
           self.pos = (self.pos[0] + 3, self.pos[1])
       if self.pos[1] > 745-self.b_radius:
           self.speed[1] *= -1
           self.pos = (self.pos[0], self.pos[1]-3)
       if self.pos[1] < self.b_radius+105:
           self.speed[1] *= -1
           self.pos = (self.pos[0], self.pos[1]+3)

    def move(self, t):
        self.refract()
        self.pos = (self.pos[0]+self.speed[0]*t, self.pos[1]+self.speed[1]*t)

    def click(self, x, y):
        if (x - self.pos[0])**2 + (y - self.pos[1])**2 < self.radius**2:
            self.score += 1
            self.pos = (randint(100, 1200), randint(100, 500))
            self.speed = [randint(-10, 10), randint(-10, 10)]


class El_ball(Ball):
    def __init__(self):
        super().__init__()
        self.b_radius*=0.9

    def make(self, surface):
        pygame.draw.ellipse(screen, self.color, (self.pos[0]-self.radius,
                            self.pos[1]-self.b_radius, self.radius, self.b_radius))

    def e_move(self, t, x, y):
        self.refract()
        r = (x-self.pos[0])**2+(y-self.pos[1])**2
        w = 1/(r+2)
        self.speed = [self.speed[0]+(self.pos[0]-x)/np.sqrt(r)*w*t, self.speed[1]+(self.pos[1]-y)/np.sqrt(r)*w*t]
        self.move(t)
        self.refract()


def balls_init(n):
    A = [Ball() for i in range(n)]
    return A


def e_balls_init(n):
    A = [El_ball() for i in range(n)]
    return A


def action(A, x, y):
    result = 0
    for i in range(len(A)):
        A[i].click(x, y)
        A[i].make(screen)
        A[i].move(1)
        result += A[i].score
    return result


def e_action(A, x, y, z, r):
    result = 0
    for i in range(len(A)):
        A[i].click(x, y)
        A[i].make(screen)
        A[i].e_move(1, z, r)
        result += A[i].score
    return result


el_balls = e_balls_init(10)
balls = balls_init(10)

done = False
e_ball = El_ball()
loses = 3
z, r = 0, 0
sc = 0
while not done:
    clock.tick(20)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
            elif event.type == pygame.MOUSEMOTION:
                z, r = event.pos
    if loses > 0:
        hearts.fill(WHITE)
        for i in range(loses):
            pygame.draw.circle(hearts, RED, (550+i*50, 50), 25)
        screen.fill((0, 0, 0))
        loses = 3-e_action(el_balls, x, y, z, r)
        sc = action(balls, x, y)
        score_surf = font.render("Score: {}".format(sc), False, RED)
        OKAY=font_1.render("You may enter your pseudonym after end of the attempt", False, RED)
        screen.blit(hearts, (0, 0))
        screen.blit(score_surf, (10, 30))
        screen.blit(OKAY, (10, 60))
        out = open('results.txt', 'r')
        s = out.readlines()
        s = [sss.rstrip() for sss in s]
        s = super_sort(s)
        if len(s) > 0:
            leaders_list_1 = font.render("Leaders: "+format(s[0]), False, RED)
            screen.blit(leaders_list_1, (900, 20))
            if len(s) > 1:
                leaders_list_2 = font.render(format(s[1]), False, RED)
                screen.blit(leaders_list_2, (990, 43))
                if len(s) > 2:
                    leaders_list_3 = font.render(format(s[2]), False, RED)
                    screen.blit(leaders_list_3, (990, 66))
        else:
            leaders_list_1 = font.render("Leaders: empty", False, RED)
            screen.blit(leaders_list_1, (900, 20))
    else:
        screen.fill((0, 0, 0))
        text = font.render("Final score: {}".format(sc), False, (255, 255, 255))
        screen.blit(text, (510, 10))
        name = input()
        with open('results.txt', 'a') as f:
            print(name + ": " +str(sc), file=f)
        done = True
    pygame.display.update()
pygame.quit()

