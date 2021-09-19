import tkinter
from tkinter import *

root = tkinter.Tk();

# title
root.title("My First Window")

# Initializing the size
root.geometry("800x1000")

# labelling
label1 = Label(root, text = "First Page")
label1.pack()

# Buttons
b1 = Button(root, text = "Click Me")
b1.place(x = 50, y = 100)

b2 = Button(root, text = "Save Me")
b2.place(x = 50, y = 150)

b3 = Button(root, text = "Delete")
b3.place(x = 50, y = 200)

b4 = Button(root, text = "HIT", bg = "#ff0000")
b4.place(x = 50, y = 250)

