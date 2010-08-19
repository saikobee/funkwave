#!/usr/bin/python

import os
import math
import random

import pygame
import pyglet
import rabbyt

from pyglet import window
from pyglet import clock

#rabbyt.set_load_texture_file_hook(rabbyt.pyglet_load_texture)
#rabbyt.set_load_texture_file_hook(rabbyt.pygame_load_texture)

# 16:9
#size =  640, 360
#size =  800, 450
size = 1024, 576

#from pyglet.gl import *
#glEnable(GL_BLEND)
#glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

#left   = lambda: -(size[0]/2)
#right  = lambda:  (size[0]/2)
#bottom = lambda: -(size[1]/2)
#top    = lambda:  (size[1]/2)

left   = lambda: 0
top    = lambda: size[1]
right  = lambda: size[0]
bottom = lambda: 0

FPS = 999
#FPS = 60

#max_stars = 1000
#max_stars =  500
max_stars =   10
#max_stars =  1

# Also possible: (left, top, right, bottom)
# for setting (0, 0) to not be in the center
rabbyt.set_viewport(size)
#rabbyt.set_viewport((left(), top(), right(), bottom()))

rabbyt.set_default_attribs()

def center_image(img):
    img.anchor_x = img.width /2
    img.anchor_y = img.height/2

pyglet.resource.path = [".", "alpha", "art"]
pyglet.resource.reindex()

#star_img = pyglet.resource.image("star.png")
star_img = pyglet.resource.image("star.png")

print star_img

center_image(star_img)

class MainWindow(window.Window):
    def __init__(self):
        super(MainWindow, self).__init__(*size, vsync=False)
        #super(MainWindow, self).__init__(*size, vsync=False)

        self.fps_display = pyglet.clock.ClockDisplay()

        self.stars = [make_star2() for x in xrange(max_stars)]

    def on_draw(self):
        self.clear()

        rabbyt.render_unsorted(self.stars)
        self.fps_display.draw()

    def update(self, dt):
        self.stars = filter(in_range, self.stars)
        for i in xrange(max_stars - len(self.stars)):
            self.stars.append(make_star())

def make_star():
    star = rabbyt.Sprite(star_img)
    #star = rabbyt.Sprite("player.png")
    dt = random.randint(1, 8)

    #star.x = rabbyt.lerp(left(), right(), dt=dt)
    star.x = left()
    star.y = random.randrange(bottom(), top())

    star.scale = random.randint(1, 4)
    star.alpha = random.random()

    return star

def make_star2():
    star = make_star()

    x  = random.randint(left(), right())
    dt = random.randint(1, 8)

    #star.x = rabbyt.lerp(x, right(), dt=dt)
    star.x = x

    return star

def move_stars():
    for i, layer in enumerate(layers):
        speed = get_speed(i)
        for sprite in layer:
            sprite.x += speed

def in_range(sprite):
    return sprite.x <= right()

window = MainWindow()
#pyglet.clock.schedule_interval(window.update, 1.0/70.0)
pyglet.clock.schedule_interval(window.update, 1.0/(FPS+10))
pyglet.app.run()
