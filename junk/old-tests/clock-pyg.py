#!/usr/bin/python

import os
import math
import random

import pyglet
import rabbyt

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

left   = lambda: 0
top    = lambda: 0
right  = lambda: size[0]
bottom = lambda: size[1]

#FPS = 999
#FPS = 60

# Also possible: (left, top, right, bottom)
# for setting (0, 0) to not be in the center
#rabbyt.set_viewport(size)
rabbyt.set_viewport((left(), top(), right(), bottom()))

#rabbyt.set_default_attribs()

def center_image(img):
    img.anchor_x = img.width /2
    img.anchor_y = img.height/2

pyglet.resource.path = [".", "alpha", "art"]
pyglet.resource.reindex()

star_img = pyglet.resource.image("star.png")

center_image(star_img)

def random_string():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    ret_len = 9
    chars = [alpha[random.randrange(len(alpha))] for i in xrange(ret_len)]
    return ''.join(chars)

class MainWindow(window.Window):
    def __init__(self):
        super(MainWindow, self).__init__(*size, vsync=False)

        self.time = 0

        self.label = pyglet.text.Label(
            'Hello, world', 
            font_name='Courier New', 
            font_size=48,
            #x=self.width//2,
            #y=self.height//2,
            x=math.sin(self.time) + self.width //2,
            y=math.cos(self.time) + self.height//2,
            #x=0,
            #y=0,
            anchor_x='center',
            anchor_y='center'
        )

    def on_draw(self):
        self.clear()
        self.label.draw()

    def update(self, dt):
        self.label.text = "%5.2f" % pyglet.clock.get_fps()
        self.time += dt * 10
        self.label.x += math.sin(self.time)
        self.label.y += math.cos(self.time)

window = MainWindow()
#pyglet.clock.schedule_interval(window.update, 1.0/70.0)
pyglet.clock.schedule_interval(window.update, 1.0/9999.0)
pyglet.app.run()
