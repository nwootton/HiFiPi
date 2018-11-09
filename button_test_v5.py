#!/usr/bin/python
# -*- coding: utf-8 -*-

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
play_pause = 27     #Play/pause mpc toggle
power_off = 20      # sudo halt now

## Some functions
def mpdConnect(client, con_id):
    """
    Simple wrapper to connect MPD.
    """
    try:
        client.connect(**con_id)
    except SocketError:
        return False
    return True

def play_pause_toggle(channel):
    print("Play/Pause")
    client.pause()

def quit(channel):
    print("Shutdown")
    os.system("sudo shutdown -h now")

## MPD object instance
client = MPDClient()
if mpdConnect(client, CON_ID):
    print('Got connected!')
    status = client.status()
    print('status = ', status)
else:
    print('fail to connect MPD server.')
    sys.exit(1)

# Setup the Pin with Internal pullups enabled and PIN in reading mode.
GPIO.setmode(GPIO.BCM)
GPIO.setup(play_pause, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(power_off, GPIO.IN, GPIO.PUD_UP)

# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(play_pause, GPIO.FALLING, callback=play_pause_toggle, bouncetime=2000)
GPIO.add_event_detect(power_off, GPIO.FALLING, callback=quit, bouncetime=2000)
