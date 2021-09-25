from math import copysign
from random import *
import turtle


turtles_num = 20
vessel_size = 300


vessel_drawer = turtle.Turtle()
vessel_drawer.hideturtle()
vessel_drawer.penup()
vessel_drawer.speed(50)
vessel_drawer.goto(vessel_size, vessel_size)
vessel_drawer.pendown()
vessel_drawer.goto(vessel_size, -vessel_size)
vessel_drawer.goto(-vessel_size, -vessel_size)
vessel_drawer.goto(-vessel_size, vessel_size)
vessel_drawer.goto(vessel_size, vessel_size)


pool = [turtle.Turtle(shape='circle') for _ in range(turtles_num)]
for unit in pool:
    unit.speed(1000)
    unit.penup()
    unit.goto((random() - 0.5) * 2 * vessel_size,
              (random() - 0.5) * 2 * vessel_size)
    unit.left((random() - 0.5) * 360)


while True:
    for unit in pool:
        unit.forward(5)
        x, y = unit.pos()
        alpha = unit.heading()
        if abs(x) > vessel_size:
            unit.goto(copysign(vessel_size, x), y)
            if alpha < 180:
                unit.left(180 - 2 * alpha)
            else:
                unit.left(3 * 180 - 2 * alpha)
        if abs(y) > vessel_size:
            unit.goto(x, copysign(vessel_size, y))
            if alpha < 180:
                unit.left(-2 * alpha)
            else:
                unit.left(4 * 180 - 2 * alpha)

turtle.done()
