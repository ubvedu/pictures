from turtle import *
import turtle

shape('turtle')

r = 200

penup()
left(90)
forward(r)
left(90)
pendown()

fillcolor(1, 1, 0.1)
begin_fill()
circle(r)
end_fill()

penup()
left(90)
forward(r * 4 / 5)
right(90)


def draw_eye():
    forward(r / 3)
    right(90)
    pendown()
    fillcolor(0.1, 0.2, 0.4)
    begin_fill()
    circle(r / 6)
    end_fill()
    penup()
    right(90)
    forward(r / 3)


draw_eye()
draw_eye()

left(90)
forward(r * 2 / 5)

pensize(10)
pendown()
backward(r / 5)
penup()

right(90)
forward(r * 3 / 5)
left(90)

circle(r * 3 / 5, 30)

color(0.4, 0.3, 0.1)
pendown()
circle(r * 3 / 5, 120)
