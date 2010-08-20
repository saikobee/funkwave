#!/usr/bin/python
import os
import glob
import math
import random

import rabbyt
import pyglet

from pyglet.gl  import *
from fshelper   import *

from pyglet import font
from pyglet import clock

# Modify this scheduled method to pause, probably
clock.schedule(rabbyt.add_time)

# 16:9
#w, h = size = 1366, 768
#w, h = size = 1280, 720
#w, h = size = 1024, 576
w, h = size =  800, 450
#w, h = size =  640, 360
#w, h = size =  320, 180

# 3:4
#w, h = size = 800, 600
#w, h = size = 640, 480

# 16:10
#w, h = size = 1680, 1050
#w, h = size = 1440,  900
#w, h = size = 1280,  800
#w, h = size =  640,  400
#w, h = size =  320,  200
#w, h = size =  160,  100

filtered = True
#filtered = False

fps_display = pyglet.clock.ClockDisplay()

pyglet.resource.path = [
    ".",
    "art",
    "costumes",
    "backgrounds",
]
pyglet.resource.reindex()

def cartesian(polar):
    r, theta = polar

    x = r * math.cos(theta)
    y = r * math.sin(theta)

    x += w/2.0
    y += h/2.0

    return (x, y)

class MainWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.viewport = FixedResolutionViewport(
            self, w, h,
            #filtered=False
            #filtered=True
            filtered=filtered
        )

        self.set_mouse_visible(False)

        self.time = 0

    def update(self, dt):
        self.time += dt
        # update game world

    def on_key_press(self, symbol, modifiers):
        from pyglet.window import key

        if symbol == key.F:
            self.set_fullscreen(not self.fullscreen)
        elif symbol == key.V:
            self.set_vsync(not self.vsync)
        elif symbol == key.ESCAPE:
            self.close()

    def on_draw(self):
        if self.scale_needed(): self.viewport.begin()

        rabbyt.clear()
        self.reset_color_hack()

        self.draw_fps()

        if self.scale_needed(): self.viewport.end()

    def reset_color_hack(self):
        glColor3f(1.0, 1.0, 1.0)

    def scale_needed(self):
        return not (self.width == w and self.height == h)

    def draw_fps(self):
        fps_display.label.color = (0.0, 0.0, 0.0, 0.75)
        fps_display.label.draw()
        fps_display.label.color = (1.0, 1.0, 1.0, 0.50)
        fps_display.label.draw()

def main():
    window_w = w
    window_h = h

    #window_w = 1280
    #window_h =  720

    window = MainWindow(width=window_w, height=window_h, vsync=False)
    #window = MainWindow(vsync=False, fullscreen=True)
    window.set_caption(
        "%i sprites :: Super Ultimate Sprite Machine Factory Window" % num_sprites
    )
    rabbyt.set_default_attribs()
    #pyglet.clock.schedule_interval(window.update, 1.0/60.0)
    pyglet.clock.schedule_interval(window.update)
    pyglet.app.run()

main()
