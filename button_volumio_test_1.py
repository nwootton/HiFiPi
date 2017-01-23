#!/usr/bin/python
# -*- coding: utf-8 -*-

# IMPORTS
import os
import sys
import time
import RPi.GPIO as GPIO

#Misc states
pp_state = 0        #Play/Pause state 1 = Playing, 0 = Paused
volume = 0
clikLastState = GPIO.input(clik)

# Define GPIO Pins that have buttons
play_pause = 27     #Play/pause mpc toggle
stop = 22           #mpc stop
prev_track = 18     #mpc prev
next_track = 23     #mpc next
stn_1 = 13          #radio station from playlist
stn_2 = 12          #radio station from playlist
stn_3 = 26          #radio station from playlist

power_off = 20      # sudo halt now

clik = 5            #volume dial clik
dot = 6             #volume dial dot

#Functions
def play_pause_toggle(channel):
    print ("Play/Pause")
    if pp_state == 0:
        print ("Playing")
        os.system("volumio play")
    else:
        print ("Paused")
        os.system("volumio pause")

def stop_play(channel):
    print ("Stop")
    os.system("volumio stop")

def prv(channel):
    print ("Previous")
    os.system("volumio previous")

def nxt(channel):
    print ("Next")
    os.system("volumio next")

def stn1(channel):
    print ("Station 1")

def stn2(channel):
    print ("Station 2")

def stn3(channel):
    print ("Station 3")

def quit(channel):
    print ("Shutdown")
    os.system("sudo shutdown -h now")

def changeVol(newVolume):
    print ("New volume is " + newVolume)
    os.system("volumio volume " + newVolume)

try:

    while True:
        clikState = GPIO.input(clik)
        dotState = GPIO.input(dot)
        if clikState != clikLastState:
            if dotState != clikState:
                volume += 1
            else:
                volume -= 1
            print volume
            changeVol(volume)
        clikLastState = clikState
        sleep(0.01)
finally:
        GPIO.cleanup()

# Setup the Pin with Internal pullups enabled and PIN in reading mode.
GPIO.setmode(GPIO.BCM)
GPIO.setup(play_pause, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(stop, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(prev_track, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(next_track, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(stn_1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(stn_2, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(stn_3, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(power_off, GPIO.IN, GPIO.PUD_UP)

GPIO.setup(clik, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dot, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(play_pause, GPIO.FALLING, callback = play_pause_toggle, bouncetime = 2000)
GPIO.add_event_detect(stop,  GPIO.FALLING, callback = stop_play, bouncetime = 2000)
GPIO.add_event_detect(prev_track,  GPIO.FALLING, callback = prv, bouncetime = 2000)
GPIO.add_event_detect(next_track,  GPIO.FALLING, callback = nxt, bouncetime = 2000)
GPIO.add_event_detect(stn_1,  GPIO.FALLING, callback = stn1, bouncetime = 2000)
GPIO.add_event_detect(stn_2,  GPIO.FALLING, callback = stn2, bouncetime = 2000)
GPIO.add_event_detect(stn_3,  GPIO.FALLING, callback = stn3, bouncetime = 2000)
GPIO.add_event_detect(power_off,  GPIO.FALLING, callback = quit, bouncetime = 2000)
