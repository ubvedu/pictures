from turtle import *
from math import cos, pi, sin

v0 = 6
alpha = 0
g = 1.5
k = 0.8

vy = v0 * sin(alpha)
vx = v0 * cos(alpha)
x = 0
y = 0
y0 = -200
dt = 0.5

shape('circle')
while vx > 0.05:
    x += vx * dt
    y += vy * dt
    vy -= g * dt
    if y < y0:
        y = y0
        vx *= k
        vy *= -k
    goto(x, y)
done()
