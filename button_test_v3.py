#!/usr/bin/python
# Assumes switch is connected to GND - so uses PULL UP

import subprocess
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Define callbacks for event detection
def play_pause_toggle(channel):
    print ("Play/Pause")
    subprocess.call(['mpc', 'toggle' ])

#Define GPIO Pins that have buttons
play_pause = 27     #Play/pause mpc toggle

GPIO.setup(play_pause, GPIO.IN, GPIO.PUD_UP)

GPIO.add_event_detect(play_pause, GPIO.RISING)  # add rising edge detection on a button
GPIO.add_event_callback(play_pause, play_pause_toggle) #Call function when detected
