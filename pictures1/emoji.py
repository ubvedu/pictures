import pygame
import numpy as np
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))

r = 200

cx = 400
cy = 400
ex = r * 2 // 5
ey = r // 5

print(ex, ey)

# head
circle(screen, (255, 255, 0), (cx, cy), r)

# eyes
eye_r = r // 6
lex = cx - ex
rex = cx + ex
bey = cy - ey
circle(screen, (255, 0, 0), (lex, bey), eye_r)
circle(screen, (255, 0, 0), (rex, bey), eye_r * 2 // 3)
circle(screen, (0, 0, 0), (lex, bey), eye_r // 2)
circle(screen, (0, 0, 0), (rex, bey), eye_r // 3)

# mouth
mx = r // 2
my = r // 3
mh = r // 10
rect(screen, (0, 0, 0), (cx - mx, cy + my, 2*mx, mh))


def rect(w, h):
    return [
        (-w//2, -h//2),
        (-w//2, +h//2),
        (+w//2, +h//2),
        (+w//2, -h//2),
    ]


def move_to(poly, x, y):
    return [(px + x, py + y) for (px, py) in poly]


def rot(mat, angle):
    return np.matmul(mat, np.array([
        [+np.cos(angle), -np.sin(angle)],
        [+np.sin(angle), +np.cos(angle)]
    ]))


# eyebrows
polygon(screen, (0, 0, 0),
        move_to(rot(rect(r // 2, r // 10), np.pi / 6), rex, bey - eye_r - r // 50))
polygon(screen, (0, 0, 0),
        move_to(rot(rect(r * 3 // 5, r // 8), -np.pi // 6), lex + r // 30, bey - eye_r - r // 13))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
