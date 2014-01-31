import pyglet
import os
from pyglet.window import key
from pyglet.window import mouse
from pyglet import clock
from pyglet.gl import *

# Import the physics engine and other important tools
import physics
from position import *

# Import the player and entity classes
from player import *
from entity import *

# Create window
window = pyglet.window.Window()

# Fullscreen toggle variable
first_f1_hit = False

# Scale stuff
glScalef(1.0, 1.0, 1.0)

# Set up custom mouse cursor
mouse_image = pyglet.resource.image('assets/sprites/cursor.png')
cursor = pyglet.window.ImageMouseCursor(mouse_image, 20, 28)
window.set_mouse_cursor(cursor)

# Keyboard input buffer
keys_held = []

@window.event
def on_key_press(symbol, modifiers):
    global first_f1_hit
    keys_held.append(symbol)
    
    # Fullscreen toggle f1 key
    if symbol == key.F1:
        if first_f1_hit == False:
	    window.set_fullscreen(True)
	    center_sprite(player_sprite,window)
	    current_player.teleport(current_player.coordX,current_player.coordY,terrain_sprite,window)
	    first_f1_hit = True
	else:
	    window.set_fullscreen(False)
	    center_sprite(player_sprite,window)
	    current_player.teleport(current_player.coordX,current_player.coordY,terrain_sprite,window)
	    first_f1_hit = False
    
@window.event
def on_key_release(symbol, modifiers):
    keys_held.pop(keys_held.index(symbol))      

# Mouse input
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print 'The left mouse button was pressed at (' + str(x) + ','+ str(y) + ')'
	print("Player coordinates:" + str(current_player.coordX) + ',' + str(current_player.coordY))
        print("Map coordinates:" + str(terrain_sprite.x) + ',' + str(terrain_sprite.y))
    if button == mouse.RIGHT:
        print 'The right mouse button was pressed at (' + str(x) + ','+ str(y) + ')'

# Set up background map
terrain_image = pyglet.image.load("herblore/assets/sprites/map.png")
center_image(terrain_image)
terrain_sprite =  pyglet.sprite.Sprite(terrain_image)

# Create a player object
current_player = Player("jewishBoy", "Radiant", "Lina")

# Set up player sprites
player_image = pyglet.resource.image("assets/sprites/player.png")
center_image(player_image)
player_sprite = pyglet.sprite.Sprite(player_image)
player_sprite.scale = 0.2

monkey_image = pyglet.resource.image("assets/sprites/monkey.jpg")
center_image(monkey_image)
monkey_sprite = pyglet.sprite.Sprite(monkey_image)
monkey_sprite.scale = 0.2
monkey_player = Entity("monkey", "Dire", "Rex")

# Set up player in center of the screen
center_sprite(player_sprite,window)

# Add the player sprite to the player object
current_player.setSprite(player_sprite)
monkey_player.setSprite(monkey_sprite)

# Add the player to the entities
physics.entities.append(monkey_player)

# Create the custom player HUD stuff
player_name_label = pyglet.text.Label(current_player.username,
                          font_name='Garamond',
                          font_size=18,
                          x=3, y=20)
player_level_label = pyglet.text.Label("Level " + str(current_player.level),
                          font_name='Garamond',
                          font_size=15,
                          x=3, y=3)

# Draw the map
center_sprite(terrain_sprite,window)

# Spawn the player
current_player.respawn(terrain_sprite,window)
monkey_player.respawn(terrain_sprite,window)

# Update function called all the time to handle input
def update(interval):
    if key.W in keys_held and current_player.coordY < 182:
	current_player.coordY += 1
	terrain_sprite.y -= 3
	for thing in physics.entities:
	    thing.getSprite().y -= 3
    if key.S in keys_held and current_player.coordY > -175:
	current_player.coordY -= 1
	terrain_sprite.y += 3
	for thing in physics.entities:
	    thing.getSprite().y += 3
    if key.A in keys_held and current_player.coordX > -190:
	current_player.coordX -= 1    
	terrain_sprite.x += 3
	for thing in physics.entities:
	    thing.getSprite().x += 3
    if key.D in keys_held and current_player.coordX < 195:
	current_player.coordX += 1
	terrain_sprite.x -= 3
	for thing in physics.entities:
	    thing.getSprite().x -= 3

# Set up interval
clock.schedule_interval(update, .01)

# Draw
@window.event
def on_draw():
    # Clear the current stuff
    window.clear()

    # Draw the terrain
    terrain_sprite.draw()
    
    # Draw the player
    current_player.getSprite().draw()

    # Draw all the entities
    for thing in physics.entities:
	thing.getSprite().draw()
    
    # Draw the HUD
    player_name_label.draw()
    player_level_label.draw()

# Begin application
pyglet.app.run()

