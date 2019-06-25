#!/usr/bin/env python 
from sense_hat import SenseHat
import time
import random
sense = SenseHat ()

x = random.randint (0,7)
y = random.randint (0,7)

r = random.randint (0, 255)
g = random.randint (0, 255)
b = random.randint (0, 255)

print("the x"), x, ("the y"), y, ("color"), r, g, b, ("this time")

sense.set_pixel (x, y, (r, g, b))
time.sleep(10)
sense.clear()
