import pygame
from random import randint
from ball import Ball

BLACK = (0, 0, 0)

RED = (218, 30, 40)
MAGENTA = (208, 38, 112)
PURPLE = (138, 63, 252)
BLUE = (15, 98, 254)
CYAN = (17, 146, 232)
TEAL = (0, 157, 154)
GREEN = (36, 161, 72)
COLORS = [RED, MAGENTA, PURPLE, BLUE, CYAN, TEAL, GREEN]

LIGHT_RED = (250, 77, 86)
LIGHT_MAGENTA = (238, 83, 150)
LIGHT_PURPLE = (165, 110, 255)
LIGHT_BLUE = (69, 137, 255)
LIGHT_CYAN = (51, 177, 255)
LIGHT_TEAL = (8, 189, 186)
LIGHT_GREEN = (66, 190, 101)
LIGHT_COLORS = [LIGHT_RED, LIGHT_MAGENTA, LIGHT_PURPLE,
                LIGHT_BLUE, LIGHT_CYAN, LIGHT_TEAL, LIGHT_GREEN]

ALL_COLORS = [COLORS, LIGHT_COLORS]

W, H = 1200, 700

NUM_BALLS = 3

FPS = 30


def main():
    pygame.init()

    screen = pygame.display.set_mode((W, H))

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    balls = [new_ball() for _ in range(NUM_BALLS)]
    score = 0

    global bg, fg
    bg, fg = random_colors()

    while not finished:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                score += handle_click(balls, event)

        update_balls(balls)
        draw_scene(screen, balls)

        pygame.display.update()
        screen.fill(BLACK)

    pygame.quit()
    print(f'Congratulations! Your score is {score}')


def random_colors():
    light = randint(0, 1)
    i1 = randint(0, len(COLORS) - 1)
    i2 = randint(max(0, i1 - 1), min(len(COLORS) - 1, i1 + 1))
    return ALL_COLORS[light][i1], ALL_COLORS[(light + 1) % 2][i2]


def new_ball():
    return Ball(0, 0, W, H)


def update_balls(balls):
    for (i, ball) in enumerate(balls):
        ball.step()
        if not ball.exists():
            balls[i] = new_ball()


def draw_scene(sf, balls):
    sf.fill(bg)
    for ball in balls:
        ball.draw(sf, fg)


cx, cy = W / 2, H / 2


def handle_click(balls, event):
    global bg, fg
    bg, fg = random_colors()

    scores = []
    for (i, ball) in enumerate(balls):
        if ball.hit(event.pos):
            scores.append(round(W * H / ball.area()))
            balls[i] = new_ball()

    score = sum(scores) ** len(scores) if len(scores) > 0 else 0
    if len(scores) == 1:
        print(f'Good shot! You got {score} points')
    elif len(scores) == 2:
        print(f'Double shot! You got {score} points')

    return score


main()
