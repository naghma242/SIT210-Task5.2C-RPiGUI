from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## hardware
red = LED(4)
green = LED(17)
blue = LED(27)

## GUI DEFINITIONS ##
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

###EVENT FUCNTIONS
def redToggle():
    if red.is_lit:
        red.off()
        redButton["text"]=  "Turn RED on"
    else:
        red.on()
        redButton["text"] = "Turn RED off"
        green.off()
        greenButton["text"]=  "Turn GREEN on"
        blue.off()
        blueButton["text"]=  "Turn BLUE on"
        
def greenToggle():
    if green.is_lit:
        green.off()
        greenButton["text"]=  "Turn GREEN on"
    else:
        green.on()
        greenButton["text"] = "Turn GREEN off"
        red.off()
        redButton["text"]=  "Turn RED on"
        blue.off()
        blueButton["text"]=  "Turn BLUE on"
        

def blueToggle():
    if blue.is_lit:
        blue.off()
        blueButton["text"]=  "Turn BLUE on"
    else:
        blue.on()
        blueButton["text"] = "Turn BLUE off"
        red.off()
        redButton["text"]=  "Turn RED on"
        green.off()
        greenButton["text"]=  "Turn GREEN on"
        
def close():
    RPi.GPIO.cleanup()
    win.destroy()

### WIDGETS
redButton = Button(win, text = 'Turn RED On', font = myFont, command = redToggle, bg = 'bisque2', height = 1, width = 35)
redButton.grid(row=0, column=1)

greenButton = Button(win, text = 'Turn GREEN On', font = myFont, command = greenToggle, bg = 'bisque2', height = 1, width = 35)
greenButton.grid(row=1, column=1)

blueButton = Button(win, text = 'Turn BLUE On', font = myFont, command = blueToggle, bg = 'bisque2', height = 1, width = 35)
blueButton.grid(row=2, column=1)

exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'red', height = 1, width = 6)
exitButton.grid(row=3, column=1)
