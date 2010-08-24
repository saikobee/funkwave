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

        self.paused = True

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
        for bullet in self.bullets:
            bullet.age += dt
            bullet.xf = self.x(self.age_factor * bullet.age) + bullet.x0
            bullet.yf = self.y(self.age_factor * bullet.age) + bullet.y0

        IntSprite.truncate_list(self.bullets)

    def pause(self):
        '''Pause the creation and aging of bullets.'''
        self.paused = True
        clock.unschedule(self.spawn_bullet)

    def play(self):
        '''Resume the creation and aging of bullets.'''
        self.paused = False
        self.spawn_bullet(0)
        clock.schedule_interval(self.spawn_bullet, 1.0/self.spawn_rate)

    def toggle(self):
        '''Toggles between play and pause.'''
        if selfpaused: self.play()
        else:          self.pause()

class LineFactory(ParaFactory):
    '''LineFactory makes a ParaFactory using an angle for a line.'''

    def __init__(self, angle, sprite, spawn_rate, age_factor=1):
        '''angle is the angle of the line in degrees.'''
        self.angle = angle

        x = lambda t: math.cos(math.radians(angle)) * t
        y = lambda t: math.sin(math.radians(angle)) * t

        super(LineFactory, self).__init__(x, y, sprite, spawn_rate, age_factor)

class PolarFactory(ParaFactory):
    '''PolarFactory makes a ParaFactory using a polar equation.'''

    def __init__(self, r, sprite, spawn_rate, age_factor=1):
        '''r is a function from an angle to a radius.'''
        self.r = r

        x = lambda t: self.r(t) * math.cos(math.radians(t))
        y = lambda t: self.r(t) * math.sin(math.radians(t))

        super(PolarFactory, self).__init__(x, y, sprite, spawn_rate, age_factor)

class Point(object):
    def __init__(point):
        self.x, self.y = point
