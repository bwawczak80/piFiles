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
    
def turnOff(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    
    
def loop():
    
    
    r = 0
    g = 100
    b = 100

    
    while g > 0:
        
        g = g-5
        r = r+5
        setColor(r,g,b) #set color
        print ('r=%d, g=%d, b=%d '%(r,g,b))
        time.sleep(.1)
    
    time.sleep(1)
    setColor(100,100,100)
    time.sleep(1)
    setColor(100,0,100)
    time.sleep(1)
    setColor(100,100,100)
    time.sleep(1)
    
    
    
    
    while r > 0:
        
        r = r-5
        g = g+5
        setColor(r,g,b) #set color
        print ('r=%d, g=%d, b=%d '%(r,g,b))
        time.sleep(.1)


    time.sleep(1)
    setColor(100,100,100)
    time.sleep(1)
    setColor(0,100,100)
    time.sleep(1)
    setColor(100,100,100)
    time.sleep(1)
              
    while r < 100:
        
        r = r+5
        b = b-5
        setColor(r,g,b) #set color
        print ('r=%d, g=%d, b=%d '%(r,g,b))
        time.sleep(.1)
        
    time.sleep(1)
    setColor(100,100,100)
    time.sleep(1)
    setColor(100,100,0)
    time.sleep(1)
    setColor(100,100,100)
    time.sleep(1)
        
def destroy():
    p_R.stop()
    p_G.stop()
    p_B.stop()
    GPIO.cleanup()
    
if __name__ == '__main__': #start here
    setup()
    try:
        loop()
        
    except KeyboardInterrupt: #cntrl +C
        destroy()
        
    
