import turtle

turtle.shape('turtle')

radius = 100
n = 50

for _ in range(n):
    turtle.forward(radius)
    turtle.stamp()
    turtle.backward(radius)
    turtle.left(360 / n)
