# import random as ran
# import turtle as t
# import numpy as np
# import matplotlib.pyplot as plt
#
# #график показывает, что сумма квадратов перемещений линейно зависит от времени
# t.shape("turtle")
# x=X=y=Y=i=0
# A=B=[0.0]
# V_x=6
# V_y=8
# T=0.1
#
# while i<1000:
#     i=i+1
#     V_x=V_x+(200*ran.uniform(-1 ,1)-5*V_x)*T
#     V_y=V_y+(200*ran.uniform(-1, 1)-5*V_y)*T
#     t.goto(t.xcor()+V_x*T,t.ycor()+V_y*T)
#     X=X+(t.xcor()-x)**2
#     x=t.xcor()
#     c=len(A)
#     A.append(X)
#     B.append(i)
#     plt.scatter(B, A, label='what')
#     if i>6:
#         p, v=np.polyfit(B, A, deg=1, cov=1)
#         z=np.arange(0, B[len(B)-1], 0.01)
#         plt.plot(z, p[0]*z+p[1], label='er')
#     plt.grid()
#     plt.show()



# import matplotlib.pyplot as plt
# import random as r
# x = [1, 2, 3, 4, 5]
# y = [0.99, 0.49, 0.35, 0.253, 0.18]
# for i in range(50):
#     x.append(i+5)
#     y.append(x[i]*r.randint(0, 1))
#     plt.errorbar(x, y, xerr=0.05, yerr=0.1)
#     plt.grid()
#     plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5, 6]
# y = [1, 1.42, 1.76, 2, 2.24, 2.5]
# p, v = np.polyfit(x, y, deg=1, cov=True)
#
# plt.scatter(x, y, label='erre')
#
# z=np.arange(0, x[5], 0.01)
# plt.plot(z, p[0]*z+p[1], label='errerereer')
# plt.show()

# from random import randint
# import turtle as t
#
# def a(): t. forward(50)
# def b(): t. forward(70)
# def c(): t. rt(45)
# def d(): t. lt(45)
# def e(): t. rt(90)
# def f(): t. lt(90)
# def g(): t.penup()
# def h(): t.pendown()
# def k(): g(), a(), h()
#
#
# f(), f()
# t.color("blue")
# t.width(15)
# for i in range(15):
#     k()
# f(), f()
# def what(n):
#     if n==0:
#         return e(), a(), a(), f(), a(), f(), a(), a(), f(), a(), f(), f(), a(), k()
#     if n==1:
#         return e(), k(), f(), d(), b(), c(), e(), a(), a(), e(), e(), a(), a(), e(), k()
#     if n==2:
#         return a(), e(), a(), c(), b(), d(), f(), a(), f(), k(), k(), e(), k()
#     if n==3:
#         return a(), e(), c(), b(), d(), f(), a(), e(), c(), b(), d(), f(),k(), f(), k(), k(), e(), k()
#     if n==4:
#         return e(), a(), f(), a(), e(), a(), e(), e(), k(), a(), e(), k()
#     if n==5:
#         return e(), a(), f(), a(), e(), a(), e(), a(), e(), k(), k(), e(), a(), k()
#     if n==6:
#         return e(), k(), a(), f(), a(), f(), a(), f(), a(), e(), c(), b(), c(), k()
#     if n==7:
#         return a(), e(), c(), b(), d(), a(), f(), k(), f(), k(), k(), e(), k()
#     if n==8:
#         return e(), a(), a(), f(), a(), f(), a(), f(), a(), e(), k(), e(), a(), e(), a(), e(), e(), k(), e(), k()
#     if n==9:
#         return e(), a(), f(), a(), c(), e(), b(), e(), c(), k(), e(), k(), f(), a(), f(), a(), f(), f(), k(), k()
#
# A = [randint(0, 9) for i in range(0, randint(7, 29))]
# for item in A:
#     what(item)

# import turtle as t
# inp=open("namefile.txt", 'r')
# def unbox(s):
#     if s=='a':
#         t.forward(50)
#     if s=='b':
#         t.forward(70)
#     if s=='c':
#         t. rt(45)
#     if s=='d':
#         t.lt(45)
#     if s=='e':
#         t.rt(90)
#     if s=='f':
#         t.lt(90)
#     if s=='g':
#         t.penup()
#     if s=='h':
#         t.pendown()
#     if s=='k':
#         t.penup(), t.forward(50) ,t.pendown()
#
# for letter in inp.readline():
#     unbox(letter)
# inp.close()
# bap=open("namefile.txt", 'w')
# print(x, file=bap)
#
# bap.close()

# import turtle as t
# t.shape("turtle")
# V_x=15
# V_y=60
# x=0
# y=0
# T=0
# x_0=0
# A = [i*0.01 for i in range(100000)]
# for j in range((len(A))):
#        x=x_0+V_x*(A[j]-T)
#        y=V_y*(A[j]-T)-5*(A[j]-T)**2
#        if y < 0:
#            T=A[j]
#            print(A[j])
#            y=0
#            x_0=x
#            V_y=3*V_y/4
#            V_x=3*V_x/4
#        t.goto(x, y)
#        if(x%2==0):
#            print(x)
#




# import random as rand
#
# import turtle
# import numpy as np
#
#
# n=int(input())
# steps_of_time_number = 1000
#
# wat=turtle.Turtle(shape='classic')
# wat.penup()
# wat.speed(10)
# wat.goto(-400, -400)
# wat.pendown()
# for i in range(4):
#     wat.forward(800)
#     wat.lt(90)
#
#
# T=0.06
# pool = [turtle.Turtle(shape='circle') for i in range(n)]
# for unit in pool:
#     unit.penup()
#     unit.speed(50)
#     unit.goto(rand.randint(-350, 350), rand.randint(-350,350))
#     unit.speed(10)
#     unit.seth(rand.uniform(-180, 180))
#     unit.pendown()
#
# velocities=[ [rand.uniform(-45, 45), rand.uniform(-45, 45)] for i in range(n)]
# for i in range(steps_of_time_number):
#     for j in range(n):
#         F_x = 0
#         F_y = 0
#         a_x=0
#         a_y=0
#         for k in range(n):
#             if k!=j:
#                 r_x=pool[k].xcor()-pool[j].xcor()
#                 r_y=pool[k].ycor()-pool[j].ycor()
#                 R=np.sqrt(r_x**2+r_y**2)
#                 F=10**8*(1/R**11-1/R**5)
#                 F_x+=F*r_x/R
#                 F_y+=F*r_y/R
#                 a_x+=F_x
#                 a_y+=F_y
#         velocities[j][0]+=a_x*T
#         velocities[j][1]+=a_y*T
#         pool[j].goto(pool[j].xcor()+velocities[j][0]*T,pool[j].ycor()+velocities[j][1]*T)
#         if pool[j].ycor()>389:
#             velocities[j][1]=-velocities[j][1]
#             pool[j].sety = 777 - pool[j].ycor()
#         if pool[j].ycor()<-389:
#             velocities[j][1] = -velocities[j][1]
#             pool[j].sety = -777 - pool[j].ycor()
#         if pool[j].xcor()>389:
#             velocities[j][0] = -velocities[j][0]
#             pool[j].setx=777-pool[j].xcor()
#         if pool[j].xcor()<-389:
#             velocities[j][0] = -velocities[j][0]
#             pool[j].setx=-777-pool[j].xcor()
