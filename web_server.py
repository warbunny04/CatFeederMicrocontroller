import network
import socket
from time import sleep
#from picozero import pico_temp_sensor, pico_led
import machine
from machine import Pin

ssid = "Mystery phone" #this will depend on the wifi you're connecting to 
password = "iminclass" #this will depend on the wifi you're connecting to 

led = Pin(25,Pin.OUT)


def connect():
    #connect to WLAN (wireless network/wifi)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while wlan.isconnected() == False: #will loop until the connection is established and 
        print('Waiting for connection...') #handshake between pi pico and connection is established
        led.toggle()
        sleep(1)
        print(wlan.ifconfig())
        
led.value(1) #led remains on after connected

try:
    connect()
except KeyboardInterrupt:
    machine.reset()
        

