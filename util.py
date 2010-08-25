class Point(object):
    def __init__(point):
        self.x, self.y = point

class RelPoint(object):
    def __init__(self, sprite, h, k):
        self.sprite = sprite
        self.h = h
        self.k = k
    @property # hax to hide function calls
    def x(self):
        return self.sprite.x + self.h
    @property # hax to hide function calls
    def y(self):
        return self.sprite.y + self.k
