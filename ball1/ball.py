import pygame
from pygame.draw import *
from random import randint

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

W, H = 1200, 900

num_balls = 3

FPS = 2 * num_balls


def main():
    pygame.init()

    screen = pygame.display.set_mode((W, H))

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    balls = [new_ball() for _ in range(num_balls)]
    score = 0

    while not finished:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                score += handle_click(balls, event)

        balls = update_balls(balls)
        draw_balls(screen, balls)

        pygame.display.update()
        screen.fill(BLACK)

    pygame.quit()
    print(f'Congratulations! Your score is {round(score)}')


def new_ball():
    r = randint(W // 120, W // 12)
    x = randint(r, W - r)
    y = randint(r, H - r)
    return x, y, r


def update_balls(balls):
    return balls[1:] + [new_ball()]


def draw_ball(sf, x, y, r):
    color = COLORS[randint(0, 5)]
    circle(sf, color, (x, y), r)


def draw_balls(sf, balls):
    for ball in balls:
        draw_ball(sf, *ball)


cx, cy = W / 2, H / 2


def handle_click(balls, event):
    mx, my = event.pos
    score = 0
    for (x, y, r) in balls:
        if (x - mx) ** 2 + (y - my) ** 2 < r ** 2:
            score += ((cx - mx) ** 2 + (cy - my) ** 2) / r
    return score


main()
