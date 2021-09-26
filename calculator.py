import tkinter
from tkinter import *

class calc:
# Functions
    def sum(self):
        self.a = e1.get()
        self.b = e2.get()
        print("value of a is: ",self.a)
        print("value of b is: ",self.b)
        addition = int(self.a) + int(self.b)
        print("Addition of two numbers is : ",addition)
        result = "Addition of two number is : "+str(addition)
        e3.delete(0,'end')
        e3.insert(END,result)

    def subtract(self):
        self.a = e1.get()
        self.b = e2.get()
        print("value of a is: ",self.a)
        print("value of b is: ",self.b)
        subtraction = int(self.a) - int(self.b)
        print("Subtraction of two numbers is : ",subtraction)
        result = "Subtraction of two number is : "+str(subtraction)
        e3.delete(0,'end')
        e3.insert(END,result)
        
    def multi(self):
        self.a = e1.get()
        self.b = e2.get()
        print("value of a is: ",self.a)
        print("value of b is: ",self.b)
        multiplication = int(self.a) * int(self.b)
        print("multiplication of two numbers is : ",multiplication)
        result = "multiplication of two number is : "+str(multiplication)
        e3.delete(0,'end')
        e3.insert(END,result)
        
    def divide(self):
        self.a = e1.get()
        self.b = e2.get()
        print("value of a is: ",self.a)
        print("value of b is: ",self.b)
        division = int(self.a) / int(self.b)
        print("division of two numbers is : ",division)
        result = "division of two number is : "+str(division)
        e3.delete(0,'end')
        e3.insert(END,result)

c = calc()
# title of the app
root = tkinter.Tk()
root.geometry('800x700+0+0')
root.title("Calculator")

# Label of the app
label1 = Label(root, text = "Simple Calculator Program", font = ("Times", "20", "bold"))
label1.place(x = 225, y = 50)

# Label of first number
label2 = Label(root, text = "Enter first number :", font = ("Times", "17", "bold"))
label2.place(x = 50, y = 200)

# Taking input of first number
e1 = Entry(root)
e1.place(x = 290, y =206)

# Label of first number
label3 = Label(root, text = "Enter second number :", font = ("Times", "17", "bold"))
label3.place(x = 50, y = 260)

# Taking input of second number
e2 = Entry(root)
e2.place(x = 290, y =267)

# Add Button
add = Button(root, text = "ADD", font = ("Times", "17", "bold"),command = c.sum)
add.place(x = 50 , y = 350)

# Subtract Button
sub = Button(root, text = "SUBTRACTION", font = ("Times", "17", "bold"), command = c.subtract)
sub.place(x = 140 , y = 350)


# Multiply Button
mul = Button(root, text = "MULTIPLICATION", font = ("Times", "17", "bold"),command = c.multi)
mul.place(x = 350 , y = 350)

# Division Button
div = Button(root, text = "DIVISION", font = ("Times", "17", "bold"),command = c.divide)
div.place(x = 600 , y = 350)

# Output
e3 = Entry(root,bd= 15, width =90, font = ("Times", 11, "bold"))
e3.place(x = 0, y =500)