import pyglet

# Get the sprites set up
bird_image = pyglet.resource.image('assets/sprites/sheet.png')
bird_sprite = pyglet.sprite.Sprite(bird_image)
bird_sprite.x = 10

title_image = pyglet.resource.image('assets/sprites/title.png')
title_sprite = pyglet.sprite.Sprite(title_image)
title_sprite.set_position(0, 0)

instructions_image = pyglet.resource.image('assets/sprites/instructions.png')
instructions_sprite = pyglet.sprite.Sprite(instructions_image)
instructions_sprite.set_position(0, 0)
