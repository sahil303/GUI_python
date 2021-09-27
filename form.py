import tkinter
from tkinter import *
from tkinter.ttk import Combobox
root = tkinter.Tk()
root.geometry('900x800+0+0')
root.title("FACE RECOGNITION")

# label
l1 = Label(root, text = "Student Attentiveness",font = ("Times","28","bold"))
l1.pack()

#Name
n = Label(root, text = "Enter Name :",font = ("Times","15","bold"))
n.place(x = 0, y= 100)
name = Entry(width = 100)
name.place(x = 125, y= 105)
# Age
a = Label(root, text = "Enter Age :",font = ("Times","15","bold"))
a.place(x = 0, y= 200)
age = Entry(width = 10)
age.place(x = 105, y= 205)

#Gender
l3 = Label(root, text = "Gender :",font = ("Times","15","bold"))
l3.place(x = 0, y = 300)
g1 = Radiobutton(root, text ="Male",font = ("Times","12"),value = 1)
g1.place(x = 90, y = 302)
g2 = Radiobutton(root, text ="Female",font = ("Times","12"), value = 2)
g2.place(x = 170, y = 302)
g2 = Radiobutton(root, text ="Others",font = ("Times","12"), value = 3)
g2.place(x = 265, y = 302)

#ComboBox
l4 = Label(root, text = "Qualification :",font = ("Times","15","bold"))
l4.place(x = 0, y = 400)
data = ('10th','12th', 'Graduate', 'PG','PHD')
cd = Combobox(root, values = data)
cd.place(x=135, y=403)

# Buttons
b1 = Button(root, text = "SUBMIT", bg = "#0000ff", fg ="#00ff00", width = 10 , height = 1)
b1.place(x =300, y = 500)
b2 = Button(root, text = "CANCEL", bg = "#aaaaff", fg ="#000000", width = 10 , height = 1)
b2.place(x =400, y = 500)

# b3 = Button(root, text = "", bg = "#ffffff", fg ="#222299", width = 10 , height = 1,command = buttonclick)
# b3.pack()
# 
# b4 = Button(root, text = "HIT", bg = "#000000", fg ="#ffffff", width = 10 , height = 1, activebackground = "Orange", activeforeground = "White")
# b4.place(x = 50, y = 250)
# 
# # LEFT RIGHT BOTTOM TOP
# bb = Button(root, text = "BOTTOM", bg = "#0000ff", fg ="#00ff00", width = 10 , height = 1)
# bb.pack(side = BOTTOM)
# 
# bl = Button(root, text = "LEFT", bg = "#aaaaff", fg ="#000000", width = 10 , height = 1)
# bl.pack(side = LEFT)
# 
# br = Button(root, text = "RIGHT", bg = "#ffffff", fg ="#222299", width = 10 , height = 1)
# br.pack(side = RIGHT)

root.mainloop()
