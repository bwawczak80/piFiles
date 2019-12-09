import RPi.GPIO as GPIO
import keypad as Keypad

ROWS = 4
COLS = 4

keys = [ '1', '2', '3', 'A',
               '4', '5', '6', 'B',
               '7', '8', '9', 'C',
               '*', '0', '#', 'D' ]

rowPins = [12, 16, 18, 22] # change pins to correspond to changes in wires
colsPins = [19, 15, 13, 11]


              
def loop():
    
    keypad1 = Keypad.Keypad(keys,rowPins,colsPins,ROWS,COLS)
    keypad1.setDebounceTime(50)
    while(True):
        key = keypad1.getKey() # keeps looping through until it gets a key
        if(key != keypad1.NULL):
            print ("your pressed key: %c"%(key))
            
if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()