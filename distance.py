import sys, os, time
import wiringpi as wp

wp.wiringPiSetup()

PIN_TRIG = 21
PIN_ECHO = 22
wp.pinMode(PIN_TRIG, 1)
wp.pinMode(PIN_ECHO, 0)
#wp.wiringPiISR(22, wp.GPIO.INT_EDGE_BOTH, echo)

print("Starting...")
while True:
  wp.digitalWrite(PIN_TRIG, 1)
  time.sleep(0.00001)
  wp.digitalWrite(PIN_TRIG, 0)

  while not wp.digitalRead(PIN_ECHO):
    time.sleep(0.0000001)
  TIME = time.time()
  while wp.digitalRead(PIN_ECHO):
    time.sleep(0.0000001)
  distance = 17000 * (time.time() - TIME)
  print("Distance:" + str(int(distance)) + " cm")
  time.sleep(0.2)