import pyglet
from tools import *

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

pipes_batch = pyglet.graphics.Batch()
pipe_img1 = pyglet.resource.image('assets/sprites/pipe.png')
pipe_img2 = pyglet.resource.image('assets/sprites/pipe.png')
pipe_img3 = pyglet.resource.image('assets/sprites/pipe.png')

bird_images = [
    center_image_anchor(downflap_image),
    center_image_anchor(middleflap_image),
    center_image_anchor(upflap_image)
]

bird_animation = pyglet.image.Animation.from_image_sequence(bird_images, .05, loop=True)
bird_sprite = pyglet.sprite.Sprite(bird_animation, 119, 175)
bird_sprite2 = pyglet.sprite.Sprite(bird_animation, 50, 130)

game_over_sprite = pyglet.text.Label(
    "GameOver :(", font_name='Arial', font_size=17, anchor_x='center', anchor_y='center'
)