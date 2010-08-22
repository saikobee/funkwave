from pyglet import clock

from bullet    import Bullet
from intsprite import IntSprite

import math

class ParaFactory(object):
    '''\
    This class manages spawning bullets at a certain rate and making them
    travel a given path determined by a parametric equation.
    '''

    def __init__(self, x, y, sprite, spawn_rate, age_factor=1):
        '''\
        x and y are the parametric functions that determine the
        path bullets take. spawn_rate is how many bullets appear per second.
        '''
        self.x = x
        self.y = y

        self.sprite = sprite

        self.spawn_rate = spawn_rate
        self.age_factor = age_factor

        self.bullets = []

        self.paused = False

        #clock.schedule_interval(self.spawn_bullet, 1.0/spawn_rate)

    def spawn_bullet(self, dt):
        '''\
        Spawns a single bullet.
        '''
        self.bullets.append(Bullet(self.sprite.x, self.sprite.y))

    def update(self, dt):
        '''\
        Ages the bullets the factory manages and updates their positions.
        '''
        if not self.paused:
            for bullet in self.bullets:
                bullet.age += dt
                bullet.xf = self.x(self.age_factor * bullet.age) + bullet.x0
                bullet.yf = self.y(self.age_factor * bullet.age) + bullet.y0

            IntSprite.truncate_list(self.bullets)

    def pause(self):
        '''Pause the creation and aging of bullets.'''
        paused = True
        clock.unschedule(self.spawn_bullet)

    def play(self):
        '''Resume the creation and aging of bullets.'''
        paused = False
        clock.schedule(self.spawn_bullet)

    def toggle(self):
        '''Toggles between play and pause.'''
        if paused: self.play()
        else:      self.pause()

class LineFactory(ParaFactory):
    def __init__(self, angle, sprite, spawn_rate, age_factor=1):
        self.angle = angle

        self.x = lambda t: math.cos(math.radians(angle)) * t
        self.y = lambda t: math.sin(math.radians(angle)) * t

        super(LineFactory, self).__init__(self.x, self.y, sprite, spawn_rate, age_factor)

class Point(object):
    def __init__(point):
        self.x, self.y = point
