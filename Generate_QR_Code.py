import pyqrcode
from tkinter import *
import os
def create():
    s = entvar.get()
    url = pyqrcode.create(s)
    url.svg("myqr.svg", scale = 8)
    url.png("myqr.png", scale = 6)
    os.system("myqr.png")

root = Tk()
canvas = Canvas(root, width = 50, height = 50)
l = Label(root, text='QR Code String').grid(row = 0, padx = 20)
global entvar
entvar = StringVar()
e = Entry(root, textvariable= entvar).grid(row = 1, padx  = 10, pady = 10)
b = Button(root, text='Create QR', command = create).grid(row = 2)
mainloop()