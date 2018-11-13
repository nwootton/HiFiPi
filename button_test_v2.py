#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    Assumes switch is connected to GND - so uses PULL UP
"""

import os
import subprocess
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Define GPIO Pins that have buttons
PLAY_PAUSE = 27     #Play/pause mpc toggle
STOP = 22           #mpc STOP
PREV_TRACK = 18     #mpc prev
NEXT_TRACK = 23     #mpc next
STN_1 = 13          #radio station from playlist
STN_2 = 12          #radio station from playlist
STN_3 = 26          #radio station from playlist

POWER_OFF = 20      # sudo halt now

#Configure PULL Up and pin connections
GPIO.setup(PLAY_PAUSE, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(STOP, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(PREV_TRACK, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(NEXT_TRACK, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(STN_1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(STN_2, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(STN_3, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(POWER_OFF, GPIO.IN, GPIO.PUD_UP)

#Begin loop to wait for button press
while True:
    if GPIO.input(PLAY_PAUSE) == GPIO.LOW:
        print("Play/Pause")
        subprocess.call(['mpc', 'toggle'])
    elif GPIO.input(STOP) == GPIO.LOW:
        print("STOP")
        subprocess.call(['mpc', 'STOP'])
    elif GPIO.input(PREV_TRACK) == GPIO.LOW:
        print("Previous")
        subprocess.call(['mpc', 'prev'])
    elif GPIO.input(NEXT_TRACK) == GPIO.LOW:
        print("Next")
        subprocess.call(['mpc', 'next'])
    elif GPIO.input(STN_1) == GPIO.LOW:
        print("Station 1")
    elif GPIO.input(STN_2) == GPIO.LOW:
        print("Station 2")
    elif GPIO.input(STN_3) == GPIO.LOW:
        print("Station 3")
    elif GPIO.input(POWER_OFF) == GPIO.LOW:
        print("Shutdown")
        #os.system("sudo shutdown -h now") # Send shutdown command to os
    else:
        #print ("Nothing")
        pass

    time.sleep(0.25)
