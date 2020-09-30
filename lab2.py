# import turtle as t
# t.shape("turtle")
# while 1:
#     t.forward(150)
#     t.left(90)

# import turtle as t
# t.shape("turtle")
# i=1
# while i<180:
#     t.left(2)
#     t.forward(5)
#     i=i+1

# import turtle as t
# t.shape("turtle")
# for i in range(0, 11, 1):
#     for j in range(4):
#         t.forward(i*10+50)
#         t.left(90)
#     t.penup()
#     t.goto(-5*(i+1), -5*(i+1))
#     t.pendown()


# import turtle as t
# # n = int(input())
# t.shape("turtle")
# for i in range(16):
#     t.left(360/16)
#     t.forward(150)
#     t.stamp()
#     t.right(180)
#     t.forward(150)
#     t.left(180)


# import turtle as t
# t.shape("turtle")
# i = 1
# while 1:
#     t.forward((i*i/10000+i*2/10000)**(1/2))
#     t.right(5)
#     i=i+1

# import turtle as t
# t.shape("classic")
# i = 10
# while 1:
#     for j in range(2):
#         t.forward(i+10)
#         t.left(90)
#     i=i+10

# import turtle as t
# t.shape("turtle")
#
#
# def func(v, s):
#     t.left(180 - 180 * (v - 2) / 2/v)
#     for i in range(v):
#         t.forward(s)
#         if(i!=v-1):
#             t.left(180-180*(v-2)/v)
# for i in range(3, 13):
#     func(i, 15*i+15)
#     t.right(180*(i-2)/i/2)
#     t.penup()
#     t.forward(15)
#     t.pendown()

# import turtle as t
# import numpy as np
#
# n = int(input())
# t.shape("turtle")
# def circle(s):
#     for i in range(35):
#         t.forward(2*np.pi/50*s)
#         t.left(180-180*33/35)
# for j in range(n):
#     circle(50)
#     t.right(360/n)


# import turtle as t
# import numpy as np
# def circle(s , v):
#     for i in range(35):
#         t.forward(2*np.pi/50*s)
#         if(v==1):
#             t.left(180-180*33/35)
#         else:
#             t.right(180-180*33/35)
# t.left(90)
# for i in range(6):
#     circle(30*(i+1), 1)
#     circle(30 * (i + 1), 2)


# import turtle as t
# import numpy as np
#
# def arc(r):
#     for i in range(30):
#         t.forward(2*np.pi/60*r)
#         t .right(180-180*58/60)
# n = int(input())
# r_1=int(input())
# r_2=int(input())
# t.shape("turtle")
# t.left(90)
# for i in range(n):
#     arc(r_1)
#     arc(r_2)

# import turtle as t
# import numpy as np
#
#
# def circle(r):
#     for i in range(60):
#          t.forward(2*np.pi/60*r)
#          t .right(180-180*58/60)
#
#
# def arc(r):
#     for i in range(30):
#          t.forward(2*np.pi/60*r)
#          t .right(180-180*58/60)
#
#
# t.penup()
# t.goto(-100, 0)
# t.pendown()
# t.left(90)
# t.color("black", "orange")
# t.begin_fill()
# circle(100)
# t.end_fill()
# t.penup()
# t.goto(35, 35)
# t.pendown()
# t.left(90)
# t.color("black", "green")
# t.begin_fill()
# circle(14)
# t.end_fill()
# t.penup()
# t.goto(-35, 35)
# t.pendown()
# t.color("black", "green")
# t.begin_fill()
# circle(14)
# t.end_fill()
# t.penup()
# t.goto(0, 27)
# t.pendown()
# t.left(90)
# t.width(10)
# t.forward(50)
# t.penup()
# t.goto(70,0)
# t.pendown()
# t.color("red")
# arc(70)

# import turtle as t
#
#
# def star(n):
#
#     for i in range(n):
#         t.forward(150)
#         t.left(180-180/n)
#
#
# x=int(input())
# t.shape("turtle")
# star(x)
# t.penup()
# t.goto(200,0)
# t.pendown()
# star(x+2)