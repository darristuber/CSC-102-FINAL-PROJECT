from gpiozero import MotionSensor
import picamera 
from signal import pause
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

pir = MotionSensor(4)
camera = picamera.PiCamera()
'''camera.start_preview()'''

n = 0

'''def stop_camera():
    camera.stop_preview()
    exit()'''
    
def take_photo():
    global n
    #print(i)
    camera.capture('/home/pi/Desktop/image.%s.jpg' % n)
    n+=1
    print(n)
    print('a photo has been taken')
    time.sleep(1)

while True:
    i = GPIO.input(4)
    if i == 0:  # When output from motion sensor is LOW
        print("No intruders", i) 
        time.sleep(1)

    elif i == 1:  # When output from motion sensor is HIGH
        print("Intruder detected", i)
        take_photo()
        print('take_photo complete')
        time.sleep(1)


pir.when_motion = take_photo

pause()
