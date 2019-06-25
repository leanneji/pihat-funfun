#!/usr/bin/env python
#this script will show a matrix of colors on the Pi HAT
from sense_hat import SenseHat
sense = SenseHat ()
import time

r = (255, 0, 0)
w = (10, 10, 10)

pixels = [
    r, r, r, r, r, r, r, r,
    r, r, r, w, w, r, r, r,
    r, r, r, w, w, r, r, r,
    r, w, w, w, w, w, w, r,
    r, w, w, w, w, w, w, r,
    r, r, r, w, w, r, r, r,
    r, r, r, w, w, r, r, r,
    r, r, r, r, r, r, r, r,
 ]

sense.set_pixels(pixels)

time.sleep(5)


m = (139, 0, 0)
w = (10, 10, 10)

pixels = [
    w, m, m, m, m, m, m, m,
    w, w, m, m, m, m, m, m,
    w, m, m, m, m, m, m, m,
    w, w, m, m, m, m, m, m,
    w, m, m, m, m, m, m, m,
    w, w, m, m, m, m, m, m,
    w, m, m, m, m, m, m, m,
    w, w, m, m, m, m, m, m,
 ]

sense.set_pixels(pixels)

time.sleep(5)




sense.clear()
