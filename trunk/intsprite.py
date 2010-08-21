import rabbyt

class IntSprite(rabbyt.Sprite):
    '''\
    This class manages a floating point location for a sprite while
    giving integer locations to the rendering engine so we don't get
    blurry sprites centered at locations like (1.333, 3.14159).
    '''

    xf  = rabbyt.anim_slot()
    yf  = rabbyt.anim_slot()
    xyf = rabbyt.swizzle("xf", "yf")
    
    @staticmethod
    def truncate(*sprites):
        '''\
        Like truncate_coords, but operates on a slurpy list of args.
        '''
        for sprite in sprites:
            sprite.x = int(sprite.xf)
            sprite.y = int(sprite.yf)

    @staticmethod
    def truncate_list(sprites):
        '''\
        Like truncate_coords, but operates on a list of args.
        '''
        self.truncate(*sprites)

    def truncate_coords(self):
        '''\
        Sets the x and y values to the integer portions of their floating
        point counterparts, xf and yf.
        '''
        self.x = int(self.xf)
        self.y = int(self.yf)
