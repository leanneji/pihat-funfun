#!/usr/bin/env python
#this script will define colors for a scrolling message on the Pi HAT
from sense_hat import SenseHat
sense = SenseHat()

#use RGB values to define colors
leanne = (75, 0, 130)
claire = (255, 99, 71)

speed = 0.06

message = raw_input()

sense.show_message(message, speed, text_colour=leanne, back_colour=claire)

sense.clear()
