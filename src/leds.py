import board
import neopixel

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

class Leds:

  def __init__(self, pin, num_leds: int):
    self.pixels = neopixel.NeoPixel(pin, num_leds, brightness=1.0,
                                    auto_write=False, pixel_order=ORDER)

    self.num_pixels = num_leds


  def red(self):
    pixels.fill((255, 0, 0))
    pixels.show()