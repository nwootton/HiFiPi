#!/usr/bin/python
# Assumes switch is connected to GND - so uses PULL UP

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


GPIO.add_event_callback(play_pause, play_pause_toggle)
GPIO.add_event_callback(stop, stop_play)
GPIO.add_event_callback(prev_track, prv)
GPIO.add_event_callback(next_track, nxt)
GPIO.add_event_callback(stn_1, stn1)
GPIO.add_event_callback(stn_2, stn2)
GPIO.add_event_callback(stn_3, stn3)
GPIO.add_event_callback(power_off, quit)
