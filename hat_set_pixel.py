#! /usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time

sense.set_pixel (2, 2, (32, 178, 170))
sense.set_pixel (4, 2, (32, 178, 170))
sense.set_pixel (3, 4, (32, 178, 170))
sense.set_pixel (1, 5, (32, 178, 170))
sense.set_pixel (2, 6, (32, 178, 170))
sense.set_pixel (3, 6, (32, 178, 170))
sense.set_pixel (4, 6, (32, 178, 170))
sense.set_pixel (5, 5, (32, 178, 170))

time.sleep(1)

sense.set_pixel (2, 2, (0, 0, 0))

time.sleep(.2)

sense.set_pixel (2, 2, (32, 178, 170))

time.sleep(1)

sense.clear()
