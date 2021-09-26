import tkinter
from tkinter import *

# title of the app
root = tkinter.Tk()
root.geometry('800x800')
root.title("Calculator")

# Label of the app
label1 = Label(root, text = "Simple Calculator Program", font = ("Times", "20", "bold"))
label1.place(x = 225, y = 100)

# Label of first number
label2 = Label(root, text = "Enter first number :", font = ("Times", "17", "bold"))
label2.place(x = 50, y = 200)

# Taking input of first number
e1 = Entry(root)
e1.place(x = 260, y =206)

# Label of first number
label3 = Label(root, text = "Enter second number :", font = ("Times", "17", "bold"))
label3.place(x = 50, y = 260)

# Taking input of second number
e2 = Entry(root)
e2.place(x = 290, y =267)