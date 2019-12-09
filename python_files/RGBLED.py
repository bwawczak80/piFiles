import RPi.GPIO as GPIO
import time
import random

pins = {'pin_R':17, 'pin_G':18, 'pin_B':27}

def setup():
    global p_R,p_G,p_B
    GPIO.setmode(GPIO.BCM) # Numbers for GPIO location
    for i in pins:
        GPIO.setup(pins[i], GPIO.OUT)
        GPIO.output(pins[i], GPIO.HIGH)
        
    p_R = GPIO.PWM(pins['pin_R'], 2000)
    p_G = GPIO.PWM(pins['pin_G'], 2000)
    p_B = GPIO.PWM(pins['pin_B'], 2000)
    
    p_R.start(0)
    p_G.start(0)
    p_B.start(0)
    
def setColor(r_val,g_val,b_val):
    p_R.ChangeDutyCycle(r_val) #Change the duty cycle
    p_G.ChangeDutyCycle(g_val) #Change the duty cycle
    p_B.ChangeDutyCycle(b_val) #Change the duty cycle
    
def loop():
    while True:
      
        r=random.randint(0,100) #get a random number 0-100
        g=random.randint(0,100) #get a random number 0-100
        b=random.randint(0,100) #get a random number 0-100
        setColor(r,g,b) #set color
        print ('r=%d, g=%d, b=%d '%(r,g,b))
        time.sleep(3)
        
def destroy():
    P_R.stop()
    p_G.stop()
    p_B.stop()
    GPIO.cleanup()
    
if __name__ == '__main__': #start here
    setup()
    try:
        loop()
        
    except KeyboardInterrupt: #cntrl +C
        destroy()
        
    