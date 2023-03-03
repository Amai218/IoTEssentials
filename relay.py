import time
import wiringpi as wp

wp.wiringPiSetup()
relay1 = 21
relay2 = 22
wp.pinMode(relay1, 1)
wp.pinMode(relay2, 1)
switch1 = 25
switch2 = 23
wp.pinMode(switch1, 0)
wp.pinMode(switch2, 0)

switchArray = [[(0,0), (0,1)], [(1,0), (1,1)]]

while True:
    (r1, r2) = switchArray[wp.digitalRead(switch1)][wp.digitalRead(switch2)]
    wp.digitalWrite(relay1, r1)
    wp.digitalWrite(relay2, r2)
    time.sleep(0.1)