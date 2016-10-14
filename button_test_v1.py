#!/usr/bin/env python
# Assumes switch is connected to GND - so uses PULL UP

import subprocess
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = 27

GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

while True:
  button_state = GPIO.input(button)
  if button_state == GPIO.HIGH:
    pass
  else:
    print ("Acting")
    subprocess.call(['mpc', 'toggle' ])
  time.sleep(0.5)
