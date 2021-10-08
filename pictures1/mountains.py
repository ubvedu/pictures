import pygame
from pygame.draw import *
from mountains_crops import *
from math import sqrt

pygame.init()

FPS = 30
h = 900
w = round(h // sqrt(2))
screen = pygame.display.set_mode((w, h))


screen.blit(background(w, h), (0, 0))
screen.blit(bush(w // 3), (w * 5 // 8, h * 2 // 3))
screen.blit(lama(h // 2), (0, h // 3))
# circle(screen, (255, 255, 0), (w // 2, h // 2), w // 4)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
