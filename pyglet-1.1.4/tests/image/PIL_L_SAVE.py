#!/usr/bin/env python

'''Test L save using PIL.  You should see l.png reference image
on the left, and saved (and reloaded) image on the right.  The saved image
may have larger dimensions due to texture size restrictions.
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id: PIL_L_SAVE.py 661 2007-02-17 00:23:30Z Alex.Holkner $'

import unittest
import base_save

from pyglet.image.codecs.pil import PILImageEncoder

class TEST_PIL_L_SAVE(base_save.TestSave):
    texture_file = 'l.png'
    encoder = PILImageEncoder()

if __name__ == '__main__':
    unittest.main()
