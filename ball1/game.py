import math
import pygame
from random import randint
import random
from ball import Ball
from sys import float_info

BLACK = (22, 22, 22)
WHITE = (244, 244, 244)

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

ALL_COLORS = COLORS + LIGHT_COLORS

W, H = 1200, 700

NUM_BALLS = 3

FPS = 30

bg_colors = [BLACK, WHITE]
fg_colors = LIGHT_COLORS


class Game:
    def __init__(self):
        self.bg = random_bg_color()

    def loop(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
        self.font = pygame.font.SysFont(None, 24)

        pygame.display.update()
        clock = pygame.time.Clock()
        finished = False

        self.balls = [new_ball() for _ in range(NUM_BALLS)]
        self.score = 0

        while not finished:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event)

            self.update_balls()
            self.draw_scene()

            pygame.display.update()

        pygame.quit()
        print(f'Congratulations! Your score is {self.score}')

    def update_balls(self):
        for (i, ball) in enumerate(self.balls):
            ball.step()
            if not ball.exists():
                self.balls[i] = new_ball()

    def draw_scene(self):
        self.screen.fill(self.bg)
        for ball in self.balls:
            ball.draw(self.screen)

    def handle_click(self, event):
        add_scores = []
        nearest_dist_squared = float_info.max
        for (i, ball) in enumerate(self.balls):
            dist_squared = ball.dist_squared(event.pos)
            if dist_squared < ball.r ** 2:
                add_scores.append(1 / ball.area())
                self.balls[i] = new_ball()
            elif dist_squared < nearest_dist_squared:
                nearest_dist_squared = dist_squared

        if len(add_scores) > 0:
            add_score = round((W * H * sum(add_scores)) *len(add_scores))
        else:
            self.bg = random_bg_color(self.bg)
            add_score = -round(W * H / (math.pi * nearest_dist_squared))

        if len(add_scores) == 0:
            print(f'Miss! You lost {-add_score} points')
        if len(add_scores) == 1:
            print(f'Good shot! You got {add_score} points')
        elif len(add_scores) == 2:
            print(f'Double shot! You got {add_score} points')

        self.score += add_score


def random_near_color(i, j):
    colors = []
    for k in range(max(0, i - 1), min(i + 1, len(COLORS) - 1) + 1):
        if k != j:
            colors.append(k)
    return random.choice(colors)


def new_ball():
    return Ball(random_fg_color(), 0, 0, W, H)


def random_bg_color(without=None):
    return random.choice([c for c in bg_colors if c != without])


def random_fg_color(without=None):
    return random.choice([c for c in fg_colors if c != without])
