import pygame
from math import pi, sqrt
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

W, H = 1200, 700

NUM_BALLS = 3

FPS = 30


font = pygame.font.SysFont(None, 20)


def main():
    pygame.init()

    screen = pygame.display.set_mode((W, H))

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    balls = [new_ball() for _ in range(NUM_BALLS)]
    score = 0

    while not finished:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                score += handle_click(balls, event)

        update_balls(balls)
        draw_balls(screen, balls)

        pygame.display.update()
        screen.fill(BLACK)

    pygame.quit()
    print(f'Congratulations! Your score is {score}')


def new_ball():
    r = 1
    x = randint(0, W)
    y = randint(0, H)
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    dr = randint(NUM_BALLS * 2, NUM_BALLS * 5)
    d2r = -1
    return x, y, r, vx, vy, dr, d2r


def update_balls(balls):
    for (i, (x, y, r, vx, vy, dr, d2r)) in enumerate(balls):
        if x < r or x > W - r:
            vx *= -1
        if y < r or y > H - r:
            vy *= -1
        balls[i] = (x + vx, y + vy, r + dr, vx, vy, dr +
                    d2r, d2r) if r + dr > 0 else new_ball()


def draw_ball(sf, ball):
    x, y, r = ball[:3]
    color = COLORS[randint(0, 5)]
    circle(sf, color, (x, y), r)


def draw_balls(sf, balls):
    for ball in balls:
        draw_ball(sf, ball)


cx, cy = W / 2, H / 2


def handle_click(balls, event):
    scores = []
    for (i, ball) in enumerate(balls):
        if ball_hit(ball, event.pos):
            scores.append(ball_score(ball))
            balls[i] = new_ball()
            balls.append(new_ball)

    score = sum(scores) ** len(scores)
    if len(scores) == 1:
        print(f'Good shot! You got {score} points')
    elif len(scores) == 2:
        print(f'Double shot! You got {score} points')

    return score


def ball_hit(ball, pos):
    x, y, r = ball[:3]
    mx, my = pos
    return (x - mx) ** 2 + (y - my) ** 2 < r ** 2


def ball_score(ball):
    _, _, r = ball[:3]
    return round(1000 / (pi * r ** 2))


main()
