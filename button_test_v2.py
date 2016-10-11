# Assumes switch is connected to GND - so uses PULL UP


import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

play_pause = 27
stop = 22
prev_track = 18
next_track = 23
stn_1 = 13
stn_2 = 19
stn_3 = 26

power_off = 21

GPIO.setup(play_pause, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(stop, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(prev_track, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(next_track, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(stn_1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(stn_2, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(stn_3, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(power_off, GPIO.IN, GPIO.PUD_UP)

while True:
    if GPIO.input(play_pause) == True:
        print ("Play/Pause")
    elif GPIO.input(stop) == True:
        print ("Stop")
    elif GPIO.input(prev_track) == True:
        print ("Previous")
    elif GPIO.input(next_track) == True:
        print ("Next")
    elif GPIO.input(stn_1) == True:
        print ("Station 1")
    elif GPIO.input(stn_2) == True:
        print ("Station 2")
    elif GPIO.input(stn_3) == True:
        print ("Station 3")
    elif GPIO.input(power_off) == True:
        print ("Shutdown")
    else:
        print ("Nothing")

    time.sleep(0.5)
