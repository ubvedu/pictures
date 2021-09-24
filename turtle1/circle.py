import turtle
import math

turtle.shape('turtle')

radius = 100
sides = 50

for _ in range(sides):
    turtle.forward(2 * radius * math.sin(math.pi / sides))
    turtle.left(360 / sides)
