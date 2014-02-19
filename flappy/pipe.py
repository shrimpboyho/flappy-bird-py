import pyglet
import window, random
from sprobj import SprObj

class Pipe(SprObj):

    def regenerate(self):
        self.x = window.bufferedWidth * 2
        self.y = random.randrange(-100, -10)