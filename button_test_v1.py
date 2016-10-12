# Assumes switch is connected to GND - so uses PULL UP
#!/usr/bin/python

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = 27

GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

while True:
  button_state = GPIO.input(button)
  if button_state == GPIO.HIGH:
    print ("HIGH")
  else:
    #print ("LOW")
    pass

    time.sleep(0.5)
