import json
import requests
import time
import pyupm_grove as grove
import pyupm_i2clcd as lcd


button = grove.GroveButton(3)
myLcd = lcd.Jhd1313m1(0,0x3E,0x62)

myLcd.setCursor(0,0)
myLcd.setColor(120,39,249)

url = "http://10.43.51.167:5000/sections/1"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

i = 0
while 1:
	if(button.value() != 0):
		myLcd.clear()
		myLcd.setCursor(0,0)
		myLcd.write('Lugares ocupados')
		i += 1
		myLcd.setCursor(1,2)
		myLcd.write(str(i))
		time.sleep(0.5)
		data = json.dumps({"space":i}) 
		r = requests.post(url, data,headers=headers)
