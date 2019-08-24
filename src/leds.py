import board
import neopixel
import random
from collections import namedtuple

RGB = namedtuple('rgb', ['r', 'g', 'b'])

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

class WavAnimation:

    def __init__(self, data, duration, color=None):
        self.duration = duration
        self.data = data
        self.fs = len(self.data) / self.duration
        if color:
          self.color = color
        else:
          self.color = RGB(
                  int(random.uniform(0, 255)),
                  int(random.uniform(0, 255)),
                  int(random.uniform(0, 255)))

    def calcColor(self, t):
        i = int(self.fs * t)
        f = self.data[i] / 255

        return RGB(
                int(self.color.r * f),
                int(self.color.g * f),
                int(self.color.b * f))

class Leds:

  def __init__(self, pin, num_leds: int):
    self.pixels = neopixel.NeoPixel(pin, num_leds, brightness=1.0,
                                    auto_write=False, pixel_order=ORDER)

    self.num_pixels = num_leds

  def applyAnimation(self, animation, t):
    newColor = animation.calcColor(t)
    self.pixels.fill((newColor.r, newColor.g, newColor.b))
    self.pixels.show()


  def off(self):
    self.pixels.fill((0,0,0))
    self.pixels.show()

  def red(self):
    self.pixels.fill((255, 0, 0))
    self.pixels.show()

  def green(self):
    self.pixels.fill((0, 255, 0))
    self.pixels.show()

  def blue(self):
    self.pixels.fill((0, 0, 255))
    self.pixels.show()

  def randomColor(self):
    r = random.choice([self.red, self.green, self.blue])
    r()