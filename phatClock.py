#!/usr/bin/env python

import time
import signal
import scrollphathd
import argparse
from scrollphathd.fonts import font5x7

print("""
Scroll pHAT HD: sternClock

Displays hours and minutes in text;
Press Ctrl+C to exit.

""")

parser = argparse.ArgumentParser(description='textclock code.')
parser.add_argument('-dt' ,'-delay_text', help="text delay time", default=0.025)
parser.add_argument('-dm' ,'-delay_message', help="message delay time", default=0.2)
parser.add_argument('-b' ,'-brightness', help="brightness", default=0.15)


args = parser.parse_args()


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
    elif num == 0:
        return "twelve"
    elif num > 20 and num < 30:
        return "twenty-"+numName(num-20)
    elif num > 30 and num < 40:
        return "thirty-"+numName(num-30)
    elif num > 40 and num < 50:
        return "forty-"+numName(num-40)
    elif num > 50 and num < 60:
        return "fifty-"+numName(num-50)
    
def paddedTime():
        timeNow = time.localtime()
        hour = timeNow.tm_hour
        minute = timeNow.tm_min
                      
        if minute == 15:
            ans = "A quarter after "+numName(hour % 12)
        elif minute == 30:
            ans = "Half past "+numName(hour % 12)
        elif minute == 45:
            ans = "A quarter to "+numName((hour+1) % 12)
        elif hour == 0 and minute == 0:
            ans = "Midnight"
        elif hour == 12 and minute == 0:
            ans = "Noon"
        elif minute == 0:
            ans = numName(hour % 12)+" o'clock"
        elif minute < 10:
            ans = numName(hour % 12)+" o-"+numName(minute)
        else:
            ans = numName(hour % 12)+" "+numName(minute)
        return "    " + ans

def run():
	scrollphathd.clear()
	scrollphathd.show()

	while True:
       		textWidth=scrollphathd.write_string(paddedTime(), x=0, y=0, font=font5x7, brightness=float(args.b))
		scrollphathd.show()

		for deltaX in range(textWidth):
    	   		scrollphathd.scroll(x=1)
	   		scrollphathd.show()
    	   		time.sleep(float(args.dt))
		scrollphathd.clear()
		scrollphathd.show()
		time.sleep(float(args.dm))

# Main function
if __name__ == "__main__":
    run_text = run()
    if (not run_text.process()):
        run_text.print_help()