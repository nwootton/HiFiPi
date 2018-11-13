#!/usr/bin/python
# -*- coding: utf-8 -*-
""" Version 6 """

# IMPORTS
import os
import sys
import time
from mpd import MPDClient
import RPi.GPIO as GPIO
from socket import error as SocketError

HOST = 'localhost'
PORT = '6600'
PASSWORD = False
##
CON_ID = {'host':HOST, 'port':PORT}
##

# Define GPIO Pins that have buttons
PLAY_PAUSE = 27     #Play/pause mpc toggle
STOP = 22           #mpc stop
PREV_TRACK = 18     #mpc prev
NEXT_TRACK = 23     #mpc next
STN_1 = 13          #radio station from playlist
STN_2 = 12          #radio station from playlist
STN_3 = 26          #radio station from playlist

POWER_OFF = 20      # sudo halt now

## Some functions
def mpdConnect(client, con_id):
    """ Simple wrapper to connect MPD. """
    try:
        client.connect(**con_id)
    except SocketError:
        return False
    return True

def play_pause_toggle():
    """ Play pause """
    print("Play/Pause")
    CLIENT.pause()

def stop_play():
    """ Stop """
    print("Stop")
    CLIENT.stop()

def prv():
    """ Previous """
    print("Previous")
    CLIENT.previous()

def nxt():
    """ Next """
    print("Next")
    CLIENT.next()

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
    os.system("sudo shutdown -h now")

## MPD object instance
CLIENT = MPDClient()
if mpdConnect(CLIENT, CON_ID):
    print('Got connected!')
    STATUS = CLIENT.status()
    print('status = ', STATUS)
else:
    print('fail to connect MPD server.')
    sys.exit(1)

# Setup the Pin with Internal pullups enabled and PIN in reading mode.
GPIO.setmode(GPIO.BCM)
GPIO.setup(PLAY_PAUSE, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(STOP, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(PREV_TRACK, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(NEXT_TRACK, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(STN_1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(STN_2, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(STN_3, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(POWER_OFF, GPIO.IN, GPIO.PUD_UP)

# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(PLAY_PAUSE, GPIO.FALLING, callback=play_pause_toggle, bouncetime=2000)
GPIO.add_event_detect(STOP, GPIO.FALLING, callback=stop_play, bouncetime=2000)
GPIO.add_event_detect(PREV_TRACK, GPIO.FALLING, callback=prv, bouncetime=2000)
GPIO.add_event_detect(NEXT_TRACK, GPIO.FALLING, callback=nxt, bouncetime=2000)
GPIO.add_event_detect(STN_1, GPIO.FALLING, callback=stn1, bouncetime=2000)
GPIO.add_event_detect(STN_2, GPIO.FALLING, callback=stn2, bouncetime=2000)
GPIO.add_event_detect(STN_3, GPIO.FALLING, callback=stn3, bouncetime=2000)
GPIO.add_event_detect(POWER_OFF, GPIO.FALLING, callback=shutdown, bouncetime=2000)
