import math
from turtle import st
import pygame
import random
from ball import Ball
from sys import float_info
import time

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

FPS = 30

bg_colors = [BLACK, WHITE]
fg_colors = LIGHT_COLORS


class Game:
    def __init__(self):
        self.update_bg_color()
        self.score_loss = 3
        self.num_balls = 3

    def update_bg_color(self, prev=None):
        self.bg = random_bg_color(prev)
        self.bg_inverse = random_bg_color(self.bg)

    def loop(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
        self.font32 = pygame.font.SysFont(None, 32)

        pygame.display.update()
        clock = pygame.time.Clock()
        finished = False

        self.begin_game()

        while not finished:
            clock.tick(FPS)

            if not self.game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        finished = True
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        self.handle_click(event)
                self.update_balls()
                self.draw_scene()
                self.score -= self.score_loss
                if self.score < 0:
                    self.end_game()
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        finished = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.begin_game()

            pygame.display.update()

        pygame.quit()

    def begin_game(self):
        self.balls = [new_ball() for _ in range(self.num_balls)]
        self.max_score = 1000
        self.score = self.max_score
        self.game_over = False
        self.start = time.time()

    def end_game(self):
        self.game_over = True
        duration = time.time() - self.start
        text = self.font32.render(
            f'Game over. Your played {round(duration, 3)}s',
            True,
            self.bg_inverse,
        )
        clip = text.get_clip()
        self.screen.blit(text, ((W - clip.w) / 2, (H - clip.h) / 2))

    def update_balls(self):
        for (i, ball) in enumerate(self.balls):
            ball.step()
            if not ball.exists():
                self.balls[i] = new_ball()

    def draw_scene(self):
        self.screen.fill(self.bg)
        for ball in self.balls:
            ball.draw(self.screen)
        self.draw_bar()

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
            add_score = W * H * sum(add_scores) * len(add_scores)
        else:
            self.update_bg_color(self.bg)
            add_score = -W * H / (math.pi * nearest_dist_squared)

        self.score = min(self.score + add_score, self.max_score)

    def draw_bar(self):
        fg = self.bg_inverse

        screen_w = self.screen.get_clip().w
        pad_lr = screen_w / 4
        pad_t = 16
        h = 24
        border_w = 2
        pygame.draw.rect(self.screen, fg, (
            pad_lr,
            pad_t,
            screen_w - 2 * pad_lr,
            h,
        ), border_w)

        inset_w = border_w + 1
        pygame.draw.rect(self.screen, fg, (
            pad_lr + inset_w,
            pad_t + inset_w,
            int((screen_w - 2 * (pad_lr + inset_w))
                * min(self.score / self.max_score, 1)),
            h - inset_w - border_w,
        ))


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
