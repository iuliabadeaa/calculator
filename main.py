from tkinter import *
window = Tk()
window.title("CALCULATOR")
window.geometry("500x500")
window.resizable(True, True)

lbl1=Label(window,text="operand 1:")
lbl1.place(x=15,y=200)
operand1=Entry(window)
operand1.place(x=100,y=200)

lbl2=Label(window,text="operand 2:")
lbl2.place(x=215,y=200)
operand2=Entry(window)
operand2.place(x=300, y=200)

def addop():
    op1=int(operand1.get())
    op2=int(operand2.get())
    sum_=int(op1+op2)
    print(sum_)

def subop():
    op1=int(operand1.get())
    op2=int(operand2.get())
    sub_=int(op1-op2)
    print(sub_)

def multiplyop():
    op1=int(operand1.get())
    op2=int(operand2.get())
    multiply_=int(op1*op2)
    print(multiply_)

def divop():
    op1=float(operand1.get())
    op2=float(operand2.get())
    div=float(op1/op2)
    print(div)

sugestive_label=Label(window,text="choose an operation:")
sugestive_label.place(x=30,y=225)

add=Button(window, text="+",command=addop)
add.place(x=20,y=250)
sub=Button(window, text="-",command=subop)
sub.place(x=50,y=250)
multiply=Button(window, text="*",command=multiplyop)
multiply.place(x=80,y=250)
divide=Button(window, text="/",command=divop)
divide.place(x=110,y=250)

window.mainloop()