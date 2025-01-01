# osc2midi2dmx
OSC over wifi to MIDI, for controlling DMX controller. targeting QLC+  and Strand Lighting 250ML

QLC+ outputs OSC over wifi to RPI, which translates the messages to Midi Commands that the 250ML accepts.

# The story
Having a Strand Lighting 250ML at my disposal, I wanted to use QLC+ alongside. Using DMX did not allow me to control the table to my liking. So i attempted to control it using the usb-midi adapter that was lying around. While searching for the adapter i found my old RPI-Zero. Then I though, how cool if i can control the 250ML wirelessly from my laptop, using the RPI as a OSC-over-Wifi to Midi adapter. 

# installation instruction on RPI:

besides the python packages as in requirements.txt: 
- sudo apt-get install libasound2-dev 
- sudo apt-get install libjack-dev 
