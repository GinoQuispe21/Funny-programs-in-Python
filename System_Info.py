import subprocess
from tkinter import *
s = subprocess.check_output('systeminfo',shell=True)
cmout = s.decode('utf-8')
print(type(cmout))
root = Tk()
root.title('System Info')
L = Label(root, text = 'System Info')
L.pack()
T = Text(root, height=200, width=100)
T.insert(INSERT, cmout)
T.pack()
mainlopp()