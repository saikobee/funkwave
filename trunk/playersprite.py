import rabbyt
from intsprite import IntSprite

class PlayerSprite(IntSprite):
    #vx = rabbyt.anim_slot()
    #vy = rabbyt.anim_slot()
    #vxy = rabbyt.swizzle("vx", "vy")

    vx_max = 1
    vy_max = 1

    x_keys = [0]
    y_keys = [0]

    def go_left(self):
        self.x_keys.append(-1)

    def go_right(self):
        self.x_keys.append(1)

    def go_up(self):
        self.y_keys.append(1)

    def go_down(self):
        self.y_keys.append(-1)

    def vx(self):
        return self.x_keys[-1] * self.vx_max

    def vy(self):
        return self.y_keys[-1] * self.vy_max

    def pop_x(self):
        self.x_keys.pop()

    def pop_y(self):
        self.y_keys.pop()

    def update(self):
        self.xf += self.vx()
        self.yf += self.vy()
        self.truncate(self)
