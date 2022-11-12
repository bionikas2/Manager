from tkinter import *
from tkinter import ttk
from Del_Old_File import Deleter
from Move_From_Down import Mover
from Slideshow import Slideshow


class App(Tk):
    def __init__(self, master):

        self.master = master
        self.notebook = ttk.Notebook(self.master, width=550, height=450)

        frame1 = Deleter(self.notebook, master)
        frame2 = Mover(self.notebook, master)
        frame3 = Slideshow(self.notebook, master)

        frame1.pack(padx=5, pady=5)
        frame2.pack(padx=5, pady=5)
        frame3.pack(padx=5, pady=5)

        self.notebook.add(frame1, text="Deleter")
        self.notebook.add(frame2, text="Mover")
        self.notebook.add(frame3, text="Slide Show")

        self.notebook.pack(padx=5, pady=5)


class menuBar(Tk):
    def __init__(self, master=None):

        Frame.__init__(self, master)

        self.master = master
        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu, tearoff=False)
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        infoMenu = Menu(menu, tearoff=False)
        infoMenu.add_command(label="Info", command=self.info)
        menu.add_cascade(label="About", menu=infoMenu)

    def exitProgram(self):
        exit()

    def info(self):
        newWindow = Toplevel(window)

        newWindow.title("Info")

        newWindow.geometry("400x200")

        text = Label(
            newWindow,
            text="""
        First program meant for practicing file manipulation
        and just getting feel for python :)

        First tab deletes files from a specified folder:
        all of them or older then specSSSSified time gap and
        leaves a text file with all the deleted files listed

        Second tab moves files from a downloadsto specified
        folder.

        Third one lets you view pictures from selected folder
    
        """,
            font=("Comic Sans", 10),
            justify=LEFT,
        ).pack()
        text.place(x=0, y=0, anchor="center")


window = Tk()
window.title("Manager")
myMenu = menuBar(window)
myWin = App(window)
window.resizable(False, False)
window.mainloop()
