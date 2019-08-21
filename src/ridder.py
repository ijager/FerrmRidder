#!/usr/bin/env python3
import time
import board

from audio import RidderAudio
from sensor import Distance
from leds import Leds

headLEDs = Leds(pin=board.D18, num_leds=4)
bodyLEDs = Leds(pin=board.D12, num_leds=4)
sensor = Distance('vl61')
audio = RidderAudio('../audio/')

start = time.time()
detect = 0
audioLength = 0

while True:

  now = time.time()

  if not detect and (now - start) > 20:
    start = now
    audioLength = audio.play_random_papierhier()

  if not detect and (now - start) < audioLength:
    headLEDs.randomColor()

  if not detect and (sensor.get() < 70):
    print('detect hand!')
    detect = now
    audioLength = audio.play_random_dankjewel()

  if detect and (now - detect) < audioLength:
    headLEDs.blink()
    time.sleep(0.2)
  else:
    detect = 0

  time.sleep(0.01)
