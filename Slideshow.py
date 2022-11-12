from tkinter import *
from tkinter import filedialog
from tkinter.font import BOLD
import os
from PIL import Image
from PIL import ImageTk, Image


class Slideshow(Frame):

    path_to_folder = ""

    images = []

    count = 0

    def __init__(self, master, win):
        self.window = win

        super().__init__(master)

        self.laber = Label(
            self,
            text="Enter a folder from which \n you want to view pictures from:",
            font=("Comic Sans", 15),
        ).place(x=275, y=50, anchor="center")

        self.button = Button(
            self,
            text="Select",
            font=("Comic Sans", 20),
            fg="blue",
            bg="white",
            command=self.return_path,
        ).place(x=100, y=125, anchor="center")

    def return_path(self):

        self.cleanUp()

        self.path_to_folder = filedialog.askdirectory()

        self.result = Label(
            self,
            text=self.shorterString(self.path_to_folder),
            font=("Comic Sans", 14, BOLD),
        )
        self.result.place(x=500, y=125, anchor="e")

        self.gettingImages(self.path_to_folder)

    def shorterString(self, string):
        if len(string) > 28:
            return "..." + string[-28:]
        else:
            return string

    def cleanUp(self):

        if self.path_to_folder != "":
            try:
                self.disp_img.destroy()
            except:
                pass
            try:
                self.btn_next.destroy()
                self.btn_previous.destroy()
            except:
                pass
            try:
                self.path_to_folder = ""
            except:
                pass
            try:
                self.result.destroy()
            except:
                pass

    def gettingImages(self, directory):
        self.images.clear()
        try:
            for x in os.listdir(directory):
                try:
                    im = Image.open(directory + "/" + x)
                    self.images.append(x)
                except IOError:
                    pass
            self.displayImages(self.images, directory + "/")
        except:
            print("No Directory!")

    def displayImages(self, images, directory):

        self.disp_img = Label(self)
        self.disp_img.pack(pady=20)
        self.disp_img.place(x=275, y=260, anchor="center")
        try:
            image = Image.open(directory + images[self.count])
        except:
            print("No images!")
            return

        aspect_ratio = image.width / image.height
        resized_img = image.resize((int(200 * aspect_ratio), 200), Image.ANTIALIAS)

        img = ImageTk.PhotoImage(resized_img)
        self.disp_img.config(image=img)
        self.disp_img.image = img

        if len(self.images) > 1:
            self.btn_previous = Button(
                self,
                text="Previous",
                font=("Comic Sans", 15),
                fg="blue",
                bg="white",
                command=self.previous_image,
            )
            self.btn_previous.place(x=20, y=400)

            self.btn_next = Button(
                self,
                text="Next",
                font=("Comic Sans", 15),
                fg="blue",
                bg="white",
                command=self.next_image,
            )
            self.btn_next.place(x=450, y=400)

    def previous_image(self):
        self.disp_img.destroy()
        self.count -= 1
        self.displayImages(self.images, self.path_to_folder + "/")

    def next_image(self):
        self.disp_img.destroy()
        self.count += 1

        self.btn_next.destroy()
        self.btn_previous.destroy()

        if self.count == len(self.images):
            self.count = 0
        self.displayImages(self.images, self.path_to_folder + "/")
