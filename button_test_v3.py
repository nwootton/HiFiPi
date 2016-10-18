#!/usr/bin/python
# Assumes switch is connected to GND - so uses PULL UP
import RPi.GPIO as GPIO
import time
import os

# Define GPIO Pins that have buttons
play_pause = 27     #Play/pause mpc toggle
stop = 22           #mpc stop
prev_track = 18     #mpc prev
next_track = 23     #mpc next
stn_1 = 13          #radio station from playlist
stn_2 = 12          #radio station from playlist
stn_3 = 26          #radio station from playlist

power_off = 20      # sudo halt now


# Setup the Pin with Internal pullups enabled and PIN in reading mode.
GPIO.setmode(GPIO.BCM)
GPIO.setup(play_pause, GPIO.IN, GPIO.PUD_UP)

# Our function on what to do when the button is pressed
def Shutdown(channel):
    print ("Shutting down")
    os.system("sudo shutdown -h now")

# Define callbacks for event detection
def play_pause_toggle(channel):
    print ("Play/Pause")
    subprocess.call(['mpc', 'toggle' ])

# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(play_pause, GPIO.FALLING, callback = play_pause_toggle, bouncetime = 2000)
#GPIO.add_event_detect(play_pause, GPIO.RISING, callback = play_pause_toggle, bouncetime = 2000)

# Now wait!
while 1:
    time.sleep(0.5)
