from intsprite import IntSprite
import pyglet

class Bullet(IntSprite):
    '''\
    This class manages one bullet.
    '''

    image = pyglet.resource.image("bullet.png")
 
    def __init__(self, x0, y0):
        super(Bullet, self).__init__(Bullet.image) 
        self.age = 0 
        self.x0 = x0
        self.y0 = y0

    def __repr__(self):
        return "Bullet<xyf=(%f, %f), xy=(%i, %i), age=%i>" % (self.xf, self.yf, self.x, self.y, self.age)
