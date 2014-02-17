import pyglet
import threading
import window
from sprites import *

class Bird(pyglet.sprite.Sprite):
    left = right = top = bottom = 0

    # Coordinate data
    TLX = 0
    TLY = 0
    TRX = 0
    TRY = 0
    BLX = 0
    BLY = 0
    BRX = 0
    BRY = 0
    dy = 15
    angacc = 50

    # Constructor
    def __init__(self, img, x=0, y=0, blend_src=770, blend_dest=771, batch=None, group=None, usage='dynamic'):
        pyglet.sprite.Sprite.__init__(self, img, x, y, blend_src, blend_dest, batch, group, usage)
        self.update_edges()
    
    # Move function
    def move(self, x, y):
        self.set_position(self.x + x, self.y + y)
        #self.update_edges()
    
    # Set the sprite angle
    def set_angle(self, angle):
        self.rotation = angle

    # Update the coordinate data everytime a move is made
    def update_edges(self):
        self.TLX = self.x - self.image.get_max_width() / 2
        self.TLY = self.y + self.image.get_max_height() / 2
        self.TRX = self.x + self.image.get_max_width() / 2
        self.TRY = self.y + self.image.get_max_height() / 2
        self.BLX = self.x - self.image.get_max_width() / 2
        self.BLY = self.y - self.image.get_max_height() / 2
        self.BRX = self.x + self.image.get_max_width() / 2
        self.BRY = self.y - self.image.get_max_height() / 2

    # Enable effect of gravity
    def gravity(self, dt):
        self.move(0, -1)
        #Check if this rotation affect directly the collision detector (visual impact bug)
        if self.rotation < 90 or self.rotation < 445:
            self.set_angle(self.rotation + (self.angacc * dt))
    # Jump
    def jump(self):
        #Implement jumping effect to prevent move directly the position of the sprite
        self.set_angle(330)
        self.move(0, 30)
