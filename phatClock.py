#!/usr/bin/env python

import time
import signal

import scrollphathd
from scrollphathd.fonts import font5x7

print("""
Scroll pHAT HD: sternClock

Displays hours and minutes in text;
Press Ctrl+C to exit.

""")

# Brightness of the seconds bar and text
BRIGHTNESS = 0.15
time0="x"
time1="y"

# Uncomment the below if your display is upside down
#   (e.g. if you're using it in a Pimoroni Scroll Bot)
scrollphathd.rotate(degrees=180)

def numName(num):
    if num == 1:
        return "one"
    elif num == 2:
        return "two"
    elif num == 3:
        return "three"
    elif num == 4:
        return "four"
    elif num == 5:
        return "five"
    elif num == 6:
        return "six"
    elif num == 7:
        return "seven"
    elif num == 8:
        return "eight"
    elif num == 9:
        return "nine"
    elif num == 10:
        return "ten"
    elif num == 11:
        return "eleven"
    elif num == 12:
        return "twelve"
    elif num == 13:
        return "thirteen"
    elif num == 14:
        return "fourteen"
    elif num == 15:
        return "fifteen"
    elif num == 16:
        return "sixteen"
    elif num == 17:
        return "seventeen"
    elif num == 18:
        return "eighteen"
    elif num == 19:
        return "nineteen"
    elif num == 20:
        return "twenty"
    elif num == 30:
        return "thirty"
    elif num == 40:
        return "forty"
    elif num == 50:
        return "fifty"
    elif num > 20 and num < 30:
        return "twenty-"+numName(num-20)
    elif num > 30 and num < 40:
        return "thirty-"+numName(num-30)
    elif num > 40 and num < 50:
        return "forty-"+numName(num-40)
    elif num > 50 and num < 60:
        return "fifty-"+numName(num-50)
    
def paddedTime():
        hourS = time.strftime("%H")
        hour = int(float(hourS))
        minuteS = time.strftime("%M")
        minute = int(float(minuteS))
                
        if minute == 15:
            return "A quarter after "+numName(hour % 12)+"   "
        elif minute == 30:
            return "Half past "+numName(hour % 12)+"   "
        elif minute == 45:
            return "A quarter to "+numName((hour+1) % 12)+"   "
        elif hour == 0 and minute == 0:
            return "Midnight"+"   "
        elif hour == 12 and minute == 0:
            return "Noon"+"   "
        elif minute == 0:
            return numName(hour % 12)+" o'clock"+"   "
        elif minute < 10:
            return numName(hour % 12)+" o-"+numName(minute)+"   "
        else:
            return numName(hour % 12)+" "+numName(minute)+"   "

while True:
    time1=time.strftime("%H:%M")
    if time1 != time0:
        time0=time1
        scrollphathd.clear()
        scrollphathd.write_string(paddedTime(), font=font5x7, brightness=BRIGHTNESS)
    # Show the buffer
    scrollphathd.show()
    # Scroll the buffer content
    scrollphathd.scroll()
    # Wait for 0.1s
    time.sleep(0.1)