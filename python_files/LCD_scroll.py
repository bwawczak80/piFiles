from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep, strftime
from datetime import datetime

def loop():
    mcp.output(3,1) # turn on LCD backlight
    lcd.begin(16,2) # set number of LCD lines and columns
 
    while(True):

        lcd.setCursor(0, 0) # set cursor position
        lcd.message("This is my message.  It finally scrolls")
        lcd.DisplayLeft()
        lcd.clear
        
        
def destroy():
    lcd.clear()
    
PCF8574_address = 0x27
PCF8574A_address = 0x3F #I2C address of the chips

try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    try:
        mcp = PCF8574_GPIO(PCF8574A_address)
    except:
        print('  I2C error')
        exit(1)
        
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        destroy()