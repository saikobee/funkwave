import rabbyt
from intsprite import IntSprite

class PlayerSprite(IntSprite):
    vx = rabbyt.anim_slot()
    vy = rabbyt.anim_slot()
    vxy = rabbyt.swizzle("vx", "vy")
