from factories import LineFactory
from util      import RelPoint

class Shot1:
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


    def spawn_bullet(self, dt):
        for factory in self.factories:
            factory.spawn_bullet(dt)

    def update(self, dt):
        for factory in self.factories:
            factory.update(dt)

    def pause(self):
        for factory in self.factories:
            factory.pause()

    def play(self):
        for factory in self.factories:
            factory.play()

    def toggle(self):
        for factory in self.factories:
            factory.toggle()


class Shot2:
    def __init__(self, sprite):
        self.sprite = sprite

        self.spawn_rate =  15
        self.age_factor = 512 + 128
        
        self.offsets = [10, -10]

        self.factories = [LineFactory(
                0,
                RelPoint(self.sprite, 0, offset),
                self.spawn_rate,
                self.age_factor
        ) for offset in self.offsets]

    def spawn_bullet(self, dt):
        for factory in self.factories:
            factory.spawn_bullet(dt)

    def update(self, dt):
        for factory in self.factories:
            factory.update(dt)

    def pause(self):
        for factory in self.factories:
            factory.pause()

    def play(self):
        for factory in self.factories:
            factory.play()

    def toggle(self):
        for factory in self.factories:
            factory.toggle()

