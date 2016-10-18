# HiFiPi #

So not the most original name I know, but it's not the most original project either.

This is a collection of Python scripts that are used to control some simple buttons attached to the GPIO connectors on my RPi2 board running Volumio music player.

This is more of an experiment than production quality code. I'm trying to figure things out as well as get something that will work for the physical build.

At time of writing this README, the odd numbered files (v1,v3 etc ) contain code designed to work with a single momentary switch attached to GPIO pin 27 (Board pin number 13). These are generally extracts and/or snippets that are used to evaluate different methods of interacting with the GPIO.

The even numbered files (v2,v4) then take the simple example from the odd numbered files and expand it to handle the complete set of switches I want in the project.

## Schematic ##

[Simple schematic](./images/HiFiPi_bb.jpg) here.

*Update*: This was my original schematic that uses GPIO_Pin 17 for 'play' & GPIO_Pin 27 for 'pause'. GPIO_Pin 17 is already taken by the IR controller on the x400 board. However you can use 'toggle' with mpc, so GPIO_Pin 27 has been used as a play/pause control and GPIO_Pin 17 has been ignored.

```bash
mpc toggle
```
