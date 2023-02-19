from machine import Pin, PWM
from time import sleep
import utime
from webservo import Servo
global portion
portion = 1 



s1 = Servo(0)       # Servo pin is connected to GP0
 
def servo_Map(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
 
def servo_Angle(angle):
    if angle < 0:
        angle = 0
    if angle > 180:
        angle = 180
    s1.goto(round(servo_Map(angle,0,180,0,1024))) # Convert range value to angle value

def FeedCat(portion):
     #portion is an interger passed in, determines how many times loop is ran 
    increment = 0

    # the function range() has thre parameters  range(start position, end position, step).
    while increment < portion:
        print("Open ...")
        for i in range(-250,250,100):
            servo_Angle(i)
            utime.sleep(0.05)
            
        print("Close ...")
        for i in range(250,-250,-100):
            servo_Angle(i)
            utime.sleep(0.05)
        print("Served portion" + str(increment) )
        
        increment = increment + 1 #when increment == to portion, while loop ends

