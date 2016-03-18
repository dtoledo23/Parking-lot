import time
import pyupm_servo as servo

servo1 = servo.ES08A(3)
servo1.setAngle(0)

while True:
	servo1.setAngle(90)
	time.sleep(2)
	servo1.setAngle(0)
	time.sleep(10)

