import pyglet
import window
from sprobj import SprObj

class Bird(SprObj):

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

    # Enable effect of gravity
    def gravity(self, dt):
        self.move(0, -1)
        #Check if this rotation affect directly the collision detector (visual impact bug)
        if self.rotation < 90 or self.rotation < 445:
            self.set_angle(self.rotation + (self.angacc * dt))
            self.update_edges()
    # Jump
    def jump(self):
        #Implement jumping effect to prevent move directly the position of the sprite
        pyglet.resource.media('assets/audio/flap.wav').play()
        if self.y > window.bufferedHeight + 10:
            return #Security fix to prevent ignore pipes in the sky :)
        return SprObj.jump(self, 20, 330)

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