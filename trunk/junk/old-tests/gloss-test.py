#!/usr/bin/python

import sys
import math
import random

from gloss import *

class GlossTest(GlossGame):
    def load_content(self):
        # Also possible from pygame.Surface
        self.bg_tex   = Texture("bg.png")
        self.star_tex = Texture("star.png")

        self.stars = []

        #self.star_count = 1000
        #self.star_count =  500
        #self.star_count =  250
        #self.star_count =  125
        self.star_count =   10
        self.make_init_stars()

        self.eggs = 0

    def make_init_stars(self):
        for i in xrange(self.star_count):
            y = random.randrange(0, 1024)
            x = random.randrange(0,  576)
            self.stars.append(Sprite(self.star_tex, position=(x, y)))

    def draw(self):
        #Gloss.clear(Color.BLACK)
        #Gloss.fill(top=Color.WHITE, bottom=Color.BLACK)
        Gloss.fill(self.bg_tex)
        for star in self.stars:
            #scale = 0.5 + 2**(self.eggs * 5)
            scale = 1
            star.draw(scale=scale, origin=None)

        print "%20s :: %.2f\r" % (Gloss.running_slowly, 1.0/Gloss.elapsed_seconds),
        sys.stdout.flush()

    def on_quit(self):
        print "Bye!"

    def update(self):
        if Gloss.tick_count/1000.0 > 2:
            pass
            #self.quit()

        self.eggs = Gloss.clamp(self.eggs + 0.005, 0, 1)

        for star in self.stars:
            #x = Gloss.lerp(star.position[0], 1024, self.eggs)
            #star.move_to(x, None)
            star.move(+10, 0)
		
game = GlossTest("My Totally Awesome Title: The Sequel")


Gloss.screen_resolution = 1024, 576
#Gloss.full_screen = False

game.run()
