import pygame
import glob
import random

class RidderAudio:

  def __init__(self, audiodir: str):
    pygame.mixer.init()

    self.papierhier = glob.glob(audiodir + '/*papier*')
    print('found papier hier files:', self.papierhier)

    self.dankjewel = glob.glob(audiodir + '/*dankjewel*')
    print('found dankjewel files:', self.dankjewel)

  def play_random_dankjewel(self):
    f = random.choice(self.dankjewel)

    sound = pygame.mixer.Sound(f)
    print('playing:', f, ' with length: ',     sound.get_length())
    sound.play()
    return sound.get_length()
    # pygame.mixer.music.load(f)
    # pygame.mixer.music.play()


  def play_random_papierhier(self):
    f = random.choice(self.papierhier)
    sound = pygame.mixer.Sound(f)
    print('playing:', f, ' with length: ',     sound.get_length())

    sound.play()
    return sound.get_length()
    # pygame.mixer.music.load(f)
    # pygame.mixer.music.play()

