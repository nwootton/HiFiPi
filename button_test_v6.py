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
stop = 22           #mpc stop
prev_track = 18     #mpc prev
next_track = 23     #mpc next
stn_1 = 13          #radio station from playlist
stn_2 = 12          #radio station from playlist
stn_3 = 26          #radio station from playlist

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
    print ("Play/Pause")
    client.pause()

def stop_play(channel):
    print ("Stop")
    client.stop()

def prv(channel):
    print ("Previous")
    client.previous()

def nxt(channel):
    print ("Next")
    client.next()

def stn1(channel):
    print ("Station 1")

def stn2(channel):
    print ("Station 2")

def stn3(channel):
    print ("Station 3")

def quit(channel):
    print ("Shutdown")
    os.system("sudo shutdown -h now")

## MPD object instance
client = MPDClient()
if mpdConnect(client, CON_ID):
    print('Got connected!')
    status=client.status()
    print 'status = ', status
else:
    print('fail to connect MPD server.')
    sys.exit(1)

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

# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(play_pause, GPIO.FALLING, callback = play_pause_toggle, bouncetime = 2000)
GPIO.add_event_detect(stop,  GPIO.FALLING, callback = stop_play, bouncetime = 2000)
GPIO.add_event_detect(prev_track,  GPIO.FALLING, callback = prv, bouncetime = 2000)
GPIO.add_event_detect(next_track,  GPIO.FALLING, callback = nxt, bouncetime = 2000)
GPIO.add_event_detect(stn_1,  GPIO.FALLING, callback = stn1, bouncetime = 2000)
GPIO.add_event_detect(stn_2,  GPIO.FALLING, callback = stn2, bouncetime = 2000)
GPIO.add_event_detect(stn_3,  GPIO.FALLING, callback = stn3, bouncetime = 2000)
GPIO.add_event_detect(power_off,  GPIO.FALLING, callback = quit, bouncetime = 2000)
