#!/usr/bin/python
# -*- coding: utf-8 -*-
""" Version 5 """

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

CON_ID = {'host':HOST, 'port':PORT}


# Define GPIO Pins that have buttons
PLAY_PAUSE = 27     #Play/pause mpc toggle
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
    """ Play pause toggle """
    print("Play/Pause")
    CLIENT.pause()

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
GPIO.setup(POWER_OFF, GPIO.IN, GPIO.PUD_UP)

# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(PLAY_PAUSE, GPIO.FALLING, callback=play_pause_toggle, bouncetime=2000)
GPIO.add_event_detect(POWER_OFF, GPIO.FALLING, callback=shutdown, bouncetime=2000)
