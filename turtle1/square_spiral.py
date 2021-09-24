import turtle

turtle.shape('turtle')

side = 20
revolutions = 5

for i in range(revolutions * 2):
    for _ in range(2):
        turtle.forward((i + 1) * side)
        turtle.left(90)