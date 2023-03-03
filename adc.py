import wiringpi as wp
import time, os, sys
import spidev
from ch7_ClassLCD import LCD

def ActivateADC ():
    wp.digitalWrite(pin_CS_adc, 0)       # Actived ADC using CS
    time.sleep(0.000005)

def DeactivateADC():
    wp.digitalWrite(pin_CS_adc, 1)       # Deactived ADC using CS
    time.sleep(0.000005)

def ActivateLCD():
    wp.digitalWrite(pin_CS_lcd, 0)       # Actived LCD using CS
    time.sleep(0.000005)

def DeactivateLCD():
    wp.digitalWrite(pin_CS_lcd, 1)       # Deactived LCD using CS
    time.sleep(0.000005)

PIN_OUT = {  
    'SCLK'  :   14,
    'DIN'   :   12,
    'DC'    :   8, 
    'CS'    :   15, #We will not connect this pin! --> we use w13
    'RST'   :   9,
    'LED'   :   7, #backlight   
}

def readadc(adcnum): 
    if ((adcnum > 7) or (adcnum < 0)): 
        return -1 
    revlen, recvData = wp.wiringPiSPIDataRW(0, bytes([1,(8+adcnum)<<4,0]))
    time.sleep(0.000005)
    adcout = ((recvData[1]&3) << 8) + recvData[2] 
    
    return adcout  

#Setup
pin_CS_adc = 0
wp.wiringPiSetup() 
wp.pinMode(pin_CS_adc, 1)                 # Set ce to mode 1 ( OUTPUT )
wp.wiringPiSPISetupMode(0, 400000, 0)  #(channel, speed, mode)

pin_CS_lcd = 1
wp.pinMode(pin_CS_lcd , 1)            # Set pin to mode 1 ( OUTPUT )
ActivateLCD()
lcd_1 = LCD(PIN_OUT)

#Main
lcd_1.clear()
lcd_1.set_backlight(1)
try:
    while True:
        ActivateADC()
        res = readadc(0) # read channel 0
        DeactivateADC()
        print ("ADC input:",res)
        ActivateLCD()
        lcd_1.clear()
        lcd_1.go_to_xy(0, 0)
        lcd_1.put_string('Value:' + str(res))
        lcd_1.refresh()
        DeactivateLCD()
        time.sleep(0.2)
except KeyboardInterrupt:
    DeactivateADC()
    lcd_1.clear()
    lcd_1.refresh()
    lcd_1.set_backlight(0)
    DeactivateLCD()
    print("\nProgram terminated")