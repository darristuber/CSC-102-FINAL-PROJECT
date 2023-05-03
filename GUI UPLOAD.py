from tkinter import *
import tkinter as tk
from tkinter import PhotoImage

class Pictures:
    def __init__(self, master):
        self.master = master
        master.title("Security System")
        #self.master(row = 2, column = 2)

        self.image_filenames = ['Kitchen  Small.png', 'bathroom Small.png', 'Garage Small.png', 'Kids bedroom Small.png', 'living room pic Small.png', 'Master Bedroom Small.png', 'Outside Small.png']
        self.current_image_index = 0
        self.load_image()
        self.image_label = tk.Label(master, image=self.current_image)
        #self.image_label.pack()
        self.image_label.grid(row = 0, rowspan = 3, column = 0, columnspan = 4)
        
        #self.img = PhotoImage(file = "earthpicture Small.png")
        #self.image = Label(width=300, image=self.img)
        #self.image.pack(side=LEFT, fill=Y)
        #self.image.grid(row = 0, rowspan = 3, column = 0)

        # buttons
        self.next_button = tk.Button(master, text="Next", command=self.next_image)
        #self.next_button.pack()
        self.next_button.grid(row=3, column=2, columnspan = 2, padx = 25, pady = 25)


        
        self.prev_button = tk.Button(master, text="Previous", command=self.prev_image)
        #self.prev_button.pack()
        self.prev_button.grid(row=3, column=0, columnspan = 2, padx = 25, pady = 25)
        
        self.on_button = tk.Button(master, text="Turn System On", command=self.prog_on)
        #self.prev_button.pack()
        self.on_button.grid(row= 0, column=4, sticky = E, padx = 25, pady = 25)
        
        self.off_button = tk.Button(master, text="Turn System Off", command=self.prog_off)
        #self.prev_button.pack()
        self.off_button.grid(row=2, column=4, sticky = E, padx = 25, pady = 25)


    def load_image(self):
        # load all pictures
        self.current_image = PhotoImage(file=self.image_filenames[self.current_image_index])

    def next_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.image_filenames)
        self.load_image()
        self.image_label.configure(image=self.current_image)

    def prev_image(self):
        self.current_image_index = (self.current_image_index - 1) % len(self.image_filenames)
        self.load_image()
        self.image_label.configure(image=self.current_image)
    def prog_on(self):
        pass
    def prog_off(self):
        pass

# Create main window
root = tk.Tk()
# Create app instance
app = Pictures(root)
root.title("Security System: Captured Images")

# Start main event loop
root.mainloop()


