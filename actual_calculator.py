import tkinter
import tkinter.font as font
from tkinter import *

root=tkinter.Tk()
root.title("CALCULATOR")
root.geometry("525x450")

exp=""

def press(val):
    global exp
    exp=exp+val
    answer.set(exp)
    
def clear():
    global exp
    answer.set("")
    exp=""

def equal():
    total=eval(exp)
    answer.set(total)



answer=StringVar()
result=Entry(root, text=answer,font=("Arial Narrow", 20, "bold"),justify="right")
result.grid(row=0, column=0, columnspan=4, ipadx=120, ipady=35)
fon=font.Font(family="Helvetica", size=14, weight="bold")
btn7=Button(root, text="7", font=fon, command=lambda:press("7"))
btn7.grid(row=1, column=0, ipadx=38, ipady=13)

btn8=Button(root, text="8", font=fon, command=lambda:press("8"))
btn8.grid(row=1, column=1, ipadx=38, ipady=13)

btn9=Button(root, text="9", font=fon, command=lambda:press("9"))
btn9.grid(row=1, column=2, ipadx=38, ipady=13)

btnpls=Button(root, text="+", font=fon,command=lambda:press("+"))
btnpls.grid(row=1, column=3, ipadx=38, ipady=13)




btn4=Button(root, text="4", font=fon, command=lambda:press("4"))
btn4.grid(row=2, column=0, ipadx=38, ipady=13)

btn5=Button(root, text="5", font=fon, command=lambda:press("5"))
btn5.grid(row=2, column=1, ipadx=38, ipady=13)

btn6=Button(root, text="6", font=fon, command=lambda:press("6"))
btn6.grid(row=2, column=2, ipadx=38, ipady=13)

btnminus=Button(root, text="-", font=fon,command=lambda:press("-"))
btnminus.grid(row=2, column=3, ipadx=38, ipady=13)




btn1=Button(root, text="1", font=fon, command=lambda:press("1"))
btn1.grid(row=3, column=0, ipadx=38, ipady=13)

btn2=Button(root, text="2", font=fon, command=lambda:press("2"))
btn2.grid(row=3, column=1, ipadx=38, ipady=13)

btn3=Button(root, text="3", font=fon, command=lambda:press("3"))
btn3.grid(row=3, column=2, ipadx=38, ipady=13)

btnmul=Button(root, text="X", font=fon,command=lambda:press("*"))
btnmul.grid(row=3, column=3, ipadx=38, ipady=13)





btn0=Button(root, text="0", font=fon, command=lambda:press("0"))
btn0.grid(row=4, column=0, ipadx=38, ipady=13)

btndot=Button(root, text=".", font=fon, command=lambda:press("."))
btndot.grid(row=4, column=1, ipadx=38, ipady=13)

btnequal=Button(root,text= "=",font=fon, command=equal)
btnequal.grid(row=4, column=2, ipadx=38,ipady=13)

btndiv=Button(root, text="/", font=fon,command=lambda:press("/"))
btndiv.grid(row=4, column=3, ipadx=38, ipady=13)

btnclear=Button(root, text="clear", font=fon, command=clear)
btnclear.grid(row=5, column=0, columnspan=4, ipadx=237,ipady=10)