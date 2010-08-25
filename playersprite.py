import pyglet
import rabbyt

from intsprite import IntSprite
from shots import Shot1, Shot2

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

        self.v_slow =  75
        self.v_fast = 150

        self.x_keys = [0]
        self.y_keys = [0]

        self.shot_keys = [None]

        self.shots = (Shot1(self), Shot2(self))

    def try_shot1(self): self.shot_keys.append(0)
    def try_shot2(self): self.shot_keys.append(1)

    def stop_shot1(self):
        if 0 in self.shot_keys:
            self.shot_keys.remove(0)

        self.shots[0].pause()

    def stop_shot2(self):
        if 1 in self.shot_keys:
            self.shot_keys.remove(1)

        self.shots[1].pause()

    def velocity(self):
        if not self.shots[1].paused():
            return self.v_slow
        else:
            return self.v_fast

    def go_left(self):  self.x_keys.append(-1)
    def go_right(self): self.x_keys.append( 1)
    def go_up(self):    self.y_keys.append( 1)
    def go_down(self):  self.y_keys.append(-1)

    def vx(self): return self.x_keys[-1] * self.velocity()
    def vy(self): return self.y_keys[-1] * self.velocity()

    def stop_left(self):
        if -1 in self.x_keys: self.x_keys.remove(-1)

    def stop_right(self):
        if  1 in self.x_keys: self.x_keys.remove( 1)

    def stop_up(self):
        if  1 in self.y_keys: self.y_keys.remove( 1)

    def stop_down(self):
        if -1 in self.y_keys: self.y_keys.remove(-1)

    def bullets(self):
        '''Returns all bullets originating from this sprite'''
        ## I hate Python
        return [bullet
            for shot in self.shots
                for bullet in shot.bullets()]
        #return [bullet for bullet in shot.bullets() for shot in self.shots]
        #return sum([shot.bullets() for shot in self.shots], [])
        #return sum(map(lambda shot: shot.bullets(), self.shots), [])

    def update(self, dt):
        '''\
        Simply update the position based on the current velocities.
        '''
        self.xf += self.vx() * dt
        self.yf += self.vy() * dt
        self.truncate_coords()

        i = self.shot_keys[-1]
        if i is not None:
            ## This section of code ensures pressing other buttons
            ## doesn't change shot type
            #if all(map(lambda f: f.paused(), self.shots)):
            #    self.shots[i].play()

            ## This section of code allows other buttons to change
            ## the current shot type
            if self.shots[i].paused():
                for shot in self.shots:
                    shot.pause()
                self.shots[i].play()

        for shot in self.shots:
            shot.update(dt)
