from intsprite import IntSprite

class Bullet(IntSprite):
    '''\
    This class manages one bullet.
    '''

    image = pygame.resource.image("bullet.png")
 
    def __init__(self):
        super(Bullet, self).__init__(Bullet.image) 
        self.age = 0 
