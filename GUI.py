import tkinter
from tkinter import *
from tkinter.ttk import Combobox

window = tkinter.Tk()
window.geometry("800x800")

#Label
lab1 = Label(window, text = "MY FIRST GUI")
lab1.pack()

# CheckBox
check1 = Checkbutton(window, text = "Python Programming")
check1.place(x = 400, y = 100)
check2 = Checkbutton(window, text = "JAVA Programming")
check2.place(x = 400, y = 125)

# Radio Button
rbutton1 = Radiobutton(window, text = "Male", value = 1)
rbutton1.place(x=400, y=300)
rbutton2 = Radiobutton(window, text = "Female", value = 2)
rbutton2.place(x=400, y=350)
rbutton3 = Radiobutton(window, text = "Transgender", value = 3)
rbutton3.place(x=400, y=400)

data = ('biscuit','soap', 'shampoo', 'choclates','icecream')
cd = Combobox(window, values = data)
cd.place(x=400, y=450)