from tkinter import *
root = Tk()
root.title("CALCULATOR")
root.geometry("310x420")
root.resizable(True, True) 


def button_click(symbol):
    current=entry_operands.get()
    entry_operands.delete(0,END)
    entry_operands.insert(0,str(current)+str(symbol))

def button_clearf():
    entry_operands.delete(0,END)

def button_addf():
    first_op=entry_operands.get()
    global f_num 
    global math 
    math = "add"
    f_num = float(first_op)
    entry_operands.delete(0,END)

def button_substrf():
    first_op=entry_operands.get()
    global f_num 
    global math 
    math="sub"
    f_num = float(first_op)
    entry_operands.delete(0,END)

def button_multiplyf():
    first_op=entry_operands.get()
    global f_num 
    global math
    math="mul"
    f_num = float(first_op)
    entry_operands.delete(0,END)

def button_dividef():
    first_op=entry_operands.get()
    global f_num 
    global math
    math="div"
    f_num = float(first_op)
    entry_operands.delete(0,END)

def button_percentagef():
    first_op=entry_operands.get()
    global f_num 
    f_num = float(first_op)
    entry_operands.delete(0,END)
    entry_operands.insert(0,f_num/100)

def button_equalf():
    second_op=entry_operands.get()
    entry_operands.delete(0,END)
    if math == "add":
        entry_operands.insert(0,f_num+float(second_op))
    if math == "sub":
        entry_operands.insert(0,f_num-float(second_op))
    if math == "mul":
        entry_operands.insert(0,f_num*float(second_op))
    if math == "div":
        entry_operands.insert(0,f_num/float(second_op))



entry_operands=Entry(root, width=28, font=('Segoe UI Symbol', 15), bg=("#A0A0A0"), borderwidth=5)
entry_operands.place(x=0,y=0)
button1=Button(root, text=("1"),width=7, font=('Segoe UI Symbol', 15), bg=("#A0A0A0"), borderwidth=5, command= lambda: button_click(1)).place(x=10,y=50)
button2=Button(root, text=("2"),width=7, font=('Segoe UI Symbol', 15), bg=("#A0A0A0"), borderwidth=5, command= lambda: button_click(2)).place(x=110,y=50)
button3=Button(root, text=("3"),width=7, font=('Segoe UI Symbol', 15), bg=("#A0A0A0"), borderwidth=5, command= lambda: button_click(3)).place(x=210,y=50)
button4=Button(root, text=("4"),width=7, font=('Segoe UI Symbol', 15), bg=("#A0A0A0"), borderwidth=5, command= lambda: button_click(4)).place(x=10,y=110)
button5=Button(root, text=("5"),width=7, font=('Segoe UI Symbol', 15), bg=("#A0A0A0"), borderwidth=5, command= lambda: button_click(5)).place(x=110,y=110)
button6=Button(root, text=("6"),width=7, font=('Segoe UI Symbol', 15), bg=("#A0A0A0"), borderwidth=5, command= lambda: button_click(6)).place(x=210,y=110)
button7=Button(root, text=("7"),width=7, font=('Segoe UI Symbol', 15), bg=("#A0A0A0"), borderwidth=5, command= lambda: button_click(7)).place(x=10,y=170)
button8=Button(root, text=("8"),width=7, font=('Segoe UI Symbol', 15), bg=("#A0A0A0"), borderwidth=5, command= lambda: button_click(8)).place(x=110,y=170)
button9=Button(root, text=("9"),width=7, font=('Segoe UI Symbol', 15), bg=("#A0A0A0"), borderwidth=5, command= lambda: button_click(9)).place(x=210,y=170)
button_clear=Button(root,text=("CLEAR"), width=7, font=('Segoe UI Symbol', 15), bg=("#A0A0A0"), borderwidth=5, command=button_clearf).place(x=10,y=230)
button0=Button(root, text=("0"),width=7, font=('Segoe UI Symbol', 15), bg=("#A0A0A0"), borderwidth=5, command= lambda: button_click(0)).place(x=110,y=230)
button_equal=Button(root, text=("="),width=7, font=('Segoe UI Symbol', 15), bg=("#A0A0A0"), borderwidth=5, command=button_equalf).place(x=210,y=230)
button_add=Button(root,text=("+"), width=7, font=('Segoe UI Symbol', 15), bg=("#A0A0A0"), borderwidth=5, command= button_addf).place(x=10,y=290)
button_substr=Button(root, text=("-"),width=7, font=('Segoe UI Symbol', 15), bg=("#A0A0A0"), borderwidth=5, command=button_substrf).place(x=110,y=290)
button_multiply=Button(root, text=("x"),width=7, font=('Segoe UI Symbol', 15), bg=("#A0A0A0"), borderwidth=5, command=button_multiplyf).place(x=210,y=290)
button_divide=Button(root,text=(":"), width=7, font=('Segoe UI Symbol', 15), bg=("#A0A0A0"), borderwidth=5, command=button_dividef).place(x=10,y=350)
button_percentage=Button(root, text=("%"),width=7, font=('Segoe UI Symbol', 15), bg=("#A0A0A0"), borderwidth=5, command=button_percentagef).place(x=110,y=350)
button_point=Button(root, text=("."),width=7, font=('Segoe UI Symbol', 15), bg=("#A0A0A0"), borderwidth=5, command=lambda:button_click('.')).place(x=210,y=350)



root.mainloop()