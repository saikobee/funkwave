#!/usr/bin/python

import rabbyt
import pygame
import gfx
import gfx.gl
import random
import os
from pygame.locals import *

# 3:4
#size =  640, 480

# 16:9
#size =  640, 360
#size =  800, 450
size = 1024, 576

# JK
#size = 1680, 1050
#size = 1600, 1000

# Bad
#size = 1280, 720
#size = 1366, 768

left   = lambda: -(size[0]/2)
right  = lambda:  (size[0]/2)
bottom = lambda: -(size[1]/2)
top    = lambda:  (size[1]/2)

#sprite_count = 1000
#sprite_count = 500
#sprite_count = 250
#sprite_count = 125

the_clock = pygame.time.Clock()

FPS = 999
#FPS = 60

video_opts = OPENGL | DOUBLEBUF

# setup window
pygame.init()
pygame.display.set_mode(size, video_opts)

pygame.mouse.set_visible(False)

# Also possible: (left, top, right, bottom)
# for setting (0, 0) to not be in the center
#rabbyt.set_viewport(size)
rabbyt.set_viewport(size)

rabbyt.set_default_attribs()

# the gameloop
keep_running = True

file =  "star.png"
img = pygame.image.load(file).convert_alpha()

def random_letter():
    star = rabbyt.Sprite(surface_to_texture_id(img), img.get_size())

    return star

def surface_to_texture_id(surf):
    surf = pygame.transform.flip(surf, True, True)
    size = surf.get_size()
    txt  = pygame.image.tostring(surf, "RGBA")
    
    return gfx.gl.load_texture(txt, size)

def toggle_fullscreen():
    global video_opts
    video_opts ^= FULLSCREEN
    pygame.display.set_mode(size, video_opts)

def handle_events():
    global keep_running
    # messagepump
    for event in pygame.event.get():
        if event.type == QUIT:
            keep_running = False

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                keep_running = False
            if event.key == K_f:
                toggle_fullscreen()

def get_scale(layer):
    #return (8 * (1.0/4.0) ** layer) + 4
    layer += 1
    return 2 * (1.0/layer)

def get_alpha(layer):
    #layer += 1
    #return 1.0/layer
    #return layer/6.0
    return 1.0

def get_speed(layer):
    return 4 * (0.5 ** layer)

def make_star(layer):
    star = random_letter()
    #star = rabbyt.Sprite("star.png")
    #star = rabbyt.Sprite(letter_filename(letter))
    #star = rabbyt.Sprite(pygame.image.load(random_letter_filename()))
    star.x = left()
    star.y = random.randint(bottom(), top())

    star.scale = get_scale(layer)
    star.alpha = get_alpha(layer)

    #star.tex_shape = (0, 1, 1, 0)
    #star.tex_shape = (0, 0.5, 0.5, 0)
    #star.tex_shape = (0.5, 0.5, 0.5, 0.5)

    return star

def make_star2(layer):
    star = make_star(layer)
    star.x = random.randint(left(), right())

    return star

def move_stars():
    for i, layer in enumerate(layers):
        speed = get_speed(i)
        for sprite in layer:
            sprite.x += speed

def in_range(sprite):
    return sprite.x <= right()

num_layers = 4

layers = [[] for x in xrange(num_layers)]
star_count = 0

#max_stars =   50
#max_stars =  100
#max_stars =  250
max_stars =  500
#max_stars = 1000

# Make sure the numbers add up to 1
percents = [0.05, 0.10, 0.20, 0.65]
# Put in the beginning stars
for layer, percent in enumerate(percents):
    for count in xrange(int(max_stars * percent)):
        layers[layer].append(make_star2(layer))

while keep_running:
    handle_events()

    #rabbyt.clear()
    color = (0.05, 0.05, 0.20)
    #color = (1.00, 1.00, 1.00)
    #color = (1.00, 1.00, 1.00)
    rabbyt.clear(color)

    move_stars()

    #for layer in reversed(layers):
    #    rabbyt.render_unsorted(layer)
    for layer in layers:
        rabbyt.render_unsorted(layer)

    #layers = [filter(in_range, layer) for layer in layers]

    for n, layer in enumerate(layers):
        i = 0
        while i < len(layer):
            if in_range(layer[i]):
               i += 1 
            else:
                del layer[i]
                layer.append(make_star(n))

    pygame.display.set_caption('FPS: %6.2f' % the_clock.get_fps())
    star_count = sum(map(len, layers))
    print star_count, "\r",
    #print "\r",
    pygame.display.flip()
    the_clock.tick(FPS)
