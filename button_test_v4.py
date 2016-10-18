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
play_pause = 27     #Play/pause mpc toggle
stop = 22           #mpc stop
prev_track = 18     #mpc prev
next_track = 23     #mpc next
stn_1 = 13          #radio station from playlist
stn_2 = 12          #radio station from playlist
stn_3 = 26          #radio station from playlist

power_off = 20      # sudo halt now

#Configure PULL Up and pin connections
GPIO.setup(play_pause, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(stop, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(prev_track, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(next_track, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(stn_1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(stn_2, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(stn_3, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(power_off, GPIO.IN, GPIO.PUD_UP)

#Define callbacks for event detection
def play_pause_toggle(channel):
    print ("Play/Pause")
    #subprocess.call(['mpc', 'toggle' ])

def stop_play(channel):
    print ("Stop")

def prv(channel):
    print ("Previous")

def nxt(channel):
    print ("Next")

def stn1(channel):
    print ("Station 1")

def stn2(channel):
    print ("Station 2")

def stn3(channel):
    print ("Station 3")

def quit(channel):
    print ("Shutdown")
    #os.system("sudo shutdown -h now")

# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(play_pause, GPIO.FALLING, callback = play_pause_toggle, bouncetime = 2000)
GPIO.add_event_detect(stop,  GPIO.FALLING, callback = stop_play, bouncetime = 2000)
GPIO.add_event_detect(prev_track,  GPIO.FALLING, callback = prv, bouncetime = 2000)
GPIO.add_event_detect(next_track,  GPIO.FALLING, callback = nxt, bouncetime = 2000)
GPIO.add_event_detect(stn_1,  GPIO.FALLING, callback = stn1, bouncetime = 2000)
GPIO.add_event_detect(stn_2,  GPIO.FALLING, callback = stn2, bouncetime = 2000)
GPIO.add_event_detect(stn_3,  GPIO.FALLING, callback = stn3, bouncetime = 2000)
GPIO.add_event_detect(power_off,  GPIO.FALLING, callback = quit, bouncetime = 2000)

# Now wait!
while 1:
    time.sleep(0.5)
