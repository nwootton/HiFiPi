#!/usr/bin/python
# -*- coding: utf-8 -*-
# Assumes switch is connected to GND - so uses PULL UP

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

#Define callbacks for event detection
def play_pause_toggle():
    """ Play pause toggle """
    print("Play/Pause")
    #subprocess.call(['mpc', 'toggle' ])

def stop_play():
    """ Stop """
    print("STOP")

def prv():
    """ Previous track """
    print("Previous")

def nxt():
    """ Next track """
    print("Next")

def stn1():
    """ Radio preset """
    print("Station 1")

def stn2():
    """ Radio preset """
    print("Station 2")

def stn3():
    """ Radio preset """
    print("Station 3")

def shutdown():
    """ Shutdown RPi """
    print("Shutdown")
    #os.system("sudo shutdown -h now")

# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(PLAY_PAUSE, GPIO.FALLING, callback=play_pause_toggle, bouncetime=2000)
GPIO.add_event_detect(STOP, GPIO.FALLING, callback=stop_play, bouncetime=2000)
GPIO.add_event_detect(PREV_TRACK, GPIO.FALLING, callback=prv, bouncetime=2000)
GPIO.add_event_detect(NEXT_TRACK, GPIO.FALLING, callback=nxt, bouncetime=2000)
GPIO.add_event_detect(STN_1, GPIO.FALLING, callback=stn1, bouncetime=2000)
GPIO.add_event_detect(STN_2, GPIO.FALLING, callback=stn2, bouncetime=2000)
GPIO.add_event_detect(STN_3, GPIO.FALLING, callback=stn3, bouncetime=2000)
GPIO.add_event_detect(POWER_OFF, GPIO.FALLING, callback=shutdown, bouncetime=2000)

# Now wait!
while 1:
    time.sleep(0.5)
