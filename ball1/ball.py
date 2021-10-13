from math import pi
from random import randint
import pygame


class Ball:
    def __init__(self, x1, y1, x2, y2):
        self.r = 1
        self.x = randint(x1, x2)
        self.y = randint(y1, y2)
        self.vx = randint(-5, 5)
        self.vy = randint(-5, 5)
        self.dr = randint(5, 15)
        self.d2r = -1

    def draw(self, sf, color):
        pygame.draw.circle(sf, color, (self.x, self.y), self.r)

    def hit(self, pos):
        x, y = pos
        return (x - self.x) ** 2 + (y - self.y) ** 2 < self.r ** 2

    def area(self):
        return pi * self.r ** 2

    def reflect_box(self, x1, y1, x2, y2):
        if self.x - self.r < x1:
            self.x = x1
            self.vx *= -1
        if self.x + self.r > x2:
            self.x = x2 
            self.vx *= -1
        if self.y - self.r < y1:
            self.y = y1
            self.vy *= -1
        if self.y + self.r > y2:
            self.y = y2
            self.vy *= -1

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.r += self.dr
        self.dr += self.d2r

    def exists(self):
        return self.r > 0
