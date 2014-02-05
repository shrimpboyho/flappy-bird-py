import pyglet
from sprites import *

class Bird:
    TLX = 0
    TLY = 0
    TRX = 0
    TRY = 0
    BLX = 0
    BLY = 0
    BRX = 0
    BRY = 0
    player_sprite = pyglet.sprite.Sprite(bird_animation)

    def move(this, x, y):
        pass
