
# If you don't have the module Wikipedia, write this in your terminal:
# pip install wikipedia

import wikipedia
import tkinter as tk

global result

def search():
    root = tk.Tk()
    L = tk.Label(root, text = entlvar.get())
    L.pack()
    T  = tk.Text(root, height = 10, width = 52)
    T.pack()
    result = wikipedia.summary(entlvar.get(), sentences = 2)
    T.insert(tk.END,  result)

root = tk.Tk()
L = tk.Label(root, text = 'Query').grid(row = 0)
entlvar = tk.StringVar()
enl = tk.Entry(root,  textvariable = entlvar)
enl.grid(row = 0, column = 1)

tk.Button(root, text = 'Quit', command = root.quit).grid(row = 3, column = 0, sticky = tk.W, pady = 4)
tk.Button(root, text = 'Search', command =  search).grid(row = 3, column = 1, sticky = tk.W, pady = 4)

tk.mainloop()