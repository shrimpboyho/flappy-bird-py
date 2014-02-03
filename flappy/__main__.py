import pyglet
from pyglet.window import key
from pyglet.gl import *
from pyglet.window import mouse

# Set up buffer variables
bufferedHeight = 256
bufferedWidth = 144

# Create the window
window = pyglet.window.Window(bufferedWidth, bufferedHeight, resizable=True)

# TODO: Get the resize event working
@window.event
def on_resize(width, height):
    global bufferedHeight, bufferedWidth
    print 'The window was resized to %dx%d' % (width, height)
    glScalef(width / bufferedWidth, height / bufferedHeight, 2.0 ) 
    bufferedHeight = height
    bufferedWidth = width

# Get the sprites set up
bird_image = pyglet.resource.image('assets/sprites/sheet.png')
title_image = pyglet.resource.image('assets/sprites/title.png')
title_sprite = pyglet.sprite.Sprite(title_image)
title_sprite.set_position(0, 0)
bird_sprite = pyglet.sprite.Sprite(bird_image)
bird_sprite.x = 10

# Get game status booleans set up
titleScreenMode = True

# Handle the keypress
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.SPACE:
        print 'The SPACE key was pressed.'

# Handle mouse presses
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print 'The left mouse button was pressed at %d, %d' % (x, y)
	# TODO: Add logic for switching game states

@window.event
def on_draw():
    # Clear the window
    window.clear()
    
    # The following two lines will change how textures are scaled.
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST) 
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    
    # Draw the title screen if nessecary
    if(titleScreenMode):
    	title_sprite.draw()

pyglet.app.run()
