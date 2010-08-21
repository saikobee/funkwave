#!/usr/bin/python
import os
import glob
import math
import random

import rabbyt
import pyglet

from pyglet.gl  import *
from fshelper   import *

from intsprite import IntSprite

random.seed(0)

#num_sprites = 2000
#num_sprites = 1000
#num_sprites =  750
#num_sprites =  500
#num_sprites =  250
#num_sprites =  100
#num_sprites =   50
#num_sprites =   10
#num_sprites =    2
#num_sprites =    1
#num_sprites =    0

from pyglet import font
from pyglet import clock

# Modify this scheduled method to pause, probably
clock.schedule(rabbyt.add_time)

# Silly deprecated code
#clock.set_fps_limit(60)
#clock.set_fps_limit(30)
#clock.set_fps_limit(10)

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

filtered = True
#filtered = False

fps_display = pyglet.clock.ClockDisplay()

pyglet.resource.path = [
    ".",
    "art",
    "alpha",
    "shapes",
    "costumes",
    "backgrounds",
]
pyglet.resource.reindex()

#DAT_IMG = pyglet.resource.image("player.png")
#DAT_IMG = pyglet.resource.image("player2.png")
#DAT_IMG = pyglet.resource.image("player3.png")
#DAT_IMG = pyglet.resource.image("player4.png")
#IDAT_IMG = pyglet.resource.image("player5.png")
#DAT_IMG = pyglet.resource.image("player6.png")
#DAT_IMG = pyglet.resource.image("player7.png")
#DAT_IMG = pyglet.resource.image("alpha4x.png")
#DAT_IMG = pyglet.resource.image("shapes.png")
#DAT_IMG = pyglet.resource.image("shapes2.png")
#DAT_IMG = pyglet.resource.image("shapes.gif")
#DAT_IMG = pyglet.resource.image("faces.png")
#DAT_IMG = pyglet.resource.image("bullet.gif")

def cartesian(polar):
    r, theta = polar

    x = r * math.cos(theta)
    y = r * math.sin(theta)

    x += w/2.0
    y += h/2.0

    return (x, y)

PLAYER_IMG = pyglet.resource.image("brunette.png")

BG_IMG = pyglet.resource.image("bg.png")

i = 0
def g():
    '''Makes a single sprite'''
    global i

    x = random.randrange(w)
    y = random.randrange(h)

    x2 = (x + random.randrange(w)) / 2.0
    y2 = (y + random.randrange(h)) / 2.0

    #sprite = rabbyt.Sprite(DAT_IMG)
    #sprite = rabbyt.Sprite(random.choice(COSTUMES))
    #sprite = rabbyt.Sprite(COSTUMES[i])
    sprite = IntSprite(PLAYER_IMG)
    i += 1

    sprite.xyf = (x, y)

    #sprite.scale = 0.50
    #sprite.scale = 2.00

    #sprite.scale = rabbyt.ease(0.75,   1.25, dt=2, extend="reverse")
    #sprite.rot   = rabbyt.ease(0.00, 360.00, dt=4, extend="reverse")
    #sprite.rot   = rabbyt.ease(-10.00, 10.00, dt=2, extend="reverse")

    #dt_x = abs(x2 - x) / 16.0
    #dt_y = abs(y2 - y) / 16.0

    #sprite.x = rabbyt.ease_out(x, x2, dt=dt_x, extend="reverse")
    #sprite.y = rabbyt.ease_in( y, y2, dt=dt_y, extend="reverse")

    rgb1 = (1.0, 0.0, 0.0)
    rgb2 = (0.0, 1.0, 0.0)
    rgb3 = (0.0, 0.0, 1.0)
    #sprite.rgb   = rabbyt.chain(
    #    rabbyt.lerp(rgb1, rgb2, dt=5),
    #    rabbyt.lerp(rgb2, rgb3, dt=5, extend="reverse")
    #)
    #sprite.red   = rabbyt.lerp(0.50, 1.00, dt=2, extend="reverse")
    #sprite.green = rabbyt.lerp(0.50, 1.00, dt=2, extend="reverse")
    #sprite.blue  = rabbyt.lerp(0.50, 1.00, dt=2, extend="reverse")
    #sprite.alpha = rabbyt.lerp(0.25, 0.75, dt=1, extend="reverse")

    return sprite

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

        self.sprite = g()

        fps_display.label.color = (0.5, 0.5, 0.5, 0.75)

        self.bg = BG_IMG

        self.time = 0

    def update(self, dt):
        self.time += dt

    def on_key_press(self, symbol, modifiers):
        from pyglet.window import key

        if symbol == key.F:
            self.set_fullscreen(not self.fullscreen)
        elif symbol == key.V:
            self.set_vsync(not self.vsync)
        elif symbol == key.ESCAPE:
            self.close()
	elif symbol == key.W:
	    self.sprite.yf += 1
	elif symbol == key.A:
	    self.sprite.xf -= 1
	elif symbol == key.S:
	    self.sprite.yf -= 1
	elif symbol == key.D:
	    self.sprite.xf += 1	
	
	IntSprite.truncate([self.sprite])

    def on_draw(self):
        if self.scale_needed(): self.viewport.begin()

        rabbyt.clear()
        
        self.reset_color_hack()

        self.bg.blit(0, 0, 0)

	self.sprite.render()

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
