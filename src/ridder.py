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



#####

app = StateMachine()

while True:
  app.processState()
  time.sleep(0.01)



from enum import Enum


class AppState(Enum):
  IDLE = 1
  DETECT = 2
  INTERMEZZO = 3


class StateMachine:

  def __init__(self):
    self.state = AppState.IDLE
    self.start = time.time()
    self.stateCount = 0

    self.wavAnimation = None

  def processState(self):

    now = time.time()

    state_time = now - self.start

    if self.state == AppState.IDLE:
      nextState = self.idleState(state_time)
    elif self.state == AppState.INTERMEZZO:
      nextState = self.intermezzoState(state_time)
    elif self.state == AppState.DETECT:
      nextState = self.detectState(state_time)
    else:
      self.state = AppState.IDLE

    self.stateCount += 1

    if nextState != self.state:
      # state transition: reset stuff
      self.start = time.time()
      self.stateCount = 0
      LEDs.off()
      self.state = nextState

  def idleState(self, t) -> AppState:

    # first entry
    if self.stateCount == 0:
      pass

    # show idle animation

    if sensor.get() < DetectThreshold_mm:
      return AppState.DETECT

    if t > PapierHierInterval_s:
      return AppState.INTERMEZZO

  def intermezzoState(self, t) -> AppState:

    # first entry
    if self.stateCount == 0:
      wav, audioLength = audio.play_random_papierhier()
      self.wavAnimation = loadAnimation(wav, audioLength)
      dice = random.choice(range(6))

    if dice == 5:
      LEDs.randomColor()
    else:
      LEDs.applyAnimation(wavAnimation, t)

    # still check for sensor event
    if sensor.get() < DetectThreshold_mm:
      return AppState.DETECT
    elif t < audioLength:
      return AppState.INTERMEZZO
    else:
      return AppState.IDLE

  def detectState(self, t) -> AppState:

    # first entry
    if self.stateCount == 0:
      print('detect hand!')
      wav, audioLength = audio.play_random_dankjewel()
      self.wavAnimation = loadAnimation(wav, audioLength)

    LEDs.applyAnimation(wavAnimation, t)

    if t < audioLength:
      return AppState.DETECT
    else:
      return AppState.IDLE





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
