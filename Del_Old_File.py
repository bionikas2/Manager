import os
import datetime
from datetime import datetime
from datetime import timedelta
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.font import BOLD
import platform


class Deleter(Frame):

    option_List = [
        "1 Week",
        "2 Weeks",
        "1 Month",
        "3 Months",
        "6 Months",
        "1 Year",
        "Everything",
    ]

    files = []

    path_to_folder = ""

    def __init__(self, master, win):

        self.window = win

        super().__init__(master)

        self.lbl = Label(
            self,
            text="Select time frame and directory you want to clean:",
            font=("Comic Sans", 15),
        )
        self.lbl.place(x=275, y=50, anchor="center")

        self.btn = Button(
            self,
            fg="blue",
            bg="white",
            text="Select",
            font=("Comic Sans", 20),
            command=self.return_path,
        )
        self.btn.place(x=350, y=100)

        style = ttk.Style()
        style.map("TCombobox", fieldbackground=[("readonly", "white")])

        self.time_Select = ttk.Combobox(
            self, values=self.option_List, font=("Comic Sans", 15), state="readonly"
        )
        self.time_Select.pack(padx=5, pady=5)
        self.time_Select.set("Everything")
        self.time_Select.place(x=50, y=110)

    def return_date(self):
        time_ = self.time_Select.get()
        if time_ == "1 Week":
            return datetime.now() - timedelta(days=7)
        elif time_ == "2 Weeks":
            return datetime.now() - timedelta(days=14)
        elif time_ == "1 Month":
            return datetime.now() - timedelta(weeks=4)
        elif time_ == "3 Months":
            return datetime.now() - timedelta(weeks=12)
        elif time_ == "6 Months":
            return datetime.now() - timedelta(weeks=24)
        elif time_ == "1 Year":
            return datetime.now() - timedelta(days=365)
        else:
            return datetime.now()

    def return_path(self):
        self.cleanUp()
        self.path_to_folder = filedialog.askdirectory()
        if self.path_to_folder != "":
            self.result = Label(
                self,
                text=self.shorterString(self.path_to_folder),
                font=("Comic Sans", 15, BOLD),
            )
            self.result.place(x=275, y=200, anchor="center")
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
            command=self.display_dir,
        )
        self.btnConfirm.place(x=200, y=250)

    def display_dir(self):
        self.deleting(self.path_to_folder)

        self.done = Label(self, text="Done!", font=("Comic Sans", 40))
        self.done.place(x=180, y=350)

    def deleting(self, directory):
        for x in os.listdir(directory):
            file_ = directory + "/" + x
            if datetime.fromtimestamp(
                os.stat(file_).st_mtime
            ) < self.return_date() and os.path.isfile(file_):
                self.files.append(x)
                os.remove(file_)
            elif os.path.isdir(file_):
                if len(os.listdir(file_)) == 0:
                    os.rmdir(file_)
                else:
                    if platform.system() == "Windows":
                        self.deleting(file_ + "\\")
                    else:
                        self.deleting(file_ + "/")
                    os.rmdir(file_)
        if directory == self.path_to_folder:
            self.writingFile(directory + "/")

    def writingFile(self, directory):
        if "Deleted Files.txt" in os.listdir(directory):
            os.remove(directory + "/" + "Deleted Files.txt")
            text_File = open(directory + "Deleted Files.txt", "w+")
        else:
            text_File = open(directory + "Deleted Files.txt", "w+")
        text_File.close()

        text_File = open(directory + "Deleted Files.txt", "a+")
        text_File.write(directory + " Deleted Files: \n")
        for x in self.files:
            if x != "Deleted Files.txt":
                text_File.write(x + "\n")

        text_File.close()
