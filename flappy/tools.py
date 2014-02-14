import pyglet

def center_image_anchor(image): 
    """Sets an image's anchor point to its center""" 
    image.anchor_x = image.width/2 
    image.anchor_y = image.height/2
    return image
