from turtle import *
from math import sqrt


dists = [0, 1, sqrt(2), 2]


def read_font(filename):
    with open(filename) as file:
        def format_pair(pair):
            return (int(pair[0]), dists[int(pair[1])])
        return [[[format_pair(pair.split(' '))
                  for pair in path.split(',')] if path != '' else []
                 for path in line.removesuffix('\n').split('|')]
                for line in file.readlines()]


def go_path(path, scale):
    for (angle, dist) in path:
        left(angle)
        forward(dist * scale)


def draw_glyph(glyph, scale):
    go_path(glyph[0], scale)
    pendown()
    go_path(glyph[1], scale)
    penup()
    go_path(glyph[2], scale)


def draw_kern(kern):
    forward(kern)


def draw_number(num, font, height, kern):
    shape('turtle')
    penup()
    for c in str(num):
        draw_glyph(font[int(c)], height / 2)
        draw_kern(kern)


num = input('Enter the number: ')
font = read_font('zip_font')

draw_number(num, font, 100, 20)
