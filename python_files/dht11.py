#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import DHT_Lib as DHT

DHTPin = 35 # define pin

def loop():
    dht = DHT.DHT(DHTPin)
    sumCnt = 0
    while(True):
        sumCnt += 1
        chk = dht.readDHT11()
        print("The sumCnt is : %d, \t chk : %d"%(sumCnt,chk))
        if( chk is dht.DHTLIB_OK):
            print("DHT11, OK!!!")
        elif(chk is dht.DHTLIB_ERROR_CHECKSUM):
            print("DHTLIB_ERROR_CHECKSUM")
        elif(chk is dht.DHTLIB_ERROR_TIMEOUT):
            print("DHTLIB__ERROR_TIMEOUT")
        else:
            print("Other Error")
            
        print("Humidity : %.2f, \t Temperature : %.2f \n"%(dht.humidity,dht.temperature))
        
        time.sleep(5)
        
if __name__ == '__main__':
    try:
        loop()
        
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()

#TODO if timeout, else display on LCD