#!/usr/bin/env python3
import time
import board
import pickle

from audio import RidderAudio
from sensor import Distance
from leds import Leds, RGB, WavAnimation

LEDs = Leds(pin=board.D18, num_leds=4)

sensor = Distance('vl61')
audio = RidderAudio('../audio/')

start = time.time()
detect = 0
audioLength = 0

wavAnimation = None

def loadAnimation(wav, audioLength):
    picklefile = wav.replace('.wav', '.pkl')
    with open(picklefile, 'rb') as f:
        animationData = pickle.load(f)
    return WavAnimation(animationData, audioLength)

while True:

  now = time.time()

  tdiff = now - start

  if not detect and tdiff > 20:
    start = now
    tdiff = 0
    wav, audioLength = audio.play_random_papierhier()
    wavAnimation = loadAnimation(wav, audioLength)

  if not detect and tdiff < audioLength:
    # LEDs.randomColor()
    if tdiff < audioLength:
      LEDs.applyAnimation(wavAnimation, tdiff)
    else:
      LEDs.off()

  if not detect and (sensor.get() < 70):
    print('detect hand!')
    detect = now
    wav, audioLength = audio.play_random_dankjewel()
    wavAnimation = loadAnimation(wav, audioLength)

  if detect:
    t = (now - detect)
    if t < audioLength:
        LEDs.applyAnimation(wavAnimation, t)
    else:
      LEDs.off()
      detect = 0

  time.sleep(0.01)