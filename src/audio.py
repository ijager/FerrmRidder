import pygame
import glob
import random
from collections import deque

class RidderAudio:

  def __init__(self, audiodir: str):
    pygame.mixer.init()
    self.audiodir = audiodir

    self.fallback = glob.glob(audiodir + '/*.wav')
    print('found fallback files:', self.fallback)

    self.intermezzo = glob.glob(audiodir + '/intermezzo/*.wav')
    print('found intermezzo files:', self.intermezzo)

    self.thankyou = glob.glob(audiodir + '/thankyou/*.wav')
    print('found thankyou files:', self.thankyou)

    self.startup = glob.glob(audiodir + '/startup/*.wav')
    print('found startupfiles:', self.startup)

    N = (len(self.intermezzo) + len(self.thankyou)) // 2

    self.recently_played = deque(maxlen=N//2)
    self.sound = None

  def play_random_startup(self):
    f = random.choice(self.startup)
    return self.play(f)

  def play_filtered_random(self, options):
    """
    Pick a random file from the list,
    but make sure it is not in the list of recently played.
    Because we don't really want true randomness..
    """
    tries = 10
    f = None
    while not f:
      f = random.choice(options)
      if f in self.recently_played:
        tries -= 1
        if tries == 0:
          # too many tries, just use this pick then
          break
        # set f to None to try again
        f = None

    self.recently_played.append(f)
    return self.play(f)

  def play_random_thankyou(self):
    return self.play_filtered_random(self.thankyou)

  def play_random_intermezzo(self):
    return self.play_filtered_random(self.intermezzo)

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
      print("Error playing ", f)
      return self.play_fallback()
