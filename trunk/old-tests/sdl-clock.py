#!/usr/bin/python

import pygame
import random
import os
from pygame.locals import *

size = 1024, 576

left   = lambda: -(size[0]/2)
right  = lambda:  (size[0]/2)
bottom = lambda: -(size[1]/2)
top    = lambda:  (size[1]/2)

the_clock = pygame.time.Clock()

FPS = 999
#FPS = 60

video_opts = OPENGL | DOUBLEBUF
#video_opts = HWSURFACE | DOUBLEBUF

# setup window
pygame.init()
pygame.display.set_mode(size, video_opts)

pygame.mouse.set_visible(False)

# Also possible: (left, top, right, bottom)
# for setting (0, 0) to not be in the center
#rabbyt.set_viewport(size)
#rabbyt.set_viewport(size)

#rabbyt.set_default_attribs()

# the gameloop
keep_running = True

font_name = pygame.font.match_font("Courier New")
the_font = pygame.font.Font(font_name, 48)

def get_fps_sprite(fps):
    color = (255, 255, 255)
    img  = the_font.render(fps, True, color)
    img  = pygame.transform.flip(img, True, False)
    star = rabbyt.Sprite(surface_to_texture_id(img), img.get_size())

    return star

def surface_to_texture_id(surf):
    surf = pygame.transform.flip(surf, True, True)
    size = surf.get_size()
    txt  = pygame.image.tostring(surf, "RGBA")
    
    return gfx.gl.load_texture(txt, size)

def toggle_fullscreen():
    global video_opts
    video_opts ^= FULLSCREEN
    pygame.display.set_mode(size, video_opts)

def handle_events():
    global keep_running
    # messagepump
    for event in pygame.event.get():
        if event.type == QUIT:
            keep_running = False

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                keep_running = False
            if event.key == K_f:
                toggle_fullscreen()

while keep_running:
    handle_events()

    #rabbyt.clear()
    color = (0.05, 0.05, 0.20)
    #color = (1.00, 1.00, 1.00)
    #color = (1.00, 1.00, 1.00)
    #rabbyt.clear(color)

    # Sprite
    the_fps = 'FPS: %6.2f' % the_clock.get_fps()

    #the_sprite = get_fps_sprite(the_fps)
    #the_sprite.render()

    # Blit
    img  = the_font.render(the_fps, True, color)
    img.blit(pygame.display.get_surface(), (0, 0))
    #print "\r",
    pygame.display.flip()
    the_clock.tick(FPS)
