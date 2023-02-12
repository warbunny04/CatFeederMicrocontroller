from machine import Pin
from mfrc522 import MFRC522
import utime
       
reader = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)
 
red = Pin(0, Pin.OUT)
green = Pin(1, Pin.OUT)
blue = Pin(2, Pin.OUT)


ServoOpenPos  = 2000000 #open position servo 
ServoClosePos = 1000000 #close position servo

 
print("Bring RFID TAG Closer...")
print("")
 
 
while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            
        #the card ID we have is 1976624164
        #the tag ID we have is 3643136261
            
            if card == 3643136261:
                print("Card ID: "+ str(card)+" PASS: Geen light/Servo open")
                #put servo code here 
                
                
                
                
                
                
    #for additional cards:            
           # elif card == 1976624164:
           #     print("Card ID: "+ str(card)+" PASS: BLUE Light Activated")
           #     #servo open, put code here 
                
            else:
                print("Card ID: "+ str(card)+" UNKNOWN CARD! Servo close/Red Light")
                
                #close servo code, RED LED activated 
                
                
                
                
                
                #red.value(1)		this is code for RGB but we are doing LED 
                #green.value(0)
                #blue.value(0) 
