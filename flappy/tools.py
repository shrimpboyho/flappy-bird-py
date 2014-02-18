import pyglet

def center_image_anchor(image): 
    """Sets an image's anchor point to its center""" 
    image.anchor_x = image.width/2 
    image.anchor_y = image.height/2
    return image

def play_audio(src, loop=False):
    try:
        audio = pyglet.resource.media(src)
        if loop:
            audio.EOS_LOOP = 'loop'
        # Possible bug with pulseaudio kernel 3.2.0-29 x86 (up to 32 streams)
        audio.play()
    except:
        pass