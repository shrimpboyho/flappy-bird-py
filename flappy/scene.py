import pyglet
import window
from sprites import *

class Scene(object):

    PIPES_PASSED = 0
    LOGO_POS_BIRD = 'up'
    LOGO_POS_LETTERS = 'up'

    PIPES_VELOCITY = 2
    BACKGROUND_VELOCITY = 1

    def move_background(self, dt):
        background_sprite1.x -= self.BACKGROUND_VELOCITY
        background_sprite2.x -= self.BACKGROUND_VELOCITY
        background_sprite3.x = self.BACKGROUND_VELOCITY

        if background_sprite1.x <= -window.bufferedWidth:
            background_sprite1.x = window.bufferedWidth
        if background_sprite2.x <= -window.bufferedWidth:
            background_sprite2.x = window.bufferedWidth
        if background_sprite2.x <= -window.bufferedWidth:
            background_sprite2.x = window.bufferedWidth

    def move_pipes(self, dt):
        pipe_top_sprite1.x -= self.PIPES_VELOCITY
        pipe_bottom_sprite1.x -= self.PIPES_VELOCITY

        pipe_top_sprite2.x -= self.PIPES_VELOCITY
        pipe_bottom_sprite2.x -= self.PIPES_VELOCITY

        pipe_top_sprite3.x -= self.PIPES_VELOCITY
        pipe_bottom_sprite3.x -= self.PIPES_VELOCITY

        #Implement random regeneration algo to prevent all same pipes
        #Implement stable solution to increment the separation between pipes
        if pipe_top_sprite1.x <= -window.bufferedWidth / 2:
            pipe_top_sprite1.x = window.bufferedWidth
        if pipe_bottom_sprite1.x <= -window.bufferedWidth / 2:
            pipe_bottom_sprite1.x = window.bufferedWidth
            self.PIPES_PASSED += 1

        if pipe_top_sprite2.x <= -window.bufferedWidth / 2:
            pipe_top_sprite2.x = window.bufferedWidth
        if pipe_bottom_sprite2.x <= -window.bufferedWidth / 2:
            pipe_bottom_sprite2.x = window.bufferedWidth
            self.PIPES_PASSED += 1

        if pipe_top_sprite3.x <= -window.bufferedWidth / 2:
            pipe_top_sprite3.x = window.bufferedWidth
        if pipe_bottom_sprite3.x <= -window.bufferedWidth / 2:
            pipe_bottom_sprite3.x = window.bufferedWidth
            self.PIPES_PASSED += 1

    def check_collide(self, crasher_obj, sprites_list):
        #TODO: append each sprite object with rect property to prevent the object creation there (performance)
        crasher_obj = Rect(crasher_obj)
        for sprite in sprites_list:
            sprite = Rect(sprite)
            if (crasher_obj.BOTTOM <= sprite.TOP and
                    crasher_obj.TOP >= sprite.BOTTOM and
                    crasher_obj.RIGHT >= sprite.LEFT and
                    crasher_obj.LEFT <= sprite.RIGHT):
                print "Collision detected between: [crasherObj: %s] [crasherSpr: %s]" % (crasher_obj, sprite)
                return True

    # Enable drawing of score
    def draw_score(self, score_number):
        if score_number < 10:
            img = pyglet.resource.image('assets/sprites/' + str(score_number) + '.png')
            img.height *= 2
            img.width *= 2
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
        self.BOTTOM = sprite.y;
