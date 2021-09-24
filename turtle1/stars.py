from math import cos, pi
import turtle

radius = 100


def draw_star(tl, n):
    coms = [
        lambda: tl.shape('turtle'),
        lambda: tl.right(90 / n),
    ]
    for _ in range(n):
        coms.append(lambda: tl.forward(2 * radius * cos(pi / 2 / n)))
        coms.append(lambda: tl.left(180 - 180 / n))
    return coms


tl1 = turtle.Turtle(shape='turtle')
tl1.penup()
tl1.backward(2 * radius)
tl1.pendown()

stars = [
    draw_star(tl1, 5),
    draw_star(turtle.Turtle(shape='turtle'), 11),
]

for i in range(max(map(len, stars))):
    for star in stars:
        if i < len(star):
            star[i]()
