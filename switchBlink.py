from enum import Enum
import time
import wiringpi as wp

DEFAULT_PERIOD = 0.0015
DEFAULT_REPS = -1  # infinite repetitions

class Mode(Enum):
    WAVE = 1
    FULL = 2 # DEFAULT

class Dir(Enum): # Direction
    LEFT = 1 # DEFAULT
    RIGHT = 2

def drive(_pinList, _mode = Mode.FULL, _direction = Dir.LEFT, _period = DEFAULT_PERIOD, _repetitions = DEFAULT_REPS):
    pinList = _pinList.copy()
    pinList.reverse() if _direction == Dir.LEFT else None
    r = 0
    while r < _repetitions if _repetitions != -1 else True:
        r = r + 1
        pinListTmp = pinList
        if _mode == Mode.FULL:
            pinListTmp = list(zip(pinList, pinList[1:] + pinList[:1]))
        for p in pinListTmp:
            p2 = None
            if type(p) is tuple:
                (p1,p2) = p
            else:
                p1 = p
            wp.digitalWrite(p1, 1)
            wp.digitalWrite(p2, 1) if p2 else None
            time.sleep(_period)
            wp.digitalWrite(p1, 0)
            wp.digitalWrite(p2, 0) if p2 else None

wp.wiringPiSetup()
pinList = [21, 22, 23, 24]
pinSwitch = 25
for p in pinList:
    wp.pinMode(p, 1)
wp.pinMode(pinSwitch, 0)

# WAVE mode, 10 ms
drive(pinList, Mode.WAVE, Dir.LEFT, 10.0 / 1000.0, 100)
# WAVE mode, 1000 ms
drive(pinList, Mode.WAVE, Dir.RIGHT, 1000.0 / 1000.0, 5)
# FULL mode, 10 ms
drive(pinList, Mode.WAVE, Dir.RIGHT, 10.0 / 1000.0, 100)
# FULL mode, 1000 ms
drive(pinList, Mode.FULL, Dir.LEFT, 1000.0 / 1000.0, 5)

while True:
    drive(pinList, Mode.FULL, Dir.LEFT if wp.digitalRead(pinSwitch) == 0 else Dir.RIGHT , 0.002, 4)