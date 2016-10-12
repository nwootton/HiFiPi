
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = 27 #Play/pause pin

GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

GPIO.add_event_detect(button, GPIO.RISING)  # add rising edge detection on a button

if GPIO.event_detected(button):
    print('Button pressed')
