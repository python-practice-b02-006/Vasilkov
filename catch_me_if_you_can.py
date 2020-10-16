
import pygame
import numpy as np
from pygame.draw import *
from random import randint, random

pygame.init()
pygame.font.init()




FPS = 40
screen = pygame.display.set_mode((1200, 750))
font = pygame.font.SysFont("Times New Roman", 30)


RED = (255, 0, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (155, 150, 90)

hearts = pygame.Surface((1200, 100))
hearts.fill(WHITE)

x, y = 0, 0

clock = pygame.time.Clock()

class Ball:
    def __init__(self):
        self.pos = (randint(100, 1100), randint(100, 500))
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.radius = randint(10, 40)
        self.bradius = self.radius
        self.speed = [randint(-10, 10), randint(-10, 10)]
        self.score=0

    def make(self,surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)

    def refract(self):
       if self.pos[0]>1195-self.radius:
            self.speed[0]*=-1
            self.pos=(self.pos[0]-3, self.pos[1])
       if self.pos[0]<self.radius+5:
           self.speed[0] *= -1
           self.pos = (self.pos[0] + 3, self.pos[1])
       if self.pos[1]>745-self.bradius:
           self.speed[1]*=-1
           self.pos = (self.pos[0], self.pos[1]-3)
       if self.pos[1]<self.bradius+105:
           self.speed[1] *= -1
           self.pos = (self.pos[0], self.pos[1]+3)

    def move(self, t):
        self.refract()
        self.pos=(self.pos[0]+self.speed[0]*t, self.pos[1]+self.speed[1]*t)

    def click(self, x, y):
        if (x - self.pos[0])**2 + (y - self.pos[1])**2 < self.radius**2:
            self.score += 1
            self.pos = (randint(100, 1200), randint(100, 500))
            self.speed = [randint(-10, 10), randint(-10, 10)]



class Elball(Ball):
    def __init__(self):
        super().__init__()
        self.bradius*=0.9
    def make(self,surface):
        pygame.draw.ellipse(screen, self.color, (self.pos[0]-self.radius, self.pos[1]-self.bradius, self.radius, self.bradius))
    def emove(self, t, x, y):
        self.refract()
        r=(x-self.pos[0])**2+(y-self.pos[1])**2
        w=1/(r+2)
        self.speed=[self.speed[0]+(self.pos[0]-x)/np.sqrt(r)*w*t, self.speed[1]+(self.pos[1]-y)/np.sqrt(r)*w*t]
        self.move(t)
        self.refract()


def balls_init(n):
    A = [Ball() for i in range(n)]
    return A


def eballs_init(n):
    A = [Elball() for i in range(n)]
    return A


def action(A, x, y):
    result = 0
    for i in range(len(A)):
        A[i].click(x, y)
        A[i].make(screen)
        A[i].move(1)
        result += A[i].score
    return result


def eaction(A, x, y, z, r):
    result = 0
    for i in range(len(A)):
        A[i].click(x, y)
        A[i].make(screen)
        A[i].emove(1, z, r)
        result += A[i].score
    return result

elballs=eballs_init(10)
balls = balls_init(10)

done = False
eball=Elball()
loses=3
z ,r =0, 0
sc=0
while not done:
    clock.tick(20)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
            elif event.type==pygame.MOUSEMOTION:
                z, r=event.pos
    if loses>0:
        hearts.fill(WHITE)
        for i in range(loses):
            pygame.draw.circle(hearts, RED, (550+i*50, 50), 25)
        screen.fill((0, 0, 0))
        loses=3-eaction(elballs, x, y, z, r)
        sc=action(balls, x, y)
        score_surf = font.render("Score: {}".format(sc), False, MAGENTA)
        screen.blit(hearts, (0, 0))
        screen.blit(score_surf, (10, 30))
    else:
        screen.fill((0, 0, 0))
        text = font.render("Final score: {}".format(sc), False, (255, 255, 255))
        screen.blit(text, (510, 10))
        name = input()
        with open('results.txt', 'a') as f:
            print(name + ':' +str(sc), file=f)
        done = True
    pygame.display.update()
pygame.quit()

