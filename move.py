#!/usr/bin/python
import os
import glob
import math
import random

import rabbyt
import pyglet

pyglet.resource.path = [
    ".",
    "art",
    "alpha",
    "shapes",
    "bullets",
    "costumes",
    "backgrounds",
]
pyglet.resource.reindex()

from pyglet.gl  import *
from fshelper   import *

from playersprite import PlayerSprite
from factories    import ParaFactory

random.seed(0)

from pyglet import font
from pyglet import clock

# Modify this scheduled method to pause, probably
clock.schedule(rabbyt.add_time)

# 16:9
#w, h = size = 1366, 768
#w, h = size = 1280, 720
#w, h = size = 1024, 576
#w, h = size =  800, 450
w, h = size =  640, 360
#w, h = size =  320, 180
#w, h = size =  160,  90

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

#filtered = True
filtered = False

fps_display = pyglet.clock.ClockDisplay()

def cartesian(polar):
    r, theta = polar

    x = r * math.cos(theta)
    y = r * math.sin(theta)

    x += w/2.0
    y += h/2.0

    return (x, y)

PLAYER_IMG = pyglet.resource.image("brunette.png")
BG_IMG     = pyglet.resource.image("bg.png")

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

        self.sprite = PlayerSprite(PLAYER_IMG)
        self.sprite.xyf = (w/4, h/2) 
        #PlayerSprite.truncate(self.sprite)
        self.sprite.truncate_coords()

        self.factory = ParaFactory(
            lambda t: 10*t,
            lambda t: 0,
            self.sprite,
            2,
            #16
            64
        )

        fps_display.label.color = (0.5, 0.5, 0.5, 0.75)

        self.bg = BG_IMG

        self.time = 0

    def update(self, dt):
        self.time += dt

        self.sprite.update(dt)
        self.factory.update(dt)

    def on_key_press(self, symbol, modifiers):
        from pyglet.window import key

        # Simple value toggles
        if symbol == key.F:
            self.set_fullscreen(not self.fullscreen)
        elif symbol == key.V:
            self.set_vsync(not self.vsync)

        elif symbol == key.ESCAPE:
            self.close()

        elif symbol == key.UP:    self.sprite.go_up()
        elif symbol == key.LEFT:  self.sprite.go_left()
        elif symbol == key.DOWN:  self.sprite.go_down()
        elif symbol == key.RIGHT: self.sprite.go_right()

        elif symbol == key.S: self.factory.play()

    def on_key_release(self, symbol, modifiers):
        from pyglet.window import key

        if   symbol == key.UP:    self.sprite.stop_up()
        elif symbol == key.LEFT:  self.sprite.stop_left()
        elif symbol == key.DOWN:  self.sprite.stop_down()
        elif symbol == key.RIGHT: self.sprite.stop_right()

        elif symbol == key.S: self.factory.pause()

    def on_draw(self):
        if self.scale_needed(): self.viewport.begin()

        rabbyt.clear()
        self.reset_color_hack()

        self.bg.blit(0, 0, 0)
        self.sprite.render()
        rabbyt.render_unsorted(self.factory.bullets)

        fps_display.label.draw()

        if self.scale_needed(): self.viewport.end()

    def reset_color_hack(self):
        glColor3f(1.0, 1.0, 1.0)

    def scale_needed(self):
        return not (self.width == w and self.height == h)

def main():
    window_w = w
    window_h = h

    #window_w = 1280
    #window_h =  720
    #window_w = 1024
    #window_h =  576
    #window_w =  800
    #window_h =  450

    window = MainWindow(width=window_w, height=window_h, vsync=False)
    #window = MainWindow(vsync=False, fullscreen=True)
    window.set_caption(
        "moving magic!"
    )
    rabbyt.set_default_attribs()
    #window.push_handlers(pyglet.window.event.WindowEventLogger())
    #pyglet.clock.schedule_interval(window.update, 1.0/70.0)
    #pyglet.clock.schedule_interval(window.update, 1.0/4.0)
    #pyglet.clock.schedule_interval(window.update, 1.0/60.0)
    pyglet.clock.schedule(window.update)
    #pyglet.clock.schedule_interval(window.update, 4.0)
    #pyglet.clock.schedule_interval(window.update, 1.0/120)
    #window.update(0)
    pyglet.app.run()

main()
