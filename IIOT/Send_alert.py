import RPi.GPIO as GPIO
import time
import yagmail

sensor_pin=18

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

pwd='ggdr toxp rwoe ehvi'

yag=yagmail.SMTP('jayeshkadam021@gmail.com',pwd)

while 1:
    if GPIO.input(sensor_pin)==1:
        yag.send(to='kadamjayesh021@gmail.com', sunject='Motion Detected', contents='Attention!!! motion detected in your environment')
        print('motion detected')

    time.sleep(2)    
