# import pyglet lib functions
import pyglet

from window import *

music = pyglet.resource.media('assets/audio/background.WAV')
music.play()

pyglet.app.run()
