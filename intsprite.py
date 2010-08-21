import rabbyt

class IntSprite(rabbyt.Sprite):
    xf  = rabbyt.anim_slot()
    yf  = rabbyt.anim_slot()
    xyf = rabbyt.swizzle("xf", "yf")
    
    @staticmethod
    def truncate(*sprites):
        for sprite in sprites:
            sprite.x = int(sprite.xf)
            sprite.y = int(sprite.yf)

    @staticmethod
    def truncate_list(sprites):
        self.truncate(*sprites)
