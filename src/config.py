## Config: These definitions are used by ridder.py

from leds import RGB

NumLEDs = 8
#SensorType = 'vl61' # 'vl53'
SensorType = 'vl53'
AudioDir = '/home/pi/FerrmRidder/audio'
PapierHierInterval_s = 60
DetectThreshold_mm = 200

FadeColor = RGB(r=0, g=20, b=60)
FadeDuration_s  = 3
