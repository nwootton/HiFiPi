#!/usr/bin/python
# -*- coding: utf-8 -*-

# IMPORTS
import sys
import time
from mpd import MPDClient

HOST = 'localhost'
PORT = '6600'
PASSWORD = False

client = MPDClient ()
client.connect(HOST, PORT)
status=client.status()
print 'status = ', status

client.play()

client.disconnect()
