# import pyglet lib functions
import pyglet

from window import *
from tools import play_audio

play_audio('assets/audio/background.wav', True)

pyglet.app.run()