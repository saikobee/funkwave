#!/usr/bin/python

import rabbyt
import pygame
import random
import random
from pygame.locals import *

size = 640, 480
#size = 640, 360
#size = 1680, 1050
#size = 1280, 720

#sprite_count = 1000
#sprite_count = 500
#sprite_count = 250
#sprite_count = 125

the_clock = pygame.time.Clock()

FPS = 999

# setup window
pygame.init()
pygame.display.set_mode(size, OPENGL | DOUBLEBUF)
#pygame.display.set_mode(size, OPENGL | DOUBLEBUF | FULLSCREEN)

pygame.mouse.set_visible(False)

# Also possible: (left, top, right, bottom)
# for setting (0, 0) to not be in the center
#rabbyt.set_viewport(size)
rabbyt.set_viewport(size)

rabbyt.set_default_attribs()

# the gameloop
keep_running = True

def handle_events():
    global keep_running
    # messagepump
    for event in pygame.event.get():
        if event.type == QUIT:
            keep_running = False

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                keep_running = False

def get_scale(layer):
    #return (8 * (1.0/4.0) ** layer) + 4
    layer += 1
    return 4.0 / layer

def get_speed(layer):
    return 4 * (1.0/2.0) ** layer

def chance(percentage):
    return random.randrange(100) < percentage

def make_star(layer):
    star = rabbyt.Sprite("star.png")
    star.x = -320
    star.y = random.randint(-240, 240)
    star.scale = get_scale(layer)

    return star

def move_stars():
    for i, layer in enumerate(layers):
        speed = get_speed(i)
        for sprite in layer:
            sprite.x += speed

def in_range(sprite):
    return sprite.x <= 320

num_layers = 8

layers = [[] for x in xrange(num_layers)]
star_count = 0

frames = 0
while keep_running:
    handle_events()

    #rabbyt.clear()
    color = (0.05, 0.05, 0.20)
    rabbyt.clear(color)

    if chance( 5): layers[0].append(make_star(0))
    #if chance( 5): layers[1].append(make_star(1))
    if chance( 5): layers[2].append(make_star(2))
    #if chance( 5): layers[3].append(make_star(3))
    if chance( 5): layers[4].append(make_star(4))
    #if chance( 5): layers[5].append(make_star(5))
    if chance( 5): layers[6].append(make_star(6))
    #if chance( 5): layers[7].append(make_star(7))

    move_stars()

    for layer in reversed(layers):
        rabbyt.render_unsorted(layer)
    #for layer in layers:
    #    rabbyt.render_unsorted(layer)

    #if frames == 60 * 5:
    #    pygame.display.set_mode(size, OPENGL | DOUBLEBUF | FULLSCREEN)
    #if frames == 60 * 10:
    #    pygame.display.set_mode(size, OPENGL | DOUBLEBUF)

    layers = [filter(in_range, layer) for layer in layers]

    pygame.display.set_caption('FPS: %6.2f' % the_clock.get_fps())
    star_count = sum(map(len, layers))
    print star_count, "\r",
    #print "\r",
    pygame.display.flip()
    the_clock.tick(FPS)
    frames += 1
