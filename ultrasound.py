from gpiozero import DistanceSensor
from gpiozero import Device
from gpiozero.pins.lgpio import LGPIOFactory
from time import sleep

# Force to use lgpio backend (for Raspberry Pi 5)
Device.pin_factory = LGPIOFactory()

sensor = DistanceSensor(echo=27, trigger=17)

while True:
    print('Distance: ', sensor.distance * 100, 'cm')
    sleep(1)
