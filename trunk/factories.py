from pyglet import clock

from bullet    import Bullet
from intsprite import IntSprite

class ParaFactory:
    '''\
    This class manages spawning bullets at a certain rate and making them
    travel a given path determined by a parametric equation.
    '''

    def __init__(self, x, y, spawn_rate):
        '''\
        x and y are the parametric functions that determine the
        path bullets take. spawn_rate is how many bullets appear per second.
        '''
        self.x = x
        self.y = y

        self.spawn_rate = spawn_rate

        self.bullets = []

        clock.schedule_interval(self.spawn_bullet, 1.0/spawn_rate)

    def spawn_bullet(self, dt):
        '''\
        Spawns a single bullet.
        '''
        self.bullets.append(Bullet())

    def update(self, dt):
        '''\
        Ages the bullets the factory manages and updates their positions.
        '''
        for bullet in self.bullets:
            bullet.age += dt
            bullet.xf = self.x(bullet.age)
            bullet.yf = self.y(bullet.age)

        IntSprite.truncate_list(self.bullets)
