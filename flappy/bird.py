import pyglet
from sprites import *

class Bird(pyglet.sprite.Sprite):
    TLX = 0
    TLY = 0
    TRX = 0
    TRY = 0
    BLX = 0
    BLY = 0
    BRX = 0
    BRY = 0
    def move(this, x, y):
        self.set_position(self.x + x, self.y + y)
    def set_angle(this, angle):
        self.rotation = angle
