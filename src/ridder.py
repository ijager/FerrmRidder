#!/usr/bin/env python3
import time
import board
import pickle
import random

from audio import RidderAudio
from sensor import Distance
from leds import Leds, RGB, WavAnimation

## Config
from config import *

## Start Script

LEDs = Leds(pin=board.D18, num_leds=NumLEDs)

sensor = Distance(SensorType)
audio = RidderAudio(AudioDir)

start = time.time()
detect = 0
dice = 0
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

  if not detect and tdiff > PapierHierInterval_s:
    start = now
    tdiff = 0
    wav, audioLength = audio.play_random_papierhier()
    wavAnimation = loadAnimation(wav, audioLength)
    dice = random.choice(range(6))

  if not detect and tdiff < audioLength:
    if dice == 5:
      LEDs.randomColor()
    else:
      if tdiff < audioLength:
        LEDs.applyAnimation(wavAnimation, tdiff)
      else:
        LEDs.off()

  if not detect and (sensor.get() < DetectThreshold_mm):
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