from enum import Enum
import time
import wiringpi as wp

PERIOD = 0.0015

class Mode(Enum):
  WAVE = 1
  FULL = 2

def roll(_pinList, _mode, _direction, _repetitions):
  pinList = _pinList.copy()
  pinList.reverse() if _direction == True else None
  for r in range(_repetitions):
    pinListTmp = pinList
    if _mode == Mode.FULL:
      pinListTmp = list(zip(pinList, pinList[1:] + pinList[:1]))
    for p in pinListTmp:
      p1 = None
      p2 = None
      if type(p) is tuple:
        (p1,p2) = p
      else:
        p1 = p
      wp.digitalWrite(p1, 1)
      wp.digitalWrite(p2, 1) if p2 else None
      time.sleep(PERIOD)
      wp.digitalWrite(p1, 0)
      wp.digitalWrite(p2, 0) if p2 else None

wp.wiringPiSetup()
pinList = [21, 22, 23, 24]
for p in pinList:
  wp.pinMode(p, 1)

roll(pinList, Mode.FULL, True, 256)
roll(pinList, Mode.FULL, False, 256)
roll(pinList, Mode.WAVE, True, 256)
roll(pinList, Mode.WAVE, False, 256)

