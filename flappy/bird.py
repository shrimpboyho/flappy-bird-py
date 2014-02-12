import pyglet
import threading
from sprites import *

# BIRD BOUNCING GLOBAL VARIABLES
birdbouncecount = 0
birdbouncebool = 'up'

class Bird(pyglet.sprite.Sprite):
    
    # Coordinate data
    TLX = 0
    TLY = 0
    TRX = 0
    TRY = 0
    BLX = 0
    BLY = 0
    BRX = 0
    BRY = 0

    # Score data
    SCORE = 0

    # Clock
    CLOCK = pyglet.clock.Clock()

    # Constructor
    def __init__(self, img, x=0, y=0, blend_src=770, blend_dest=771, batch=None, group=None, usage='dynamic'):
        pyglet.sprite.Sprite.__init__(self, img, x, y, blend_src, blend_dest, batch, group, usage)
        self.update_edges()
        self.begin_bouncing()
    
    # Move function
    def move(self, x, y):
        self.set_position(self.x + x, self.y + y)
        self.update_edges()
    
    # Set the sprite angle
    def set_angle(self, angle):
        self.rotation = angle
    
    # Increment pipe score
    def plus_one(self):
        self.SCORE += 1;

    # Update the coordinate data everytime a move is made
    def update_edges(self):
        self.TLX = self.x
        self.TLY = self.y + self.image.get_max_height()
        self.TRX = self.x + self.image.get_max_width()
        self.TRY = self.y + self.image.get_max_height()
        self.BLX = self.x
        self.BLY = self.y
        self.BRX = self.x + self.image.get_max_width()
        self.BRY = self.y
    
    # Manipulate coordinate data to simulate bouncing
    def bounce_player(self, dt):
        global birdbouncebool, birdbouncecount

        if birdbouncebool == 'up' and birdbouncecount <= 5:
            self.move(0, 1)
            birdbouncecount += 1

        if birdbouncecount == 5:
            birdbouncebool = 'down'

        if birdbouncecount == 0:
            birdbouncebool = 'up'

        if birdbouncebool == 'down' and birdbouncecount >= 0:
            self.move(0, -1)
            birdbouncecount -= 1

    # Manipulate coordinate data to simulate bouncing
    def bounce_player_game(self, dt):
        self.move(0, 25)

    def unbounce_player_game(self, dt):
        self.move(0, -.9)

    # Begin the bouncing
    def begin_bouncing(self):
        self.CLOCK.schedule_interval(self.bounce_player, .05)

    # End the bouncing
    def end_bouncing(self):
        self.CLOCK.unschedule(self.bounce_player)

    # Enable drawing of score
    def draw_score(self):
	scores = str(self.SCORE)
	scoresl = scores.split()
	picdig = []
	for dig in scoresl:
	    img = pyglet.resource.image('assets/sprites/' + dig + '.png')
	    img.height = img.height * 2
	    img.width = img.width * 2
	    picdig.append(img)
	# TODO: Implement better drawing algo to handle drawing double digit scores
	for pic in picdig:
	    pic.blit(64,204)