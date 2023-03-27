from gpiozero import MotionSensor
import picamera 
from time import sleep
from signal import pause

pir = MotionSensor(4)
camera = picamera.PiCamera()
camera.start_preview()

i = 0

'''def stop_camera():
    camera.stop_preview()
    exit()'''
    
def take_photo():
    global i
    i = i + 1
    camera.capture('/home/pi/Desktop/image.%s.jpg' % i)
    print('a photo has been taken')

pir.when_motion = take_photo

pause()
