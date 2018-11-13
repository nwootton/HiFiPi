#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	First attempt at getting a button to work with the MPC daemon
	Assumes switch is connected to GND - so uses PULL UP
"""

import subprocess
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

BUTTON = 27

GPIO.setup(BUTTON, GPIO.IN, GPIO.PUD_UP)

while True:
    BUTTON_STATE = GPIO.input(BUTTON)
    if BUTTON_STATE == GPIO.HIGH:
        pass
    else:
        print("Acting")
        subprocess.call(['mpc', 'toggle'])
    time.sleep(0.5)
