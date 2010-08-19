#!/usr/bin/python
import rabbyt
import pyglet
import random

random.seed(0)

#num_sprites = 1000
num_sprites =  500
#num_sprites =  250
#num_sprites = 100
#num_sprites = 10
#num_sprites = 2
#num_sprites = 1
#num_sprites = 0
#num_sprites = 200

pyglet.clock.schedule(rabbyt.add_time)

fps_display = pyglet.clock.ClockDisplay()

pyglet.resource.path = [".", "alpha", "art"]
pyglet.resource.reindex()

#DAT_IMG = pyglet.resource.image("player.png")
DAT_IMG = pyglet.resource.image("star.png")
#DAT_IMG = pyglet.resource.image("bullet.gif")

def g():
    for i in xrange(num_sprites):
        x = random.randrange(0, 1024)
        y = random.randrange(0,  576)
        #sprite = rabbyt.Sprite("player.png")
        #sprite = rabbyt.Sprite("player.png")
        sprite = rabbyt.Sprite(DAT_IMG)
        sprite.xy = (x, y)
        sprite.x = rabbyt.lerp(x-100, x+100, dt=2, extend="reverse")
        sprite.y = rabbyt.lerp(y-100, y+100, dt=2, extend="reverse")
        sprite.rot = rabbyt.lerp(0,360, dt=10, extend="extrapolate")
        sprite.rgb = rabbyt.lerp((1,0.5,0.5), (0.5,1,0.5), dt=2, extend="reverse")
        ##sprite.alpha = rabbyt.lerp(0, 1, dt=0.25, extend="reverse")
        sprite.alpha = rabbyt.lerp(0.25, 1, dt=1, extend="reverse")
        yield sprite

sprites = list(g())

# TODO: WINDOWS KNOW THEIR OWN SIZE
w, h = size = 1024, 576

class MainWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

    def update(self, dt):
        pass

    def on_draw(self):
        rabbyt.clear()
        rabbyt.render_unsorted(sprites)
        fps_display.draw()

def other_main():
    #window = MainWindow(*size, vsync=False)
    window = MainWindow(width=size[0], height=size[1], vsync=False)
    window.set_caption(
        "%i sprites :: Super Ultimate Sprite Machine Factory Window" % num_sprites
    )
    rabbyt.set_default_attribs()
    #window.push_handlers(pyglet.window.event.WindowEventLogger())
    pyglet.clock.schedule_interval(window.update, 1.0/70.0)
    #pyglet.clock.schedule_interval(window.update, 1.0/120)
    pyglet.app.run()

#main_loop()
other_main()
