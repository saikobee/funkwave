#!/usr/bin/python

import os
import math
import random

import pyglet
#import rabbyt

from pyglet import window
from pyglet import clock

# 16:9
#size =  640, 360
#size =  800, 450
size = 1024, 576

#left   = lambda: -(size[0]/2)
#right  = lambda:  (size[0]/2)
#bottom = lambda: -(size[1]/2)
#top    = lambda:  (size[1]/2)

from pyglet.gl import *
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

left   = lambda: 0
top    = lambda: size[1]
right  = lambda: size[0]
bottom = lambda: 0

FPS = 999
#FPS = 60

#max_stars = 1000
#max_stars =  500
#max_stars =  250
#max_stars =  100
max_stars =   10
#max_stars =    1

# Also possible: (left, top, right, bottom)
# for setting (0, 0) to not be in the center
#rabbyt.set_viewport(size)
#rabbyt.set_viewport((left(), top(), right(), bottom()))

#rabbyt.set_default_attribs()

def center_image(img):
    img.anchor_x = img.width /2
    img.anchor_y = img.height/2

pyglet.resource.path = [".", "alpha", "art"]
pyglet.resource.reindex()

star_img = pyglet.resource.image("star.png")

center_image(star_img)

class MainWindow(window.Window):
    def __init__(self):
        super(MainWindow, self).__init__(*size, vsync=False)
        #super(MainWindow, self).__init__(*size)

        self.fps_display = pyglet.clock.ClockDisplay()
        self.star_batch = pyglet.graphics.Batch()
        self.groups = [pyglet.graphics.OrderedGroup(i) for i in xrange(4)]
        self.stars = []

        percents = [0.05, 0.10, 0.20, 0.65]
        # Put in the beginning stars
        for layer, percent in enumerate(percents):
            for count in xrange(int(max_stars * percent)):
                self.stars.append(self.make_star2(layer))

    def make_star(self, layer):
        star = pyglet.sprite.Sprite(
            star_img,
            batch=self.star_batch,
            group=self.groups[layer]
        )

        star.layer = layer

        star.x = left()
        star.y = random.randrange(bottom(), top())

        star.scale = self.get_scale(layer)
        star.alpha = self.get_alpha(layer)

        return star

    def make_star2(self, layer):
        star = self.make_star(layer)

        star.x = random.randint(left(), right())

        return star

    def get_scale(self, layer):
        #return (8 * (1.0/4.0) ** layer) + 4
        layer += 1
        return 2 * (1.0/layer)

    def get_alpha(self, layer):
        #layer += 1
        #return 1.0/layer
        return layer/6.0
        #return 1.0

    def on_draw(self):
        self.clear()

        self.fps_display.draw()
        self.star_batch.draw()

    def update(self, dt):
        # Delete those gone too far
        i = 0
        while i < len(self.stars):
            if in_range(self.stars[i]):
               i += 1 
            else:
                lay = self.stars[i].layer
                del self.stars[i]
                self.stars.append(self.make_star(lay))

        # Move the remaining stars
        for star in self.stars:
            star.x += 100 * dt

def in_range(sprite):
    return sprite.x <= right()

window = MainWindow()
pyglet.clock.schedule_interval(window.update, 1.0/70.0)
#pyglet.clock.schedule_interval(window.update, 1.0/120)
pyglet.app.run()
