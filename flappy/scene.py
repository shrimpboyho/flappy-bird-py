import pyglet
import window
from sprites import *

class Scene(object):

    PIPES_PASSED = 0
    LOGO_POS_BIRD = 'up'
    LOGO_POS_LETTERS = 'up'

    PIPES_VELOCITY = 1.5
    BACKGROUND_VELOCITY = .5

    def move_background(self, dt):
        background_sprite1.x -= self.BACKGROUND_VELOCITY
        background_sprite2.x -= self.BACKGROUND_VELOCITY
        background_sprite3.x -= self.BACKGROUND_VELOCITY

        if background_sprite1.x <= -window.bufferedWidth:
            background_sprite1.x = window.bufferedWidth
        if background_sprite2.x <= -window.bufferedWidth:
            background_sprite2.x = window.bufferedWidth
        if background_sprite2.x <= -window.bufferedWidth:
            background_sprite2.x = window.bufferedWidth

    def move_pipes(self, dt):
        window.pipe1.move(-self.PIPES_VELOCITY, 0)
        window.pipe2.move(-self.PIPES_VELOCITY, 0)
        window.pipe3.move(-self.PIPES_VELOCITY, 0)

        #Implement stable solution to increment the separation between pipes
        if window.pipe1.x <= window.bufferedWidth / -2:
            window.pipe1.regenerate()
            self.PIPES_PASSED += 1
        if window.pipe2.x <= window.bufferedWidth / -2:
            window.pipe2.regenerate()
            self.PIPES_PASSED += 1
        if window.pipe3.x <= window.bufferedWidth / -2:
            window.pipe3.regenerate()
            self.PIPES_PASSED += 1

    def check_collision(self, crasher_obj, sprobj_list):
        for sprite in sprobj_list:
            if (crasher_obj.bottom <= sprite.top and
                    crasher_obj.top >= sprite.bottom and
                    crasher_obj.right >= sprite.left and
                    crasher_obj.left <= sprite.right):
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