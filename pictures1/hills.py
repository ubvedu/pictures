import pygame
from pygame.draw import *
from hills_utils import *
from math import sqrt

pygame.init()

FPS = 30
h = 600
w = round(600 / sqrt(2))
screen = pygame.display.set_mode((w, h))


screen.blit(background(w, h), (0, 0))

# circle(screen, (255, 255, 0), (w / 2, h / 2), w / 4)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
