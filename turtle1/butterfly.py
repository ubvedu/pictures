import turtle

turtle.shape('turtle')

circles = 6
radius = 100
step = 25

turtle.left(90)
for i in range(circles):
    r = radius + step * i
    turtle.circle(r)
    turtle.circle(-r)
