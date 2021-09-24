import turtle

turtle.shape('turtle')

radius = 20
n = 19

for _ in range(n):
    turtle.circle(radius)
    turtle.left(360 / n)
