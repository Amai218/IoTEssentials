import wiringpi as wp
import time
from enum import Enum

class Lit(Enum):
    OFF = 0
    ON = 1

wp.wiringPiSetup()
ldrSwitchPins = [21, 26]
for s in ldrSwitchPins:
    wp.pinMode(s, 0)
ledPins = [22, 23, 24, 25]
for l in ledPins:
    wp.pinMode(l, 1)

mappingArray = [[Lit.ON, Lit.OFF], [Lit.OFF, Lit.ON]]

def checkAndShow():
    if mappingArray[wp.digitalRead(ldrSwitchPins[0])][wp.digitalRead(ldrSwitchPins[1])] == Lit.ON:
        print("light on")
        for l in ledPins:
            wp.digitalWrite(l, 1)
    else:
        print("light off")
        for l in ledPins:
            wp.digitalWrite(l, 0)

while True:
    checkAndShow()
    time.sleep(0.5)