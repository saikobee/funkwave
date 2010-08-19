#!/usr/bin/python

import rabbyt
import pygame
from pygame.locals import *

size = 640, 480

# setup window
pygame.init()
pygame.display.set_mode(size, pygame.OPENGL | pygame.DOUBLEBUF)
rabbyt.set_viewport(size)
rabbyt.set_default_attribs()

# load our sprite
my_sprite = rabbyt.Sprite("test.png")

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


while keep_running:
    handle_events()
    rabbyt.clear()
    my_sprite.render()
    pygame.display.flip()
