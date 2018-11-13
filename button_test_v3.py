#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
	Assumes switch is connected to GND - so uses PULL UP
"""

import os
import time
import RPi.GPIO as GPIO

# Define GPIO Pins that have buttons
PLAY_PAUSE = 27     #Play/pause mpc toggle
STOP = 22           #mpc STOP
PREV_TRACK = 18     #mpc prev
NEXT_TRACK = 23     #mpc next
STN_1 = 13          #radio station from playlist
STN_2 = 12          #radio station from playlist
STN_3 = 26          #radio station from playlist

POWER_OFF = 20      # sudo halt now


# Setup the Pin with Internal pullups enabled and PIN in reading mode.
GPIO.setmode(GPIO.BCM)
GPIO.setup(PLAY_PAUSE, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(POWER_OFF, GPIO.IN, GPIO.PUD_UP)

# Our function on what to do when the button is pressed
def shutdown():
    """ Turns off RPi """
    print("Shutting down")
    os.system("sudo shutdown -h now")

# Define callbacks for event detection
def play_pause_toggle():
    """ Toggle play pause via MPC daemon """
    print("Play/Pause")
    subprocess.call(['mpc', 'toggle'])

# Add our function to execute when the button pressed event happens
#GPIO.add_event_detect(PLAY_PAUSE, GPIO.FALLING, callback = PLAY_PAUSE_toggle, bouncetime = 2000)
#GPIO.add_event_detect(POWER_OFF, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)

GPIO.add_event_detect(PLAY_PAUSE, GPIO.RISING, callback=play_pause_toggle, bouncetime=2000)
GPIO.add_event_detect(POWER_OFF, GPIO.RISING, callback=shutdown, bouncetime=2000)

# Now wait!
while 1:
    time.sleep(0.5)
