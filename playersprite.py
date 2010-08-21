import rabbyt
from intsprite import IntSprite

class PlayerSprite(IntSprite):
    v_max = 100

    x_keys = [0]
    y_keys = [0]

    def go_left(self):  self.x_keys.append(-1)
    def go_right(self): self.x_keys.append( 1)
    def go_up(self):    self.y_keys.append( 1)
    def go_down(self):  self.y_keys.append(-1)

    def vx(self): return self.x_keys[-1] * self.v_max
    def vy(self): return self.y_keys[-1] * self.v_max

    def pop_left(self):  self.x_keys.remove(-1)
    def pop_right(self): self.x_keys.remove( 1)
    def pop_up(self):    self.y_keys.remove( 1)
    def pop_down(self):  self.y_keys.remove(-1)

    def update(self, dt):
        self.xf += self.vx() * dt
        self.yf += self.vy() * dt
        self.truncate(self)
