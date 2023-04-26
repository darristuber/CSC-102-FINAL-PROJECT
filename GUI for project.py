'''from tkinter import *
from os import *
pictures = []
path = '/user/CSC 102/pictures'
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        pictures.append(file)
        #yield file
print(pictures)


class App(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        #imput images
        #choose from variety of images? 
        self.img = PhotoImage(file = "earthpicture Small.png")
        self.image = Label(width=300, image=self.img)
        self.image.pack(side=LEFT, fill=Y)
        self.image.grid(row = 0, rowspan = 3, column = 0)
            
        checkbutton1 = Checkbutton(window)
        checkbutton2 = Checkbutton(window)
        checkbutton3 = Checkbutton(window)

        checkbutton1.grid(row = 0, column = 1)
        checkbutton2.grid(row = 1, column = 1)
        checkbutton3.grid(row = 2, column = 1)
        
        label1 = Label(window, text='Name', bg='#E200E6')
        label2 = Label(window, text='Password', bg='#E200E6')

        label1.grid(row=0, column=3, sticky = E, padx = 25, pady = 25)
        label2.grid(row=1, column=3, sticky = E, padx = 25, pady = 25)

        System_On = Button(window, text='System On', command=None)
        #login button will take up 2 columns and be in the center of both
        loginBtn.grid(row=0, column = 3)
        System_Off = Button(window, text='System Off', command=None)
        #login button will take up 2 columns and be in the center of both
        loginBtn.grid(row=1, column = 3)

        emailBox.grid(row=0, column=4, columnspan = 2, sticky = W)
        pwBox.grid(row=1, column=4, columnspan = 2, sticky = W)

        loginBtn = Button(window, text='Previous Image', command=None)
        #login button will take up 2 columns and be in the center of both
        loginBtn.grid(row=3, column = 0)
        
        loginBtn = Button(window, text='Next Image', command=None)
        #login button will take up 2 columns and be in the center of both
        loginBtn.grid(row=3, column = 1)
        
        #loginBtn2 = Button(window, text='Wide Button', command=None)
        #login button will take up 2 columns and be in the center of both
        #loginBtn2.grid(row=3, rowspan = 2, column = 2, columnspan=2)

        label3 = Label(window, text='LABEL 3', bg='#E200E6')
        label3.grid(row=2, rowspan = 2, column=3, columnspan = 2)

window = Tk()
window.title("Security System")

app = App(window)
window.mainloop()'''
  
#        self.image_filenames = ['Kitchen Small.png', 'bathroom Small.png', 'Garage Small.png', 'Kids bedroom Small.png', 'Master Bedroom Small.png', 'Outside Small.png']
import tkinter as tk
from tkinter import PhotoImage

class ImageCycleApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Cycle App")

        # Define image filenames
        self.image_filenames = ['Kitchen Small.png', 'bathroom Small.png', 'Garage Small.png', 'Kids bedroom Small.png', 'Master Bedroom Small.png', 'Outside Small.png']

        self.current_image_index = 0

        # Load first image
        self.load_image()

        # Create image label
        self.image_label = tk.Label(master, image=self.current_image)
        self.image_label.pack()

        # Create "Next" button
        self.next_button = tk.Button(master, text="Next", command=self.next_image)
        self.next_button.pack()

    def load_image(self):
        # Load image from file
        self.current_image = PhotoImage(file=self.image_filenames[self.current_image_index])

    def next_image(self):
        # Increment current image index and wrap around if necessary
        self.current_image_index = (self.current_image_index + 1) % len(self.image_filenames)
        # Load new image
        self.load_image()
        # Update image label
        self.image_label.configure(image=self.current_image)

# Create main window
root = tk.Tk()
# Create app instance
app = ImageCycleApp(root)
# Start main event loop
root.mainloop()
