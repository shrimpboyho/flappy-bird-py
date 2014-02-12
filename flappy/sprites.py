import pyglet
from copy import *

# Get the sprites set up

title_image = pyglet.resource.image('assets/sprites/title.png')
title_sprite = pyglet.sprite.Sprite(title_image)
title_sprite.set_position(0, 0)

flappybird_image = pyglet.resource.image('assets/sprites/flappybird.png')
flappybird_sprite = pyglet.sprite.Sprite(flappybird_image)
flappybird_sprite.set_position(10, 162)

background_image = pyglet.resource.image('assets/sprites/background.png')
background_sprite = pyglet.sprite.Sprite(background_image)
background_sprite.set_position(0, 0)

instructions_image = pyglet.resource.image('assets/sprites/instructions.png')
instructions_sprite = pyglet.sprite.Sprite(instructions_image)
instructions_sprite.set_position(0, 0)

downflap_image = pyglet.resource.image('assets/sprites/downflap.png')
upflap_image = pyglet.resource.image('assets/sprites/upflap.png')
middleflap_image = pyglet.resource.image('assets/sprites/middleflap.png')

bird_images = [
    downflap_image,
    middleflap_image,
    upflap_image
]

bird_animation = pyglet.image.Animation.from_image_sequence(bird_images, .05, loop=True)
bird_sprite = pyglet.sprite.Sprite(bird_animation)
bird_sprite.set_position(115, 171)
bird_sprite2 = pyglet.sprite.Sprite(bird_animation)
bird_sprite2.set_position(41, 120)
bouncebool = 'up'
bouncebool2 = 'up'
bouncebool3 = 'up'

def bounce2(dt):
    global bouncebool2
    if(bouncebool2 == 'up' and bird_sprite2.y <= 125):
	bird_sprite2.y += 1
    if(bird_sprite2.y == 125):
        bouncebool2 = 'down'
    if(bird_sprite2.y == 120):
        bouncebool2 = 'up'
    if(bouncebool2 == 'down' and bird_sprite2.y >= 120):
	bird_sprite2.y -= 1
pyglet.clock.schedule_interval(bounce2, .05) # update at 60Hz

def bounce1(dt):
    global bouncebool
    if(bouncebool == 'up' and bird_sprite.y <= 175):
	bird_sprite.y += 1
    if(bird_sprite.y == 175):
        bouncebool = 'down'
    if(bird_sprite.y == 170):
        bouncebool = 'up'
    if(bouncebool == 'down' and bird_sprite.y >= 170):
	bird_sprite.y -= 1

    global bouncebool3
    if(bouncebool3 == 'up' and flappybird_sprite.y <= 167):
        flappybird_sprite.y += 1
    if(flappybird_sprite.y == 167):
        bouncebool3 = 'down'
    if(flappybird_sprite.y == 162):
        bouncebool3 = 'up'
    if(bouncebool3 == 'down' and flappybird_sprite.y >= 162):
	flappybird_sprite.y -= 1
pyglet.clock.schedule_interval(bounce1, .05) # update at 60Hz
