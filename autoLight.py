import wiringpi as wp
import time

wp.wiringPiSetup()
wp.pinMode(21, 0)
ledPins = [22, 23, 24, 25]
for l in ledPins:
  wp.pinMode(l, 1)

def checkAndShow():
  if wp.digitalRead(21) == 0:
    print("light off")
    for l in ledPins:
      wp.digitalWrite(l, 0)
  else:
    print("light on")
    for l in ledPins:
      wp.digitalWrite(l, 1)

while True:
  checkAndShow()
  time.sleep(0.5)

