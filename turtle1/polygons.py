import turtle
import math

turtle.shape('turtle')

radius = 50
polygons = 20


def draw_polygon(sides, radius):
    angle = 360 / sides
    turtle.right((180 - angle) / 2)
    for _ in range(sides):
        turtle.forward(2 * radius * math.sin(math.pi / sides))
        turtle.left(angle)
    turtle.left((180 - angle) / 2)


for i in range(3, polygons):
    draw_polygon(i, radius)
    new_radius = radius / math.cos(math.pi / (i + 1))
    turtle.penup()
    turtle.backward(new_radius - radius)
    turtle.pendown()
    radius = new_radius
