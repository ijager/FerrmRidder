import pygame
import glob
import random

class RidderAudio:

  def __init__(self, audiodir: str):
    pygame.mixer.init()
    self.audiodir = audiodir

    self.fallback = glob.glob(audiodir + '/*.wav')
    print('found fallback files:', self.fallback)

    self.intermezzo = glob.glob(audiodir + '/intermezzo/*.wav')
    print('found intermezzo files:', self.intermezzo)

    self.dankjewel = glob.glob(audiodir + '/thankyou/*.wav')
    print('found dankjewel files:', self.dankjewel)

    self.startup = glob.glob(audiodir + '/startup/*.wav')
    print('found startupfiles:', self.startup)

    self.sound = None

  def play_random_startup(self):
    f = random.choice(self.startup)
    return self.play(f)

  def play_random_dankjewel(self):
    f = random.choice(self.dankjewel)
    return self.play(f)

  def play_random_intermezzo(self):
    f = random.choice(self.intermezzo)
    return self.play(f)

  def play_fallback(self):
    f = self.fallback[0]
    self.sound = pygame.mixer.Sound(f)
    print('playing:', f, ' with length: ',     self.sound.get_length())

    self.sound.play()
    return (f, self.sound.get_length())

  def play(self, f):
    # first stop sound if one is currently playing
    if self.sound:
        self.sound.stop()

    try:
      self.sound = pygame.mixer.Sound(f)
      print('playing:', f, ' with length: ',     self.sound.get_length())

      self.sound.play()
      return (f, self.sound.get_length())
    except:
      return self.play_fallback()
