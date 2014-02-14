import pyglet
from copy import *

# Get the sprites set up

title_image = pyglet.resource.image('assets/sprites/title.png')
title_sprite = pyglet.sprite.Sprite(title_image, 0, 0)

flappybird_image = pyglet.resource.image('assets/sprites/flappybird.png')
flappybird_sprite = pyglet.sprite.Sprite(flappybird_image, 10, 162)

background_batch = pipes_batch = pyglet.graphics.Batch()
background_sprite1 = pyglet.sprite.Sprite(pyglet.resource.image('assets/sprites/background.png'), 
    0, 0, batch=background_batch
)
background_sprite2 = pyglet.sprite.Sprite(pyglet.resource.image('assets/sprites/background.png'), 
    144, 0, batch=background_batch
)
background_sprite3 = pyglet.sprite.Sprite(pyglet.resource.image('assets/sprites/background.png'), 
    288, 0, batch=background_batch
)

instructions_image = pyglet.resource.image('assets/sprites/instructions.png')
instructions_sprite = pyglet.sprite.Sprite(instructions_image, 0, 0)

downflap_image = pyglet.resource.image('assets/sprites/downflap.png')
upflap_image = pyglet.resource.image('assets/sprites/upflap.png')
middleflap_image = pyglet.resource.image('assets/sprites/middleflap.png')

PIPE_TOP_L = 300
PIPE_TOP_R = 120
PIPE_TOP_B = 30
PIPE_TOP_T = 200

PIPE_BTM_L = 330
PIPE_BTM_R = 120
PIPE_BTM_B = 30
PIPE_BTM_T = 136

pipes_batch = pyglet.graphics.Batch()
pipe_top_sprite1 = pyglet.sprite.Sprite(
    pyglet.resource.image('assets/sprites/sheet.png').
    get_region(PIPE_TOP_L, PIPE_TOP_R, PIPE_TOP_B, PIPE_TOP_T), 0, 120, batch=pipes_batch
)
pipe_bottom_sprite1 = pyglet.sprite.Sprite(
    pyglet.resource.image('assets/sprites/sheet.png').
    get_region(PIPE_BTM_L, PIPE_BTM_R, PIPE_BTM_B, PIPE_BTM_T), 0, -60, batch=pipes_batch
)
pipe_top_sprite2 = pyglet.sprite.Sprite(
    pyglet.resource.image('assets/sprites/sheet.png').
    get_region(PIPE_TOP_L, PIPE_TOP_R, PIPE_TOP_B, PIPE_TOP_T), 144, 130, batch=pipes_batch
)
pipe_bottom_sprite2 = pyglet.sprite.Sprite(
    pyglet.resource.image('assets/sprites/sheet.png').
    get_region(PIPE_BTM_L, PIPE_BTM_R, PIPE_BTM_B, PIPE_BTM_T), 144, -60, batch=pipes_batch
)
pipe_top_sprite3 = pyglet.sprite.Sprite(
    pyglet.resource.image('assets/sprites/sheet.png').
    get_region(PIPE_TOP_L, PIPE_TOP_R, PIPE_TOP_B, PIPE_TOP_T), 288, 110, batch=pipes_batch
)
pipe_bottom_sprite3 = pyglet.sprite.Sprite(
    pyglet.resource.image('assets/sprites/sheet.png').
    get_region(PIPE_BTM_L, PIPE_BTM_R, PIPE_BTM_B, PIPE_BTM_T), 288, -80, batch=pipes_batch
)

bird_images = [
    downflap_image,
    middleflap_image,
    upflap_image
]

bird_animation = pyglet.image.Animation.from_image_sequence(bird_images, .100, loop=True)
bird_sprite = pyglet.sprite.Sprite(bird_animation)
bird_sprite.set_position(115, 171)
bird_sprite2 = pyglet.sprite.Sprite(bird_animation)
bird_sprite2.set_position(41, 120)

bird_animation = pyglet.image.Animation.from_image_sequence(bird_images, .05, loop=True)
bird_sprite = pyglet.sprite.Sprite(bird_animation, 115, 171)
bird_sprite2 = pyglet.sprite.Sprite(bird_animation, 41, 120)