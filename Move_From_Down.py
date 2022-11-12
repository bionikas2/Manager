from tkinter import *
from tkinter import filedialog
from tkinter.font import BOLD
import os
from pathlib import Path


class Mover(Frame):

    path_to_folder = ""

    def __init__(self, master, win):

        self.window = win

        super().__init__(master)

        self.label = Label(
            self,
            text="Choose where to want to move\n the files from download folder:",
            font=("Comic Sans", 15),
        )
        self.label.place(x=275, y=50, anchor="center")

        self.btn = Button(
            self,
            text="Select",
            font=("Comic Sans", 20),
            fg="blue",
            bg="white",
            command=self.return_path,
        )
        self.btn.place(x=275, y=125, anchor="center")

    def return_path(self):

        self.cleanUp()

        self.path_to_folder = filedialog.askdirectory()
        if self.path_to_folder != "":
            self.result = Label(
                self,
                text=self.shorterString(self.path_to_folder),
                font=("Comic Sans", 15, BOLD),
            )
            self.result.place(x=275, y=225, anchor="center")

            self.confirm()

    def shorterString(self, string):
        if len(string) > 40:
            return "..." + string[-40:]
        else:
            return string

    def cleanUp(self):

        if self.path_to_folder != "":
            try:
                self.result.destroy()
            except:
                pass
            try:
                self.btnConfirm.destroy()
            except:
                pass
            try:
                self.path_to_folder = ""
            except:
                pass
            try:
                self.done.destroy()
            except:
                pass

    def confirm(self):
        self.btnConfirm = Button(
            self,
            fg="blue",
            bg="white",
            text="Confirm",
            font=("Comic Sans", 20),
            command=self.display_done,
        )
        self.btnConfirm.place(x=215, y=275)

    def display_done(self):
        d = f"{Path.home()}/Downloads"
        self.moving(self.path_to_folder, d)

        self.done = Label(self, text="Done!", font=("Comic Sans", 40))
        self.done.place(x=200, y=350)

    def moving(self, directory, downs):
        for x in os.listdir(downs):
            file = downs + "/" + x
            if os.path.isfile(file):
                Path(file).rename(directory + "/" + x)
            elif os.path.isdir(file):
                if len(os.listdir(file)) == 0:
                    Path(file).rename(directory + "/" + x)
                else:
                    self.moving(directory, file + "/")
                    Path(file).rename(directory + "/" + x)
