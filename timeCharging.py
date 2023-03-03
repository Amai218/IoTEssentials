import wiringpi as wp
import time
import os, sys

wp.wiringPiSetup()

while True:
  wp.pinMode(21, 1)
  wp.digitalWrite(21, 0)

  time.sleep(0.1)

  wp.pinMode(21, 0)
  TIME = time.time()

  while wp.digitalRead(21) == 0:
    time.sleep(0.000001)

  print("Charged in: " + str(int((time.time() - TIME)*1000000)) + " us" )