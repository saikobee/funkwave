#!/usr/bin/python

import rabbyt
import pygame
import random
import gfx
import gfx.gl
from pygame.locals import *

#size = 640, 480
#size = 640, 360
#size = 1680, 1050
#size = 1280, 720
#size = 1024, 576
size = 1024, 768

#sprite_count = 1000
#sprite_count = 500
sprite_count = 250
#sprite_count = 125

the_clock = pygame.time.Clock()

bullets = []

FPS = 999
#FPS = 60

video_opts = OPENGL | DOUBLEBUF

# setup window
pygame.init()
pygame.display.set_mode(size, video_opts)

pygame.mouse.set_visible(False)

def toggle_fullscreen():
    global video_opts
    video_opts ^= FULLSCREEN
    pygame.display.set_mode(size, video_opts)

# Also possible: (left, top, right, bottom)
# for setting (0, 0) to not be in the center
#rabbyt.set_viewport(size)
rabbyt.set_viewport(size)

rabbyt.set_default_attribs()

# load our sprite
def surface_to_texture_id(surf):
    surf = pygame.transform.flip(surf, True, True)
    size = surf.get_size()
    txt  = pygame.image.tostring(surf, "RGBA")
    
    return gfx.gl.load_texture(txt, size)

sprite_surf = pygame.image.load("bullet.png").convert_alpha()
sprite_id   = surface_to_texture_id(sprite_surf)

sprites = [rabbyt.Sprite(sprite_id, sprite_surf.get_size()) for x in xrange(sprite_count)]
player  = rabbyt.Sprite("player.png")
bg      = rabbyt.Sprite("bg.png")

for sprite in sprites:
    #sprite.scale = 1
    #sprite.scale = 0.5
    #sprite.scale = 0.66
    #sprite.scale = 0.50
    #sprite.scale = 0.33
    pass

# Not needed
#player.x, player.y = 0, 0

# the gameloop
keep_running = True

held = {
    'up'   : False,
    'down' : False,
    'left' : False,
    'right': False,

    'focus-up'   : False,
    'focus-down' : False,
    'focus-left' : False,
    'focus-right': False,

    'shoot': False,
}
controls = {
    'up'   : K_UP,
    'down' : K_DOWN,
    'left' : K_LEFT,
    'right': K_RIGHT,

    'focus-up'   : K_i,
    'focus-down' : K_k,
    'focus-left' : K_j,
    'focus-right': K_l,

    'shoot': K_SPACE,
}
game_settings = {
    'speed'       :  2.0,
    'focus-speed' : 16.0,
    'bullet-speed':  4.0,
}

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

            for control in held.iterkeys():
                if event.key == controls[control]:
                    held[control] = True

        # If keys are let go, actions should stop happening, or start
        if event.type == KEYUP:
            for control in held.iterkeys():
                if event.key == controls[control]:
                    held[control] = False

def cartesian(polar):
    '''This function converts a polar point (r, theta) to a cartesian point (x, y)'''
    import math

    r, theta = polar
    
    x = r * math.cos(theta)
    y = r * math.sin(theta)

    return (x, y)

CTR   = 0
CTR_V = 0.001
LIMIT = size[1]

def get_values(x, f):
    import math

    global CTR
    global LIMIT

    x += CTR
    x %= LIMIT

    CTR += CTR_V

    polar = (x, f(x))
    return cartesian(polar)

def move_sprites():
    # Needs outer IF so you can't do regular and focus-speed together
    if any(held[x] for x in ('up', 'down', 'left', 'right')):
        if held['up']:    player.y +=  game_settings['speed']
        if held['down']:  player.y += -game_settings['speed']
        if held['left']:  player.x += -game_settings['speed']
        if held['right']: player.x +=  game_settings['speed']
    else:
        if held['focus-up']:    player.y +=  game_settings['focus-speed']
        if held['focus-down']:  player.y += -game_settings['focus-speed']
        if held['focus-left']:  player.x += -game_settings['focus-speed']
        if held['focus-right']: player.x +=  game_settings['focus-speed']

    for i, sprite in enumerate(sprites):
        sprite.x, sprite.y = get_values(i, lambda x: x/8.0)
        #sprite.y = get_value(i)

def maybe_shoot():
    if held['shoot']:
        shot = rabbyt.Sprite("bullet.png")
        shot.x = player.x
        shot.y = player.y
        shot.scale = 0.25
        bullets.append(shot)

def move_bullets():
    for bullet in bullets:
        bullet.x += game_settings['bullet-speed']

while keep_running:
    handle_events()

    rabbyt.clear()

    maybe_shoot()

    move_sprites()
    move_bullets()

    bg.render()
    player.render()
    # This seems to get about 1FPS more, oh boy
    rabbyt.render_unsorted(bullets)
    rabbyt.render_unsorted(sprites)

    #pygame.display.set_caption("%i objects" % len(sprites))
    pygame.display.set_caption('FPS: %6.2f' % the_clock.get_fps())
    pygame.display.flip()
    the_clock.tick(FPS)
    #print ('FPS: %6.2f\r' % the_clock.get_fps()),
