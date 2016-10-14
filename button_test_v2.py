#!/usr/bin/python
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
stn_2 = 19          #radio station from playlist
stn_3 = 26          #radio station from playlist

power_off = 21      # sudo halt now

#Configure PULL Up and pin connections
GPIO.setup(play_pause, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(stop, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(prev_track, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(next_track, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(stn_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(stn_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(stn_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(power_off, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Begin loop to wait for button press
while True:
    if GPIO.input(play_pause) == GPIO.LOW:
        print ("Play/Pause")
        subprocess.call(['mpc', 'toggle' ])
    elif GPIO.input(stop) == GPIO.LOW:
        print ("Stop")
        subprocess.call(['mpc', 'stop' ])
    elif GPIO.input(prev_track) == GPIO.LOW:
        print ("Previous")
        subprocess.call(['mpc', 'prev' ])
    elif GPIO.input(next_track) == GPIO.LOW:
        print ("Next")
        subprocess.call(['mpc', 'next' ])
    elif GPIO.input(stn_1) == GPIO.LOW:
        print ("Station 1")
    elif GPIO.input(stn_2) == GPIO.LOW:
        print ("Station 2")
    elif GPIO.input(stn_3) == GPIO.LOW:
        print ("Station 3")
    elif GPIO.input(power_off) == GPIO.LOW:
        print ("Shutdown")
        os.system("sudo shutdown -h now") # Send shutdown command to os
    else:
        #print ("Nothing")
        pass

    time.sleep(0.25)
