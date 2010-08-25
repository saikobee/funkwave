from factories import LineFactory
from util      import RelPoint

class Shot(object):
    '''Controls a group of factories'''
    def spawn_bullet(self, dt):
        for factory in self.factories:
            factory.spawn_bullet(dt)

    def update(self, dt):
        for factory in self.factories:
            factory.update(dt)

    def paused(self):
        return all(map(lambda f: f.paused, self.factories))

    def pause(self):
        for factory in self.factories:
            factory.pause()

    def play(self):
        for factory in self.factories:
            factory.play()

    def toggle(self):
        for factory in self.factories:
            factory.toggle()


class Shot1(Shot):
    '''The player's shot: type 1'''
    def __init__(self, sprite):
        self.sprite = sprite

        self.spawn_rate =  15
        self.age_factor = 512 + 128
        self.angles     = (6, 3, 0, -3, -6)

        self.factories = [LineFactory(
            angle,
            self.sprite,
            self.spawn_rate,
            self.age_factor
        ) for angle in self.angles]

class Shot2(Shot):
    '''The player's shot: type 2'''
    def __init__(self, sprite):
        self.sprite = sprite

        self.spawn_rate =  30
        self.age_factor = 512 + 128
        
        self.offsets = (10, -10)

        self.factories = [LineFactory(
                0,
                RelPoint(self.sprite, 0, offset),
                self.spawn_rate,
                self.age_factor
        ) for offset in self.offsets]
