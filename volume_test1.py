#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Assumes switch is connected to GND - so uses PULL UP
from RPi.GPIO import GPIO
from time import sleep

#Define GPIO Pins that have buttons
play_pause = 27     #Play/pause mpc toggle
stop = 22           #mpc stop
prev_track = 18     #mpc prev
next_track = 23     #mpc next
stn_1 = 13          #radio station from playlist
stn_2 = 12          #radio station from playlist
stn_3 = 26          #radio station from playlist

power_off = 20      # sudo halt now

clk = 5            #volume dial clk
dt = 6             #volume dial dt

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

volume = 0
clkLastState = GPIO.input(clk)

def changeVol(newVolume):
    print ("New volume is " + newVolume)

try:

    while True:
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if clkState != clkLastState:
            if dtState != clkState:
                volume += 1
            else:
                volume -= 1
            print volume
            #changeVol(volume)
        clkLastState = clkState
        sleep(0.01)
finally:
        GPIO.cleanup()
