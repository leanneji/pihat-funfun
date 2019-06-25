#! /usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time

color = (99, 99, 99)

def heart (color):
    sense.set_pixel (1, 7, (color))
    sense.set_pixel (0, 6, (color))
    sense.set_pixel (0, 5, (color))
    sense.set_pixel (1, 6, (color))
    sense.set_pixel (2, 6, (color))
    sense.set_pixel (2, 5, (color))
    time.sleep(1)

heart(color)

color = (100, 0, 0)

heart(color)
 

sense.clear()
