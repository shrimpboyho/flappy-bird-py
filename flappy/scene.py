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
            if (crasher_obj.bottom <= sprite.top and
                    crasher_obj.top >= sprite.bottom and
                    crasher_obj.right >= sprite.left and
                    crasher_obj.left <= sprite.right):
                return True

    # Enable drawing of score
    def draw_score(self, score_number):
        for number in range(0, score_number):
            if number < 10:
                img = pyglet.resource.image('assets/sprites/' + str(number) + '.png')
                img.blit(64, 204)
            else:
                # TODO: Implement better drawing algo to handle drawing double digit scores
                for number in list(str(number)):
                    pass
                    #img = pyglet.resource.image('assets/sprites/' + str(number) + '.png')
                    #img.blit(64, 214)

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
    left = right = top = bottom = 0
    def __init__(self, sprite):
        self.left = sprite.x;
        self.right = sprite.x + sprite.width;
        self.bottom = sprite.y + 8; #related to sprite img crop
        self.top = sprite.y + sprite.height;