from pygame import Surface
import pygame
from pygame.draw import *
from pygame.transform import rotate
from random import *
from math import cos, pi, sqrt


# one fractal iteration
def f(points, symmetric=False):
    p0 = points[0]
    w = points[-1][0] - p0[0]
    h = points[-1][1] - p0[1]

    def insert(p1, p2, x, y):

        if symmetric and (p2[1] - p1[1]) * h < 0:
            return (p2[0] - x * (p2[0] - p1[0]), p2[1] + y * (p1[1] - p2[1]))

        return (p1[0] + x * (p2[0] - p1[0]), p1[1] + y * (p2[1] - p1[1]))

    new_points = [p0]
    for i in range(len(points) - 1):

        inner = [insert(
            points[i],
            points[i + 1],
            (p[0] - p0[0]) / w,
            (p[1] - p0[1]) / h,
        ) for p in points[1:-1]]

        if symmetric and (points[i + 1][1] - points[i][1]) * h < 0:
            inner.reverse()

        new_points += inner
        new_points.append(points[i + 1])

    return new_points


def background(w, h):
    sf = Surface((w, h))

    sf.fill((212, 187, 255))

    hills = f([(0, h * 3 / 8),
              (w / 3, h * 2 / 7),
              (w * 3 / 5, h / 7),
              (w, h / 4)])
    polygon(sf, (168, 168, 168), [(w, h),
                                  (0, h)] + hills)
    aalines(sf, (0, 0, 0), False, hills)

    grass = f([(0, h / 2 - h / 16 - h / 64),
               (w / 4, h / 2 - h / 16 - h / 32),
               (w * 3 / 7, h / 2 - h / 16),
               (w * 5 / 7, h / 2 + h / 16 - h / 32 - h / 64),
               (w, h / 2 + h / 16)])
    polygon(sf, (66, 190, 101), [(w, h),
                                 (0, h)] + grass)
    aalines(sf, (0, 0, 0), False, grass)

    return sf


def flower(d):
    sf = Surface((d, d))
    sf.set_colorkey((0, 0, 0))

    r = d / 2
    a = r / 3
    b = a / 1.5

    size = (2 * a, 2 * b)

    def draw_petal(x, y):
        ellipse(sf, (255, 255, 255), (r - a + x, r - b + y) + size)
        ellipse(sf, (141, 141, 141), (r - a + x, r - b + y) + size, 1)

    draw_petal(0, -b * 3 / 2)
    draw_petal(-a, -b)
    draw_petal(+a, -b)
    draw_petal(-a * 3 / 2, 0)

    ellipse(sf, (241, 194, 27), (r - a, r - b) + size)

    draw_petal(+a * 3 / 2, 0)
    draw_petal(-a, b)
    draw_petal(+a, b)
    draw_petal(0, +b * 3 / 2)

    return sf


def bush(d):
    sf = Surface((d, d))
    sf.set_colorkey((0, 0, 0))

    R = d / 2

    circle(sf, (111, 220, 140), (R, R), R)

    sf.blit(rotate(flower(d / 3), +20), (R * 0.4, R * 0.1))
    sf.blit(rotate(flower(d / 3), -30), (R * 0.9, R * 0.4))
    sf.blit(rotate(flower(d / 3), +30), (R * 0.3, R * 0.6))
    sf.blit(rotate(flower(d / 4), -30), (R * 1.0, R * 0.0))
    sf.blit(rotate(flower(d / 4), -30), (R * 0.9, R * 1.1))
    sf.blit(rotate(flower(d / 4), +60), (R * 0.0, R * 0.5))
    sf.blit(rotate(flower(d / 5), +40), (R * 0.4, R * 1.2))
    sf.blit(rotate(flower(d / 5), -90), (R * 1.6, R * 0.9))
    return sf
