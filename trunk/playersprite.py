import pyglet
import rabbyt

from intsprite import IntSprite

class PlayerSprite(IntSprite):
    '''\
    This class helps to manage the tricky business of using a keyboard
    to determine the velocity of a player.
    '''

    #image = pyglet.resource.image("brunette.png")
    #image = pyglet.resource.image("black-hair.png")
    #image = pyglet.resource.image("black-hair2.png")
    image = pyglet.resource.image("spots.png")

    def __init__(self, *args, **kwargs):
        super(PlayerSprite, self).__init__(PlayerSprite.image, *args, **kwargs)

        self.v_max = 100

        self.x_keys = [0]
        self.y_keys = [0]

    def go_left(self):  self.x_keys.append(-1)
    def go_right(self): self.x_keys.append( 1)
    def go_up(self):    self.y_keys.append( 1)
    def go_down(self):  self.y_keys.append(-1)

    def vx(self): return self.x_keys[-1] * self.v_max
    def vy(self): return self.y_keys[-1] * self.v_max

    def stop_left(self):
        if -1 in self.x_keys: self.x_keys.remove(-1)

    def stop_right(self):
        if  1 in self.x_keys: self.x_keys.remove( 1)

    def stop_up(self):
        if  1 in self.y_keys: self.y_keys.remove( 1)

    def stop_down(self):
        if -1 in self.y_keys: self.y_keys.remove(-1)

    def update(self, dt):
        '''\
        Simply update the position based on the current velocities.
        '''
        self.xf += self.vx() * dt
        self.yf += self.vy() * dt
        self.truncate_coords()
