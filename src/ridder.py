#!/usr/bin/env python3
import time
import board
import pickle
import random

from audio import RidderAudio
from sensor import Distance
from leds import Leds, RGB, WavAnimation, FadeAnimation

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

def loadAnimation(wav, audioLength, color=None):
    picklefile = wav.replace('.wav', '.pkl')
    with open(picklefile, 'rb') as f:
        animationData = pickle.load(f)
    return WavAnimation(animationData, audioLength, color)



#####


from enum import Enum


class AppState(Enum):
  STARTUP = 0
  IDLE = 1
  DETECT = 2
  INTERMEZZO = 3
  BONUS = 4
  


class StateMachine:

  def __init__(self):
    self.state = AppState.STARTUP
    self.start = time.time()
    self.stateCount = 0
    self.audioLength = 0
    self.dice = 0
    self.ledAnimation = None

  def processState(self):

    now = time.time()

    state_time = now - self.start
    nextState = self.state

    if self.state == AppState.IDLE:
      nextState = self.idleState(state_time)
    elif self.state == AppState.INTERMEZZO:
      nextState = self.intermezzoState(state_time)
    elif self.state == AppState.DETECT:
      nextState = self.detectState(state_time)
    elif self.state == AppState.BONUS:
      nextState = self.bonusState(state_time)
    elif self.state == AppState.STARTUP:
      nextState = self.startupState(state_time)
    else:
      self.state = AppState.IDLE

    self.stateCount += 1

    if nextState != self.state:
      # state transition: reset stuff
      self.start = time.time()
      self.stateCount = 0
      LEDs.off()
      print('transition: ', self.state , ' to ', nextState)
      self.state = nextState

  def startupState(self, t) -> AppState:

    # first entry
    if self.stateCount == 0:

      wav, self.audioLength = audio.play_random_startup()
      #self.ledAnimation = loadAnimation(wav, self.audioLength, color=RGB(255,0,0))
      self.ledAnimation = FadeAnimation(
              RGB(255,0,0),
              15)

    # show animation
    LEDs.applyAnimation(self.ledAnimation, t)

    if t > self.audioLength:
      return AppState.IDLE
    else:
      return AppState.STARTUP


  def idleState(self, t) -> AppState:

    # first entry
    if self.stateCount == 0:
      self.ledAnimation = FadeAnimation(
              FadeColor,
              FadeDuration_s)

    # show idle animation
    LEDs.applyAnimation(self.ledAnimation, t)

    if sensor.get() < DetectThreshold_mm:
      return AppState.DETECT

    if t > PapierHierInterval_s:
      return AppState.INTERMEZZO

    bonusDice = random.choice(range(100000))
    if bonusDice == 31:
        print('bonusDice = ', bonusDice)
        return AppState.BONUS



    return AppState.IDLE

  def intermezzoState(self, t) -> AppState:

    # first entry
    if self.stateCount == 0:
      wav, self.audioLength = audio.play_random_papierhier()
      self.ledAnimation = loadAnimation(wav, self.audioLength)
      self.dice = random.choice(range(6))

    if self.dice == 5:
      LEDs.randomColor()
    else:
      LEDs.applyAnimation(self.ledAnimation, t)

    # still check for sensor event
    if sensor.get() < DetectThreshold_mm:
      return AppState.DETECT
    elif t < self.audioLength:
      return AppState.INTERMEZZO
    else:
      return AppState.IDLE

  def detectState(self, t) -> AppState:

    # first entry
    if self.stateCount == 0:
      print('detect hand!')
      wav, self.audioLength = audio.play_random_dankjewel()
      self.ledAnimation = loadAnimation(wav, self.audioLength)

    LEDs.applyAnimation(self.ledAnimation, t)

    if t < self.audioLength:
      return AppState.DETECT
    else:
      return AppState.IDLE


  def bonusState(self, t) -> AppState:

    # first entry
    if self.stateCount == 0:
      self.ledAnimation = FadeAnimation(
              RGB(255,0,0),
              1)

    # show idle animation
    LEDs.applyAnimation(self.ledAnimation, t)

    if t > 5:
      return AppState.IDLE
    else:
      return AppState.BONUS

app = StateMachine()

while True:
  app.processState()
  time.sleep(0.01)

