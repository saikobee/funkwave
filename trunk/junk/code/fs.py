#!/usr/bin/python
import math
import random

import rabbyt
import pyglet

from fshelper import *

random.seed(0)

#num_sprites = 2000
#num_sprites = 1000
num_sprites =  500
#num_sprites =  250
#num_sprites = 100
#num_sprites = 10
#num_sprites = 2
#num_sprites = 1
#num_sprites = 0
#num_sprites = 200

from pyglet import font
from pyglet import clock

# Modify this scheduled method to pause, probably
clock.schedule(rabbyt.add_time)

#clock.set_fps_limit(60)
#clock.set_fps_limit(30)
#clock.set_fps_limit(10)

# 16:9
#w, h = size = 1280, 720
#w, h = size = 1024, 576
#w, h = size =  800, 450
#w, h = size =  640, 360
#w, h = size =  320, 240

# 3:4
#w, h = size = 800, 600
w, h = size = 640, 480

# 16:10
#w, h = size = 1680, 1050
#w, h = size =  640,  400
#w, h = size =  320,  200
#w, h = size =  160,  100

fps_display = pyglet.clock.ClockDisplay()

pyglet.resource.path = [
    ".",
    "alpha",
    "art",
    "shapes",
]
pyglet.resource.reindex()

#DAT_IMG = pyglet.resource.image("player.png")
#DAT_IMG = pyglet.resource.image("alpha4x.png")
#DAT_IMG = pyglet.resource.image("shapes.png")
DAT_IMG = pyglet.resource.image("faces.png")
#DAT_IMG = pyglet.resource.image("bullet.gif")

def g():
    x = random.randrange(w)
    y = random.randrange(h)

    sprite = rabbyt.Sprite(DAT_IMG)

    sprite.shape.width  = 32
    sprite.shape.height = 32 

    # TODO: Not exact!
    #sprite.tex_shape.width  = 1.0/3.0/3.0
    sprite.tex_shape.width  = 1.0/8.0
    sprite.tex_shape.height = 1.0/8.0
    sprite.tex_shape.left   = 0
    sprite.tex_shape.bottom = 0

    # TODO: WHY DOES THIS WORK
    #sprite.u = rabbyt.lerp(0, 1.0/4.0, dt=4, extend="constant")

    sprite.xy = (x, y)

    sprite.scale = rabbyt.ease(0.25,   1.50, dt=1, extend="reverse")
    sprite.rot   = rabbyt.ease(0.00, 360.00, dt=1, extend="extrapolate")

    sprite.x = rabbyt.ease_out(x-50, x+50, dt=1, extend="reverse")
    sprite.y = rabbyt.ease_in( y+50, y-50, dt=1, extend="reverse")

    rgb1 = (1.0, 0.0, 0.0)
    rgb2 = (0.0, 1.0, 0.0)
    rgb3 = (0.0, 0.0, 1.0)
    #sprite.rgb   = rabbyt.chain(
    #    rabbyt.lerp(rgb1, rgb2, dt=5),
    #    rabbyt.lerp(rgb2, rgb3, dt=5, extend="reverse")
    #)
    sprite.red   = rabbyt.lerp(0.50, 1.00, dt=2, extend="reverse")
    sprite.green = rabbyt.lerp(0.50, 1.00, dt=4, extend="reverse")
    sprite.blue  = rabbyt.lerp(0.50, 1.00, dt=8, extend="reverse")
    sprite.alpha = rabbyt.lerp(0.25, 0.75, dt=1, extend="reverse")

    return sprite

sprites = [g() for i in xrange(num_sprites)]

class MainWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.viewport = FixedResolutionViewport(
            self, w, h,
            filtered=False
            #filtered=True
        )

        self.set_mouse_visible(False)

    def update(self, dt):
        for sprite in sprites:
            vals = [0.00, 0.25/1, 0.25/2]
            n = len(vals)
            sprite.u = vals[random.randrange(n)]

    def on_key_press(self, symbol, modifiers):
        from pyglet.window import key

        if symbol == key.F:
            self.set_fullscreen(not self.fullscreen)
        elif symbol == key.V:
            self.set_vsync(not self.vsync)
        elif symbol == key.ESCAPE:
            self.close()

    def on_draw(self):
        if self.fullscreen: self.viewport.begin()

        rabbyt.clear()
        rabbyt.render_unsorted(sprites)

        fps_display.label.color = (0.0, 0.0, 0.0, 0.5)
        fps_display.label.draw()
        fps_display.label.color = (1.0, 1.0, 1.0, 0.5)
        fps_display.label.draw()

        if self.fullscreen: self.viewport.end()

def other_main():
    #window = MainWindow(width=w, height=h, vsync=False)
    window = MainWindow(vsync=False, fullscreen=True)
    # See bookmarks for scaling...
    #window = MainWindow(width=w, height=h, vsync=False, fullscreen=True)
    #window = MainWindow(width=w, height=h, vsync=True)
    window.set_caption(
        "%i sprites :: Super Ultimate Sprite Machine Factory Window" % num_sprites
    )
    rabbyt.set_default_attribs()
    #window.push_handlers(pyglet.window.event.WindowEventLogger())
    #pyglet.clock.schedule_interval(window.update, 1.0/70.0)
    pyglet.clock.schedule_interval(window.update, 1.0/4.0)
    #pyglet.clock.schedule_interval(window.update, 1.0/120)
    pyglet.app.run()

#main_loop()
other_main()
