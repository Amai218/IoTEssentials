import sys, os, time
import wiringpi as wp

wp.wiringPiSetup()

PIN_TRIG = 21
PIN_ECHO = 22
ledMotorPins = [23, 24, 25, 26]
DRIVE_PERIOD = 0.002

wp.pinMode(PIN_TRIG, 1)
wp.pinMode(PIN_ECHO, 0)
for p in ledMotorPins:
    wp.pinMode(p, 1)

def drive(_pinList = ledMotorPins):
    pinList = list(zip(_pinList, _pinList[1:] + _pinList[:1]))
    for p in pinList:
        (p1,p2) = p
        wp.digitalWrite(p1, 1)
        wp.digitalWrite(p2, 1)
        time.sleep(DRIVE_PERIOD)
        wp.digitalWrite(p1, 0)
        wp.digitalWrite(p2, 0)

def ledsOff(_pinList = ledMotorPins):
    for l in _pinList:
        wp.digitalWrite(l, 0)

print("Starting...")
while True:
    wp.digitalWrite(PIN_TRIG, 1)
    time.sleep(0.00001)
    wp.digitalWrite(PIN_TRIG, 0)
    
    WATCHDOG = time.time()
    
    while not wp.digitalRead(PIN_ECHO) and (time.time() - WATCHDOG) < 0.1:
        time.sleep(0.0000001)
    TIME = time.time()
    
    WATCHDOG = time.time()
    
    while wp.digitalRead(PIN_ECHO) and (time.time() - WATCHDOG) < 0.1:
        time.sleep(0.0000001)
    distance = 17000 * (time.time() - TIME)
    if distance > 30.0:
        print("safe:" + str(int(distance)) + " cm")
        ledsOff()
    else:
        print("alarm:" + str(int(distance)) + " cm")
        drive() # also lights up LEDs
    time.sleep(0.01)