from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep, strftime
from datetime import datetime



def get_time_now():
    return datetime.now().strftime('   %H:%M:%S')
    

def get_cpu_temp():
    tmp = open('/sys/class/thermal/thermal_zone0/temp')
    cpu = tmp.read()
    tmp.close()
    return '{:.2f}'.format( float(cpu)/1000 ) + ' C'    

def loop():
    mcp.output(3,1) # turn on LCD backlight
    lcd.begin(16,2) # set number of LCD lines and columns
    while(True):
        lcd.clear()
        lcd.setCursor(0,0) # set cursor position
        
        lcd.message('CPU: ' + get_cpu_temp()+'\n')  #display CP temp
        lcd.message( get_time_now()) #display current time
        
        sleep(.5)
    
def destroy():
    lcd.clear()
    
PCF8574_address = 0x27
PCF8574A_address = 0x3F #I2C address of the chips

#Create GPIO adapter
try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    try:
        mcp = PCF8574_GPIO(PCF8574A_address)
    except:
        print('  I2C error')
        exit(1)
        
# Create LCD

lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        destroy()