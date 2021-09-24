import turtle
import math

turtle.shape('turtle')

distance = 5
revolutions = 5
step = 10
bias = 10

angle = 0
while angle < revolutions * 2 * math.pi:
    radius = bias + distance * angle
    turtle.forward(step)
    d_angle = step / 2 / radius
    turtle.left(d_angle * 180 / math.pi)
    angle += d_angle
