from math import cos, pi
import turtle


radius = 100


tl1 = turtle.Turtle(shape='turtle')
tl1.penup()
tl1.backward(2 * radius)
tl1.pendown()
tl2 = turtle.Turtle(shape='turtle')


drawers = [
    [tl1, 5, 0],
    [tl2, 11, 0],
]


def prepare(tl, n):
    tl.right(90 / n)


def move(tl, n):
    tl.forward(2 * radius * cos(pi / 2 / n))
    tl.left(180 - 180 / n)


for drawer in drawers:
    prepare(drawer[0], drawer[1])

done = False
while not done:
    done = True
    for drawer in drawers:
        if drawer[2] != drawer[1]:
            move(drawer[0], drawer[1])
            drawer[2] += 1
            done = False
