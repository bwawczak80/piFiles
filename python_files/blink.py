import RPi.GPIO as GPIO
import time

ledPin = 17 # GPIO pin number


def setup():
    GPIO.setmode(GPIO.BCM)  # Numbers for GPIO location
    GPIO.setup(ledPin, GPIO.OUT) #Set ledPin's mode to output
    GPIO.output(ledPin, GPIO.LOW) # Set to LOW to turn off = false
    
    
def loop():
    while True:
        GPIO.output(ledPin, GPIO.HIGH) # led on
        time.sleep(1) #sleep for 1 second
        GPIO.output(ledPin, GPIO.LOW) # led off
        time.sleep(1) #sleep for 1 second
        

def destroy():
    GPIO.output(ledPin,GPIO.LOW)
    GPIO.cleanup()  #release resources
    
    
if __name__ == '__main__': #Program Start
    setup()
    try:
        loop()
        
    except KeyboardInterrupt: # checks for cntrl+ C
        destroy()
