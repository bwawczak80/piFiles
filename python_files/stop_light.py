import RPi.GPIO as GPIO
import time

ledRedPin = 17 # GPIO pin number
ledYellowPin = 4
ledGreenPin = 19

secondRed = 23
secondYellow = 25
secondGreen = 16



def setup():
    GPIO.setmode(GPIO.BCM)  # Numbers for GPIO location
    
    GPIO.setup(ledRedPin, GPIO.OUT) #Set ledPin's mode to output
    GPIO.output(ledRedPin, GPIO.LOW) # Set to LOW to turn off = false
    
    GPIO.setup(ledYellowPin, GPIO.OUT) 
    GPIO.output(ledYellowPin, GPIO.LOW)
    
    GPIO.setup(ledGreenPin, GPIO.OUT) 
    GPIO.output(ledGreenPin, GPIO.LOW)
    
    GPIO.setup(secondRed, GPIO.OUT) 
    GPIO.output(secondRed, GPIO.LOW)
    
    GPIO.setup(secondYellow, GPIO.OUT) 
    GPIO.output(secondYellow, GPIO.LOW)
    
    GPIO.setup(secondGreen, GPIO.OUT) 
    GPIO.output(secondGreen, GPIO.LOW)
    
    
def loop():
    while True:
        GPIO.output(ledRedPin, GPIO.HIGH) # led on
        GPIO.output(ledYellowPin, GPIO.LOW)
        GPIO.output(ledGreenPin, GPIO.LOW)
        time.sleep(12) 
        
        GPIO.output(ledRedPin, GPIO.LOW) # led off
        GPIO.output(ledYellowPin, GPIO.LOW)
        GPIO.output(ledGreenPin, GPIO.HIGH)
        time.sleep(9) 
        
        GPIO.output(ledRedPin, GPIO.LOW) 
        GPIO.output(ledYellowPin, GPIO.HIGH)
        GPIO.output(ledGreenPin, GPIO.LOW)
        time.sleep(3)
        
        GPIO.output(secondRed, GPIO.HIGH) # led on
        GPIO.output(secondYellow, GPIO.LOW)
        GPIO.output(secondGreen, GPIO.LOW)
        time.sleep(12) 
        
        #GPIO.output(secondGreen, GPIO.LOW) # led off
        #GPIO.output(secondYellow, GPIO.LOW)
        #GPIO.output(secondRed, GPIO.HIGH)
        #time.sleep(27) 
        
        #GPIO.output(secondGreen, GPIO.LOW) 
        #GPIO.output(secondYellow, GPIO.HIGH)
        #GPIO.output(secondRed, GPIO.LOW)
        #time.sleep(3) 
        
        

def destroy():
    GPIO.output(ledRedPin,GPIO.LOW)
    GPIO.output(ledYellowPin,GPIO.LOW)
    GPIO.output(ledGreenPin,GPIO.LOW)
    
    GPIO.output(secondGreen,GPIO.LOW)
    GPIO.output(secondYellow,GPIO.LOW)
    GPIO.output(secondGreen,GPIO.LOW)
    GPIO.cleanup()  #release resources
    
    
if __name__ == '__main__': #Program Start
    setup()
    try:
        loop()
        
        
    except KeyboardInterrupt: # checks for cntrl+ C
        destroy()