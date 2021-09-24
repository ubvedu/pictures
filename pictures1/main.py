import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))

cx = 400
cy = 400
ex = 125
ey = 50

circle(screen, (255, 255, 0), (cx, cy), 300)
circle(screen, (255, 0, 0), (cx - ex, cy - ey), 50)
circle(screen, (255, 0, 0), (cx + ex, cy - ey), 35)
circle(screen, (0, 0, 0), (cx - ex, cy - ey), 30)
circle(screen, (0, 0, 0), (cx + ex, cx - ey), 20)

mx = 150
my = 100
mh = 30

rect(screen, (0, 0, 0), (cx - mx, cy + my, 2*mx, mh))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
