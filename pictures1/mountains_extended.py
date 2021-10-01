import pygame
from pygame.draw import *
from pygame.transform import flip
from mountains_crops import *
from math import sqrt

pygame.init()

FPS = 30
h = 600
w = round(600 / sqrt(2))
screen = pygame.display.set_mode((w, h))


screen.blit(background(w, h), (0, 0))

screen.blit(bush(w / 4), (w * 6 / 7, h * 2 / 3))
screen.blit(bush(w / 4), (w * 3 / 7, h * 4 / 5))
screen.blit(bush(w / 7), (w * 6 / 7, h * 5 / 9))
screen.blit(bush(w / 6), (w * 6 / 9, h * 7 / 11))
screen.blit(bush(w / 4), (w * -1 / 9, h * 2 / 3))
screen.blit(bush(w / 7), (w * 0 / 7, h * 4 / 9))

screen.blit(lama(h / 5), (w / 9, h / 3))
screen.blit(flip(lama(h / 5), True, False), (w * 2 / 9, h * 3 / 7))
screen.blit(flip(lama(h / 5), True, False), (w / 3, h * 3 / 8))
screen.blit(lama(h / 3), (w / 3, h / 2))
screen.blit(flip(lama(h / 2.2), True, False), (w / 2, h * 5 / 8))
screen.blit(lama(h), (-w / 2, h / 2))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
