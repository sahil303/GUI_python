import tkinter
from tkinter import *
from tkinter import messagebox
root = tkinter.Tk();

# Functions
def buttonclick():
    messagebox.showinfo("Alert", "This is testing command window.\n Good Evening")
# title
root.title("My First Window")

# Initializing the size
root.geometry("800x1000+100+0")

# labelling
label1 = Label(root, text = "First Page")
label1.pack()

# Buttons
b1 = Button(root, text = "Click Me", bg = "#0000ff", fg ="#00ff00", width = 10 , height = 1)
b1.place(x = 50, y = 100)

b2 = Button(root, text = "Save Me", bg = "#aaaaff", fg ="#000000", width = 10 , height = 1)
b2.place(x = 50, y = 150)

b3 = Button(root, text = "Delete", bg = "#ffffff", fg ="#222299", width = 10 , height = 1)
b3.place(x = 50, y = 200)

b4 = Button(root, text = "HIT", bg = "#000000", fg ="#ffffff", width = 10 , height = 1,command = buttonclick)
b4.place(x = 50, y = 250)

