#!/usr/bin/env python

'''Test L load using PyPNG.  You should see the l.png image on 
a checkboard background.
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id: PYPNG_L_LOAD.py 661 2007-02-17 00:23:30Z Alex.Holkner $'

import unittest
import base_load

from pyglet.image.codecs.png import PNGImageDecoder

class TEST_PNG_L_LOAD(base_load.TestLoad):
    texture_file = 'l.png'
    decoder = PNGImageDecoder()

if __name__ == '__main__':
    unittest.main()
