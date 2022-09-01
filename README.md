# FerrmRidder

## Requirements

* Raspberry Pi 3 with Raspbian
* VL53L0X distance sensor
* Neopixel LED strip (WS2813)
* USB Audio output device (e.g. usb -> 3.5inch audio converter)
* Raspberry Pi breakout board with connectors for sensors (See Breakout directory)

## Installation Instructions

Download New Raspbian headless image and flash sd card

On a Mac:

```
diskutil unmountdisk /dev/disk2
sudo dd bs=2m if=2019-07-10-raspbian-buster-lite.img of=/dev/rdisk2
```

Boot raspberry pi and configure wifi and enable ssh and I2C

```
sudo raspi-config
```

Updates

```
sudo apt update && sudo apt upgrade
```

Install pip for python3
```
sudo apt-get install python3-pip
```


Install python dependencies, neopixel modules etc

```
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel pygame libsdl-mixer1.2
sudo pip3 install adafruit-circuitpython-vl53l0x
sudo pip3 install adafruit-circuitpython-vl6180x
```

Then we'll follow [this Stackexchange](https://raspberrypi.stackexchange.com/questions/80072/how-can-i-use-an-external-usb-sound-card-and-set-it-as-default) answer to enable USB audio.


## send audio to pi

```
tar -czvf audio.tar.gz audio
scp audio.tar.gz pi@ip:~
```

