from audio import RidderAudio
import time
import board

from sensor import Distance
from leds import Leds

print('start')

sensor = Distance('vl61')

leds = Leds(pin=board.D18, num_leds=4)

leds.red()


audio = RidderAudio('../audio/')

audio.play_random_thankyou()

print('got distance:', sensor.get())

time.sleep(8)

audio.play_random_intermezzo()

time.sleep(8)