from factories import LineFactory

class Shot1:
    def __init__(self, sprite):
        self.sprite = sprite

        self.spawn_rate = 10
        self.age_factor = 32

        self.factories = [
            LineFactory(
                15,
                self.sprite,
                self.spawn_rate,
                self.age_factor
            ),
            LineFactory(
                0,
                self.sprite,
                self.spawn_rate,
                self.age_factor
            ),
            LineFactory(
                -15,
                self.sprite,
                self.spawn_rate,
                self.age_factor
            )
        ]


    def spawn_bullet(self, dt):
        for factory in self.factories:
            factory.spawn_bullet(1.0/self.spawn_rate)

    def update(self, dt):
        for factory in self.factories:
            factory.update(1.0/self.spawn_rate)

    def pause(self):
        for factory in self.factories:
            factory.pause()

    def play(self):
        for factory in self.factories:
            factory.play()

    def toggle(self):
        for factory in self.factories:
            factory.toggle()
