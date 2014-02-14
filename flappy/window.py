# import lib stuff
import pyglet
from pyglet.window import key
from pyglet.gl import *
from pyglet.window import mouse

# import other stuff
from bird import *
from sprites import *
from scene import *
from state import *

# Set up buffer variables
bufferedHeight = 256    
bufferedWidth = 144

# Set up the screen resolution variables
smallScreen = True
bigScreen = False

# Scale resolution
glScalef(1.0, 1.0, 1.0)

# Create the window
window = pyglet.window.Window(bufferedWidth, bufferedHeight, resizable=True)
#window.set_location(50,750)

player = Bird(bird_animation, 41, 120)
scene = Scene()
state = State()

# Set up the current state as the title screen
state.change('title')

# Handle the keypress
@window.event
def on_key_release(symbol, modifiers):
    global player

    global bigScreen
    global smallScreen

    if symbol == key.SPACE:
        player.jump()

    if symbol == key.PAGEUP:
        if smallScreen == True:
                glScalef(2.0, 2.0, 2.0)
                window.set_size(window.width * 2, window.height * 2)
                smallScreen = False
                bigScreen = True
    if symbol == key.PAGEDOWN:
            if bigScreen:
                glScalef(0.5, 0.5, 0.5)
                window.set_size(window.width / 2 , window.height /2)
                smallScreen = True
                bigScreen = False

# Handle mouse presses
@window.event
def on_mouse_release(x, y, button, modifiers):
    if button == mouse.LEFT:
        print 'The left mouse button was released at %d, %d' % (x, y)

    """ Add logic for switching game states """
    if state.INSTRUCTIONS:
        state.change('gameplay')
        
    if state.TITLE_SCREEN:
        if smallScreen:
            # Play button logic
            if x > 21 and x < 60 and y > 63 and y < 75:
                state.change('instructions')
            # Score button logic
            if x > 80 and x < 119 and y > 63 and y < 75:
                state.change('highscores')

        if bigScreen:
            # Play button logic
            if x > 43 and x < 121 and y > 125 and y < 148:
                state.change('instructions')
            # Score button logic
            if x > 160 and x < 240 and y > 125 and y < 148:
                state.change('highscores')
    if state.GAME_PLAY_STARTED:
        player.jump()
    if state.GAME_OVER:
        pass
    if state.HIGH_SCORES_SCREEN:
        pass

def crash_pipe():
    return scene.check_collide(player, [
        pipe_top_sprite1, pipe_bottom_sprite1,
        pipe_top_sprite2, pipe_bottom_sprite2,
        pipe_top_sprite3, pipe_bottom_sprite3,
    ])

def crash_floor():
    global bufferedHeight
    return player.y > bufferedHeight or player.y < 0

# Grab fps count
fps_display = pyglet.clock.ClockDisplay()

pyglet.clock.schedule_interval(scene.logo_animation, .05) # update at 60Hz

def schedule_events_to_play():
    if state.GAME_PLAY and not state.GAME_PLAY_STARTED:
        state.GAME_PLAY_STARTED = True
        pyglet.clock.schedule_interval(scene.move_background, .005) # update at 60Hz
        pyglet.clock.schedule_interval(scene.move_pipes, .005) # update at 60Hz
        pyglet.clock.schedule_interval(player.gravity, .01)

# Handle the drawing
@window.event
def on_draw():

    # Clear the window
    window.clear()
    
    # The following two lines will change how textures are scaled.
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST) 
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    # Draw the title screen if nessecary
    if state.TITLE_SCREEN:
        title_sprite.draw()
        flappybird_sprite.draw()
        bird_sprite.draw()

    # Draw the gameplay screen if nessecary
    if state.GAME_PLAY:
        if crash_floor() or crash_pipe():
            state.GAME_PLAY = False
            state.GAME_OVER = True
        schedule_events_to_play()
        background_batch.draw()
        player.draw()
        pipes_batch.draw()
        scene.draw_score(scene.PIPES_PASSED)

    # Draw the highscore screen if nessecary
    if state.HIGH_SCORES_SCREEN:
        pass

    # Draw the gameover screen if nessecary
    if state.GAME_OVER:
        pass
    
    # Draw the instructions screen if nessecary
    if state.INSTRUCTIONS:
        instructions_sprite.draw()
        bird_sprite2.draw()

    fps_display.draw()
