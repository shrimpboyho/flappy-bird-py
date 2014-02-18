import pyglet
import window
from sprobj import SprObj
from tools import play_audio

class Bird(SprObj):

    JUMPING_STEPS = 0
    JUMP_INCREASE_LEVEL = 2
    JUMP_MAX_STEPS = 15
    JUMP_CHANGE_ANGLE = 330
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

    def gravity(self, dt):
        self.move(0, -1.5)
        #Check if this rotation affect directly the collision detector (visual impact bug)
        if self.rotation < 90 or self.rotation < 445:
            self.set_angle(self.rotation + (self.angacc * dt))
            self.update_edges()    

    def jump_effect(self, dt):
        #TODO: Improve this, we need more reaction
        self.JUMPING_STEPS += 1
        pyglet.clock.unschedule(self.gravity)
        if self.y > window.bufferedHeight + 10:
            pyglet.clock.unschedule(self.jump_effect)
            pyglet.clock.schedule_interval(self.gravity, .00000001)
            return #Security fix to prevent ignore pipes in the sky :)
        if self.JUMPING_STEPS < self.JUMP_MAX_STEPS:
            return SprObj.jump(self, self.JUMP_INCREASE_LEVEL, self.JUMP_CHANGE_ANGLE)
        pyglet.clock.unschedule(self.jump_effect)
        pyglet.clock.schedule_interval(self.gravity, .00000001)
        self.JUMPING_STEPS = 0

    def jump(self):
        play_audio('assets/audio/flap.wav')
        pyglet.clock.unschedule(self.jump_effect)
        pyglet.clock.schedule_interval(self.jump_effect, .00000001)

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