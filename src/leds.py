import board
import neopixel
import random

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

class Leds:

  def __init__(self, pin, num_leds: int):
    self.pixels = neopixel.NeoPixel(pin, num_leds, brightness=1.0,
                                    auto_write=False, pixel_order=ORDER)

    self.num_pixels = num_leds
    self.lastBrightness = 0


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

  def blink(self):

    if self.pixels.brightness:
      self.lastBrightness = self.pixels.brightness
      self.pixels.brightness = 0
    else:
      self.pixels.brightness = self.pixels.lastBrightness
    self.pixels.show()
