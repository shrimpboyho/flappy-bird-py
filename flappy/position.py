def center_image(image): 
    """Sets an image's anchor point to its center""" 
    image.anchor_x = image.width/2 
    image.anchor_y = image.height/2

def center_sprite(sprite,window): 
    """Sets an sprite to the center of the window""" 
    sprite.x = window.width/2 
    sprite.y = window.height/2
