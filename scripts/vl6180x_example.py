# Simple demo of the VL6180X distance sensor.
# Will print the sensed range/distance every second.
import time

import board
import busio

import adafruit_vl6180x

# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
vl61 = adafruit_vl6180x.VL6180X(i2c)

# Optionally adjust the measurement timing budget to change speed and accuracy.
vl61.measurement_timing_budget = 10000

# Main loop will read the range and print it every second.
while True:
    try:
        r = vl61.range
        if r:
            print('Range: {0}mm'.format(r))
    except:
        print('fail, retry..')
    time.sleep(1.0)
