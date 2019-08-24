import pygame
import glob
import random

class RidderAudio:

  def __init__(self, audiodir: str):
    pygame.mixer.init()

    self.papierhier = glob.glob(audiodir + '/*papier*.wav')
    print('found papier hier files:', self.papierhier)

    self.dankjewel = glob.glob(audiodir + '/*dankjewel*.wav')
    print('found dankjewel files:', self.dankjewel)

    self.sound = None

  def play_random_dankjewel(self):

    if self.sound:
        self.sound.stop()
    f = random.choice(self.dankjewel)

    self.sound = pygame.mixer.Sound(f)
    print('playing:', f, ' with length: ',     self.sound.get_length())
    self.sound.play()
    return (f, self.sound.get_length())
    # pygame.mixer.music.load(f)
    # pygame.mixer.music.play()


  def play_random_papierhier(self):
    if self.sound:
        self.sound.stop()
    f = random.choice(self.papierhier)
    self.sound = pygame.mixer.Sound(f)
    print('playing:', f, ' with length: ',     self.sound.get_length())

    self.sound.play()
    return (f, self.sound.get_length())
    # pygame.mixer.music.load(f)
    # pygame.mixer.music.play()
