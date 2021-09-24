import turtle

turtle.shape('turtle')

coils = 10
radius1 = 60
radius2 = 40

turtle.left(90)
for _ in range(coils):
    turtle.circle(-radius1, 180)
    turtle.circle(-radius2, 180)
