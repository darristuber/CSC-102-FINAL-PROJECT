import RPi.GPIO as GPIO
import time
import requests
import gpiozero
from pygame import mixer
from filestack import Client
from picamera import PiCamera

camera = PiCamera()
client = Client("AYFpxOiBuT76o5iAxOA7az")
mixer.init()
global new_filelink

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN)  # Read output from PIR motion sensor
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # button
GPIO.setup(6, GPIO.OUT)  # LED output pin
sound = mixer.Sound('doorbell-1.wav')


def sendPicture():
    camera.capture("image.jpg")
    new_filelink = client.upload(filepath="image.jpg")
    print(new_filelink.url)


def ring():
    sound.play()
    print("Ding dong!")
    camera.capture("image.jpg")
    new_filelink = client.upload(filepath="image.jpg")
    r = requests.post('https://maker.ifttt.com/trigger/trigger/json/with/key/cQ5sQUR5HKWjtu1OnNQ0_L',
                      json={'value1': new_filelink.url})


def motionDetected():
    camera.capture("image.jpg")
    new_filelink = client.upload(filepath="image.jpg")
    r = requests.post('https://maker.ifttt.com/trigger/trigger/json/with/key/cQ5sQUR5HKWjtu1OnNQ0_L',
                      json={'value1': new_filelink.url})


while True:
    b = GPIO.input(18)
    i = GPIO.input(22)
    if b == True:
        time.sleep(0.1)
        sendPicture()
        ring()
        time.sleep(5)
    if i == 0:  # When output from motion sensor is LOW
        print("No intruders", i)
        GPIO.output(6, 0)  # Turn OFF LED
        time.sleep(0.1)

    elif i == 1:  # When output from motion sensor is HIGH
        print("Intruder detected", i)
        GPIO.output(6, 1)  # Turn ON LED
        motionDetected()
        time.sleep(5)