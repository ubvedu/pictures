from math import copysign
import pygame
from pygame.draw import *
from random import *


def flower(s):
    surface = pygame.Surface((s, s))
    a = s / 6
    b = a / 2
    ellipse()


# one fractal iteration
def f(points):
    p0 = points[0]
    w = points[-1][0] - p0[0]
    h = points[-1][1] - p0[1]

    def insert(p1, p2, x, y):
        #   symmetric pattern
        # if (p2[1] - p1[1]) * h < 0:
        #     return (p2[0] - x * (p2[0] - p1[0]), p2[1] + y * (p1[1] - p2[1]))
        return (p1[0] + x * (p2[0] - p1[0]), p1[1] + y * (p2[1] - p1[1]))
    new_points = [p0]
    for i in range(len(points) - 1):
        inner = [insert(
            points[i],
            points[i + 1],
            (p[0] - p0[0]) / w,
            (p[1] - p0[1]) / h,
        ) for p in points[1:-1]]
        #   reverse for symmetric pattern
        # if (points[i + 1][1] - points[i][1]) * h < 0:
        #     inner.reverse()
        new_points += inner
        new_points.append(points[i + 1])
    return new_points


def background(w, h):
    sf = pygame.Surface((w, h))

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
