# import pyglet lib functions
import pyglet

from window import *

music = pyglet.resource.media('assets/audio/background.wav')
music.EOS_LOOP = 'loop'
music.play()

pyglet.app.run()
