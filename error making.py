# This program allows you to make error windows
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

master = Tk()
master.geometry("300x200+10+20")
master.title("Main Menu")

v1 = IntVar()
v2 = IntVar()

def makeWindow():
    def finish():
        makeWindow.destroy()
    
    selection1=("Error", "Warning", "Info")
    makeWindow = Toplevel(master)
    makeWindow.title("Make")
    makeWindow.geometry("500x300+10+20")
    
    lbl=Label(makeWindow, text="Make your Error:", font=("Arial", 16))
    lbl.place(x=15, y=10)    
    
    btn = Button(makeWindow, text ="Done.", command = finish)
    btn.place(x=400, y=255)
    
    lbl=Label(makeWindow, text="Error Title:", font=("Arial", 11))
    lbl.place(x=55, y=50)
    txtfld=Entry(makeWindow, text="")
    txtfld.place(x=30, y=70)
    
    lbl=Label(makeWindow, text="Error Text:", font=("Arial", 11))
    lbl.place(x=210, y=50)
    txtfld=Entry(makeWindow, text="")
    txtfld.place(x=180, y=70)
    
    lbl=Label(makeWindow, text="Error type:", font=("Arial", 11))
    lbl.place(x=65, y=100)
    cb1 = Combobox(makeWindow, values=selection1)
    cb1.place(x=30, y=120)


def openWindow():
    newWindow = Toplevel(master)
    newWindow.title("Open")
    newWindow.geometry("300x200+10+20")

def deleteWindow():
    newWindow = Toplevel(master)
    newWindow.title("Delete")
    newWindow.geometry("300x200+10+20")
    
def closeWindow():
    master.destroy()

lbl=Label(master, text="Choose an option:", font=("Arial", 16))
lbl.place(x=20, y=20)

btn = Button(master, text ="Make", command = makeWindow)
btn.place(x=20, y=60)

btn = Button(master, text ="Open", command = openWindow)
btn.place(x=20, y=90)

btn = Button(master, text ="Delete", command = deleteWindow)
btn.place(x=20, y=120)

btn = Button(master, text ="Quit", command = closeWindow)
btn.place(x=20, y=170)

mainloop()