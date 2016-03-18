#!/usr/bin/python
import socket
import fcntl
import struct
import time
import mraa
import requests
import json

import pyupm_i2clcd as lcd

#PIN numbers
BUTTON_GPIO = 6   
TOUCH_GPIO = 8 
LED = 13   

#Initialize Gpio objects
button = mraa.Gpio(BUTTON_GPIO)  
touch = mraa.Gpio(TOUCH_GPIO)
led = mraa.Gpio(LED)

# LCD Screen configuration
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
myLcd.clear()
myLcd.setColor(90, 90, 255)
myLcd.setCursor(0,0)

#Direccion of digital signals
button.dir(mraa.DIR_IN)  
touch.dir(mraa.DIR_IN)  
led.dir(mraa.DIR_OUT)
    
#Variables config
led.write(0)
messages = " "
touchState = False
buttonState = False
lastButtonState = False
lastTouchState = False


r = requests.get("http://10.43.51.167:5000/sections/P_Entrance")
content = json.loads(r.text)
lugares = content['capacity']
MAX = content['max']

urlReserve = "http://10.43.51.167:5000/sections/P_Entrance/reserve/1"
urlFree = "http://10.43.51.167:5000/sections/P_Entrance/free/1"

while True:

    #------- Button and Touch control
    buttonState = button.read() == 1;
    touchState = touch.read() == 1;

    if(lastButtonState != buttonState):
        if(buttonState):
            r = requests.get(urlReserve)
            print r.text
            content = json.loads(r.text)
            lugares = content['capacity']



    if(lastTouchState != touchState):
        if(touchState):
            r = requests.get(urlFree)
            print r.text
            content = json.loads(r.text)
            lugares = content['capacity']



    lastTouchState = touchState
    lastButtonState = buttonState


    # ------ LCD -------
        #Red = 252, 18, 33
        #Amarillo = 229, 220, 22
        #Verde = 46, 254, 67

    percentage = (lugares/(MAX*1.0)) 
    green = int(255.0 * percentage)
    red = int(255.0 * (1 - percentage) )

    myLcd.setColor(red, green, 0)

    messages = "Disponibles: " + str(lugares) + " "
    myLcd.setCursor(0,3)
    myLcd.write("P_Entrance")
    myLcd.setCursor(1,0)
    myLcd.write(messages)


    # Wait
    time.sleep(0.05)
