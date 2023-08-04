import tkinter as tk
import time
from adafruit_servokit import ServoKit
Kit = ServoKit(channels=16)



def button1_click():
    
    Kit.servo[1].angle = int(100)
    Kit.servo[2].angle = int(180)
    

def button2_click():
    Kit.servo[1].angle = int(180)
    Kit.servo[2].angle = int(120)

def button3_click():
    Kit.servo[1].angle = int(100)
    Kit.servo[2].angle = int(130)

def button4_click():
    Kit.servo[0].angle = int(0)


def button5_click():
    Kit.servo[0].angle = int(100)


def button6_click():
    Kit.servo[0].angle = int(180)


def button7_click():
    Kit.servo[3].angle = int(0)


def button8_click():
    Kit.servo[3].angle = int(42)


# Create the main window
window = tk.Tk()
window.title("Button Functions")

# Create buttons
button1 = tk.Button(window, text="Button 1", command=button1_click)
button1.pack()

button2 = tk.Button(window, text="Button 2", command=button2_click)
button2.pack()

button3 = tk.Button(window, text="Button 3", command=button3_click)
button3.pack()

button4 = tk.Button(window, text="Button 4", command=button4_click)
button4.pack()

button5 = tk.Button(window, text="Button 5", command=button5_click)
button5.pack()

button6 = tk.Button(window, text="Button 6", command=button6_click)
button6.pack()

button7 = tk.Button(window, text="Button 7", command=button7_click)
button7.pack()

button8 = tk.Button(window, text="Button 8", command=button8_click)
button8.pack()

# Run the main event loop
window.mainloop()
