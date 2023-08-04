import tkinter as tk
import time
from adafruit_servokit import ServoKit
Kit = ServoKit(channels=16)
i = 0
while i <7:

    Kit.servo[0].angle = int(130)

    Kit.servo[1].angle = int(180)
    
    Kit.servo[2].angle = int(100)

    Kit.servo[3].angle = int(0)

    time.sleep(1)

    Kit.servo[3].angle = int(42) 

    time.sleep(1)

    Kit.servo[0].angle = int(130)

    Kit.servo[1].angle = int(150)
    
    Kit.servo[2].angle = int(150)
    
    time.sleep(0.5)

    Kit.servo[0].angle = int(15)

    time.sleep(1)

    Kit.servo[1].angle = int(180)

    time.sleep(1)

    Kit.servo[3].angle = int(0)

    time.sleep(1)

    Kit.servo[0].angle = int(130)

    Kit.servo[2].angle = int(100)

    time.sleep(1)


    i = i+1
