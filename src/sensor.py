
import board
import busio

import adafruit_vl53l0x
import adafruit_vl6180x

class Distance:

  def __init__(self, sensor):

    # Initialize I2C bus and sensor.
    self.i2c = busio.I2C(board.SCL, board.SDA)
    if sensor == 'vl53':
      self.sensor = adafruit_vl53l0x.VL53L0X(self.i2c)

    elif sensor == 'vl61':
      self.sensor = adafruit_vl6180x.VL6180X(self.i2c)


    if self.sensor:

      # set timing budget in milliseconds
      self.sensor.measurement_timing_budget = 20000


  def get(self):
    return self.sensor.range
