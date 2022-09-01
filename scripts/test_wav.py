#!/usr/bin/env python3
import pygame
import sys
import time

if len(sys.argv) < 2:
    print("supply the path to the wavfile as the first argument")
    exit(1)

wavfile_path = sys.argv[1]


pygame.mixer.init()

print("trying to play ", wavfile_path)
sound = pygame.mixer.Sound(wavfile_path)
duration = sound.get_length()
sound.play()
time.sleep(duration)
print("kthxbye")
