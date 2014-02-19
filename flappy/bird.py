import pyglet
import window
from sprobj import SprObj
from tools import play_audio

class Bird(SprObj):

    #JUMP EFFECT
    JUMPING_STEPS = 0
    JUMP_INCREASE_LEVEL = 3
    JUMP_MAX_STEPS = 10
    JUMP_CHANGE_ANGLE = 330

    JUMP_STEPS = 35

    # Coordinate data
    TLX = 0
    TLY = 0
    TRX = 0
    TRY = 0
    BLX = 0
    BLY = 0
    BRX = 0
    BRY = 0
    ANGACC = 50

    def gravitate(self, dt):
        self.move(0, -1.5)
        #Check if this rotation affect directly the collision detector (visual impact bug)
        if self.ROTATION < 90 or self.ROTATION < 445:
            self.set_angle(self.ROTATION + (self.ANGACC * dt))
            self.update_edges()

    def jump_effect(self, dt):
        #TODO: Try to use this, but we need more reaction (this method should be called by clock in self.jump())
        self.JUMPING_STEPS += 1
        window.set_gravity(False)
        if self.y > window.bufferedHeight + 10:
            pyglet.clock.unschedule(self.jump_effect)
            window.set_gravity(True)
            return #Security fix to prevent ignore pipes in the sky :)

        if self.JUMPING_STEPS < self.JUMP_MAX_STEPS: #can jump
            SprObj.jump(self, self.JUMP_INCREASE_LEVEL, self.JUMP_CHANGE_ANGLE)
        else:
            pyglet.clock.unschedule(self.jump_effect)
            window.set_gravity(True)
            self.JUMPING_STEPS = 0

    def jump(self):
        play_audio('assets/audio/flap.wav')
        window.set_gravity(False)
        SprObj.jump(self, self.JUMP_STEPS, self.JUMP_CHANGE_ANGLE)
        window.set_gravity(True)

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

    def crash_floor(self):
        return self.y < 0