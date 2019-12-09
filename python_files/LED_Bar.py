import RPi.GPIO as GPIO
import time

ledPins = [17,18,27,22,23,24,25,2,3,8]

def setup():
    print("Program is starting......")
    GPIO.setmode(GPIO.BCM)
    for pin in ledPins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        
def destroy():
    for pin in ledPins:
        GPIO.output(pin, GPIO.HIGH)
    GPIO.cleanup()
    
def loop():
    while True:
        for pin in ledPins:
            GPIO.output(pin, GPIO.LOW)
            time.sleep(.1)
            GPIO.output(pin, GPIO.HIGH)
            
        for pin in ledPins[::-1]:
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(pin, GPIO.HIGH)
        
        
if __name__ == '__main__':
    setup()
    try:
        loop()
    
    except KeyboardInterrupt: #checks for cntrl + C
        destroy()
    
    
    
    