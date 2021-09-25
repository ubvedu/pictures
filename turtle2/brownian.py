from random import *
from turtle import *

shape('turtle')
color(0.7, 0, 0.2)

max_dist = 100
moves = 100

for _ in range(moves):
    forward(max_dist * random())
    left((random() - 0.5) * 360)
