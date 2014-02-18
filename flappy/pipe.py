import pyglet
import window, random
from sprobj import SprObj

class Pipe(SprObj):

    def regenerate(self):
        self.x = window.bufferedWidth
        self.y = random.randrange(-120, 0)