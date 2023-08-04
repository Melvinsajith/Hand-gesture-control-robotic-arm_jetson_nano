import tkinter as tk
import time
from adafruit_servokit import ServoKit
Kit = ServoKit(channels=16)

#change number of the Kit.servo[##].angele = int(180) to change servo number 
for i in range(5):
    Kit.servo[3].angle = int(0)
    time.sleep(1)
    Kit.servo[3].angle = int(40)