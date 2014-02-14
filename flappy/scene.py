import pyglet
import window
from sprites import *

class Scene(object):

    PIPES_PASSED = 0
    LOGO_POS_BIRD = 'up'
    LOGO_POS_LETTERS = 'up'

    def move_background(self, dt):
        background_sprite1.x = background_sprite1.x - 1
        background_sprite2.x = background_sprite2.x - 1
        background_sprite3.x = background_sprite3.x - 1

    def move_pipes(self, dt):
        pipe_top_sprite1.x = pipe_top_sprite1.x - 2
        pipe_bottom_sprite1.x = pipe_bottom_sprite1.x - 2

        pipe_top_sprite2.x = pipe_top_sprite2.x - 2
        pipe_bottom_sprite2.x = pipe_bottom_sprite2.x - 2

        pipe_top_sprite3.x = pipe_top_sprite3.x - 2
        pipe_bottom_sprite3.x = pipe_bottom_sprite3.x - 2

        if background_sprite1.x <= -window.bufferedWidth:
            background_sprite1.x = window.bufferedWidth
        if background_sprite2.x <= -window.bufferedWidth:
            background_sprite2.x = window.bufferedWidth
        if background_sprite2.x <= -window.bufferedWidth:
            background_sprite2.x = window.bufferedWidth

        if pipe_top_sprite1.x <= -window.bufferedWidth / 2:
            pipe_top_sprite1.x = window.bufferedWidth
        if pipe_bottom_sprite1.x <= -window.bufferedWidth / 2:
            pipe_bottom_sprite1.x = window.bufferedWidth
            self.PIPES_PASSED = self.PIPES_PASSED +1

        if pipe_top_sprite2.x <= -window.bufferedWidth / 2:
            pipe_top_sprite2.x = window.bufferedWidth
        if pipe_bottom_sprite2.x <= -window.bufferedWidth / 2:
            pipe_bottom_sprite2.x = window.bufferedWidth
            self.PIPES_PASSED = self.PIPES_PASSED +1

        if pipe_top_sprite3.x <= -window.bufferedWidth / 2:
            pipe_top_sprite3.x = window.bufferedWidth
        if pipe_bottom_sprite3.x <= -window.bufferedWidth / 2:
            pipe_bottom_sprite3.x = window.bufferedWidth
            self.PIPES_PASSED = self.PIPES_PASSED +1

    def check_collide(self, crasher_obj, sprites_list):
        crasher_obj = Rect(crasher_obj)
        for sprite in sprites_list:
            sprite = Rect(sprite)
            if (crasher_obj.BOTTOM <= sprite.TOP and
                    crasher_obj.TOP >= sprite.BOTTOM and
                    crasher_obj.RIGHT >= sprite.LEFT and
                    crasher_obj.LEFT <= sprite.RIGHT):
                return True

    # Enable drawing of score
    def draw_score(self, score_number):
	print "Drawing score: %d" % (score_number)
	if score_number < 10:
            img = pyglet.resource.image('assets/sprites/' + str(score_number) + '.png')
            img.height = img.height * 2
            img.width = img.width * 2
	    img.blit(64, 204)
        else:
            # TODO: Implement better drawing algo to handle drawing double digit scores
            pass

    def logo_animation(self, dt):
        if self.LOGO_POS_BIRD == 'up' and bird_sprite.y <= 175:
           bird_sprite.y += 1

        if bird_sprite.y == 175:
            self.LOGO_POS_BIRD = 'down'

        if bird_sprite.y == 170:
            self.LOGO_POS_BIRD = 'up'

        if self.LOGO_POS_BIRD == 'down' and bird_sprite.y >= 170:
           bird_sprite.y -= 1

        if self.LOGO_POS_LETTERS == 'up' and flappybird_sprite.y <= 167:
            flappybird_sprite.y += 1

        if flappybird_sprite.y == 167:
            self.LOGO_POS_LETTERS = 'down'

        if flappybird_sprite.y == 162:
            self.LOGO_POS_LETTERS = 'up'

        if self.LOGO_POS_LETTERS == 'down' and flappybird_sprite.y >= 162:
            flappybird_sprite.y -= 1

class Rect(object):

    LEFT = RIGHT = TOP = BOTTOM = 0

    def __init__(self, sprite):
        self.LEFT = sprite.x;
        self.RIGHT = sprite.x + sprite.width;
        self.TOP = sprite.y + sprite.height;
        self.BOTTOM = sprite.y + 8; #related to sprite img crop
