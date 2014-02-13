import pyglet
from copy import *

# Get the sprites set up

title_image = pyglet.resource.image('assets/sprites/title.png')
title_sprite = pyglet.sprite.Sprite(title_image, 0, 0)

flappybird_image = pyglet.resource.image('assets/sprites/flappybird.png')
flappybird_sprite = pyglet.sprite.Sprite(flappybird_image, 10, 162)

background_image1 = pyglet.resource.image('assets/sprites/background.png')
background_sprite1 = pyglet.sprite.Sprite(background_image1, 0, 0)

background_image2 = pyglet.resource.image('assets/sprites/background.png')
background_sprite2 = pyglet.sprite.Sprite(background_image2, 144, 0)

background_image3 = pyglet.resource.image('assets/sprites/background.png')
background_sprite3 = pyglet.sprite.Sprite(background_image3, 288, 0)

instructions_image = pyglet.resource.image('assets/sprites/instructions.png')
instructions_sprite = pyglet.sprite.Sprite(instructions_image, 0, 0)

downflap_image = pyglet.resource.image('assets/sprites/downflap.png')
upflap_image = pyglet.resource.image('assets/sprites/upflap.png')
middleflap_image = pyglet.resource.image('assets/sprites/middleflap.png')

pipe_top_image = pyglet.resource.image('assets/sprites/sheet.png').get_region(300,120, 30, 200)
pipe_top_sprite = pyglet.sprite.Sprite(pipe_top_image, 110, 120)

pipe_bottom_image = pyglet.resource.image('assets/sprites/sheet.png').get_region(330, 120, 28, 136)
pipe_bottom_sprite = pyglet.sprite.Sprite(pipe_bottom_image, 112, -60)


bird_images = [
    downflap_image,
    middleflap_image,
    upflap_image
]

bird_animation = pyglet.image.Animation.from_image_sequence(bird_images, .05, loop=True)
bird_sprite = pyglet.sprite.Sprite(bird_animation, 115, 171)
bird_sprite2 = pyglet.sprite.Sprite(bird_animation, 41, 120)

class Rect(object):
    left = right = top = bottom = 0
    def __init__(self, sprite):
        self.left = sprite.x;
        self.right = sprite.x + sprite.width;
        self.bottom = sprite.y + 8; #related to sprite img crop
        self.top = sprite.y + sprite.height;

def collide(sprites_list, crasher_obj):
    crasher_obj = Rect(crasher_obj)
    for sprite in sprites_list:
        sprite = Rect(sprite)
        if (crasher_obj.bottom <= sprite.top and
                crasher_obj.top >= sprite.bottom and
                crasher_obj.right >= sprite.left and
                crasher_obj.left <= sprite.right):
            return True

bouncebool = 'up'
bouncebool2 = 'up'
bouncebool3 = 'up'

def bounce1(dt):
    global bouncebool
    if bouncebool == 'up' and bird_sprite.y <= 175:
	   bird_sprite.y += 1

    if bird_sprite.y == 175:
        bouncebool = 'down'

    if bird_sprite.y == 170:
        bouncebool = 'up'

    if bouncebool == 'down' and bird_sprite.y >= 170:
	   bird_sprite.y -= 1

    global bouncebool3
    if bouncebool3 == 'up' and flappybird_sprite.y <= 167:
        flappybird_sprite.y += 1

    if flappybird_sprite.y == 167:
        bouncebool3 = 'down'

    if flappybird_sprite.y == 162:
        bouncebool3 = 'up'

    if bouncebool3 == 'down' and flappybird_sprite.y >= 162:
        flappybird_sprite.y -= 1

pyglet.clock.schedule_interval(bounce1, .05) # update at 60Hz
