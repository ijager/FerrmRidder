from audio import RidderAudio
import time
import board

from queue import queue
from sensor import Distance
from leds import Leds

print('start')

sensor = Distance('vl61')

leds = Leds(pin=boar.D18, num_leds=4)

leds.red()

events = queue()

audio = RidderAudio('../audio/')

audio.play_random_dankjewel()

print('got distance:', sensor.get())

time.sleep(10)

audio.play_random_papierhier()

time.sleep(10)