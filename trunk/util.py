class Point(object):
    '''Turns an (x, y) tuple into an object with .x and .y'''
    def __init__(point):
        self.x, self.y = point

class RelPoint(object):
    '''RelPoint is a point relative to another point, offset by (h, k)'''
    def __init__(self, sprite, h, k):
        self.sprite = sprite
        self.h = h
        self.k = k

    @property
    def x(self):
        return self.sprite.x + self.h

    @property
    def y(self):
        return self.sprite.y + self.k
