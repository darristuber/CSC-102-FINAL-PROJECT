import tkinter as tk
from tkinter import PhotoImage
import os

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
camera.resolution = (640, 480)

path = '/home/pi/motion_sensor-master/capturedPictures'

class Pictures():
    def __init__(self, master):
        self.master = master
        self._system = "off"
        master.title("Security System")
        #self.master(row = 2, column = 2)

        self.image_filenames = []
        self.get_pics()
        self.current_image_index = 0
        self.load_image()
        self.image_label = tk.Label(master, image=self.current_image)
        #self.image_label.pack()
        self.image_label.grid(row = 0, rowspan = 3, column = 0, columnspan = 4)
        
        # buttons
        self.next_button = tk.Button(master, text="Next", command=self.next_image)
        #self.next_button.pack()
        self.next_button.grid(row=3, column=2, columnspan = 2, padx = 25, pady = 25)

        self.prev_button = tk.Button(master, text="Previous", command=self.prev_image)
        #self.prev_button.pack()
        self.prev_button.grid(row=3, column=0, columnspan = 2, padx = 25, pady = 25)
        
        self.on_button = tk.Button(master, text="Turn System On", command=self.prog_on)
        #self.prev_button.pack()
        self.on_button.grid(row= 0, column=4, padx = 25, pady = 25)
        
        self.off_button = tk.Button(master, text="Turn System Off", command=self.prog_off)
        #self.prev_button.pack()
        self.off_button.grid(row=2, column=4, padx = 25, pady = 25)


    def get_pics(self):
        self.image_filenames = []
        for filename in os.listdir(path):
            if filename.endswith('.png'):
                self.image_filenames.append(os.path.join(path, filename))
        
    def load_image(self):
        # load all pictures
        self.current_image = None
        if (len(self.image_filenames) > 0):
            self.current_image = PhotoImage(file=self.image_filenames[self.current_image_index])

    def next_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.image_filenames)
        self.load_image()
        self.image_label.configure(image=self.current_image)
        print(len(self.image_filenames))

    def prev_image(self):
        self.current_image_index = (self.current_image_index - 1) % len(self.image_filenames)
        self.load_image()
        self.image_label.configure(image=self.current_image)
    def prog_on(self):
        self._system = 'on'
        self.get_pics()
    def prog_off(self):
        self._system = 'off'
        self.get_pics()

def take_photo():
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)

    #print(i)
    camera.capture('/home/pi/motion_sensor-master/capturedPictures/image.%s.png' % curr_clock)

    print('a photo has been taken')
#     time.sleep(1)
    
def poll():
    if app._system == 'on':
        i = GPIO.input(4)
        if i == 0:  # When output from motion sensor is LOW
            print("No intruders", i) 
            root.config(bg="green")
#             time.sleep(1)

        elif i == 1:  # When output from motion sensor is HIGH
            print("Intruder detected", i)
            root.config(bg="red")
            take_photo()
            print('take_photo complete')
#             time.sleep(1)

    root.after(100, poll)

# Create main window
root = tk.Tk()
# Create app instance
app = Pictures(root)
root.title("Security System: Captured Images")
print ('hi')
# system = 'off'
poll()
root.mainloop()

######MOTION SENSOR MAIN ##########



#while True:

# pir.when_motion = take_photo

# pause()



