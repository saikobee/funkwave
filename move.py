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
from shots        import Shot1, Shot2
from const        import *

random.seed(0)

# Modify this scheduled method to pause, probably
pyglet.clock.schedule(rabbyt.add_time)

class MainWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.viewport = FixedResolutionViewport(
            self, WIDTH, HEIGHT,
            filtered=FILTERED
        )

        self.set_mouse_visible(False)

        self.sprite = PlayerSprite()
        self.sprite.xyf = (WIDTH/4, HEIGHT/2) 
        #PlayerSprite.truncate(self.sprite)
        self.sprite.truncate_coords()

        self.fps_display = pyglet.clock.ClockDisplay()

        #self.factory = ParaFactory(
        #    lambda t: 10*t,
        #    lambda t: 0,
        #    self.sprite,
        #    2,
        #    #16
        #    64
        #)

        self.text_colorf = (0.50, 0.50, 0.50, 0.75)
        self.text_colori = ( 128,  128,  128,  224)

        self.bg = pyglet.resource.image("bg.png")

        self.time = 0

        self.collisions = 0

        self.coll_ctr = pyglet.text.Label(
            anchor_x="right",
            anchor_y="bottom",
            halign="right",
            x=WIDTH - 10,
            y=5,
            bold=True,
            font_size=16,
            color=self.text_colori
        )

        self.fps_display.label.color = self.text_colorf
        #self.fps_display.label.color = self.text_colori

    def update(self, dt):
        self.time += dt

        self.sprite.update(dt)
        
        self.detect_collisions()

    def detect_collisions(self):
        collisions = rabbyt.collisions.collide_single(
            self.sprite,
            self.sprite.bullets()
        )
        self.collisions += len(collisions)
        self.coll_ctr.text = "%i" % self.collisions

    def on_draw(self):
        if self.scale_needed(): self.viewport.begin()

        rabbyt.clear()
        self.reset_color_hack()

        self.bg.blit(0, 0, 0)
        self.sprite.render()

        for shot in self.sprite.shots:
            for factory in shot.factories:
                rabbyt.render_unsorted(factory.bullets)

        self.fps_display.label.draw()
        self.coll_ctr.draw()

        if self.scale_needed(): self.viewport.end()

    def reset_color_hack(self):
        glColor3f(1.0, 1.0, 1.0)

    def scale_needed(self):
        return not (self.width == WIDTH and self.height == HEIGHT)

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

        elif symbol == key.A: self.sprite.try_shot1()
        elif symbol == key.S: self.sprite.try_shot2()

    def on_key_release(self, symbol, modifiers):
        from pyglet.window import key

        if   symbol == key.UP:    self.sprite.stop_up()
        elif symbol == key.LEFT:  self.sprite.stop_left()
        elif symbol == key.DOWN:  self.sprite.stop_down()
        elif symbol == key.RIGHT: self.sprite.stop_right()

        elif symbol == key.A: self.sprite.stop_shot1()
        elif symbol == key.S: self.sprite.stop_shot2()

def main():
    window_w = WIDTH
    window_h = HEIGHT

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
