import turtle
import math

turtle.shape('turtle')

side = 10
squares = 10

for i in range(squares):
    for _ in range(4):
        turtle.left(90)
        turtle.forward((i + 1) * side)
    turtle.penup()
    turtle.right(45)
    turtle.forward(side / math.sqrt(2))
    turtle.left(45)
    turtle.pendown()
