from tkinter import *
from tkinter import ttk

root = Tk() #Create Window

frm = ttk.Frame(root, padding=10) #Create Frame
frm.grid()
root.geometry('300x300+100+100')

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

root.mainloop() #Start Program