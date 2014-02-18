import pyglet
import threading
import window
from sprites import *

class SprObj(pyglet.sprite.Sprite):

    # Constructor
    def __init__(self, img, x=0, y=0, blend_src=770, blend_dest=771, batch=None, group=None, usage='dynamic'):
        pyglet.sprite.Sprite.__init__(self, img, x, y, blend_src, blend_dest, batch, group, usage)
        
    # Move function
    def move(self, x, y):
        self.set_position(self.x + x, self.y + y)

    # Set the sprite angle
    def set_angle(self, angle):
        self.rotation = angle

    # Jump
    def jump(self, increase, angle=None):
        if angle:
            self.set_angle(angle)
        self.move(0, increase)

    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + self.width
    
    @property
    def top(self):
        return self.y + self.height

    @property
    def bottom(self):
        return self.y