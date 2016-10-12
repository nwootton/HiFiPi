# HiFiPi #

So not the most original name I know, but it's not the most original project either.

This is a collection of Python scripts that are used to control some simple buttons attached to the GPIO connectors on my RPi2 board.

This is more of an experiment than production quality code. I'm trying to figure things out as well as get something that will work for the physical build.

At time of writing this README, the odd numbered files (v1,v3 etc ) contain code designed to work with a single momentary switch attached to GPIO pin 27 (Board pin number 13). These are generally extracts and/or snippets that are used to evaluate different methods of interacting with the GPIO.

The even numbered files (v2,v4) then take the simple example from the odd numbered files and expand it to handle the complete set of switches I want in the project.
