from tkinter import *
import os
import sys


global result
global enter2
global enter3


window = Tk()
input=Entry(window,fg='black', width=25, bd=15, font=('Helvetica 15'))
input.place(x=40, y=250)
input.focus()


firstnumber=Label(window, text="Type the first number below:", bg='gray', fg='black', font=('Helvetica 12'))
firstnumber.place(x=90, y=220)


def button_command():
    global a
    a = int(input.get())


    input.delete(0, END)
    print(a)

    firstnumber.destroy()
    secondnumber=Label(window, text="Type the second number below:", bg='gray', fg='black', font=('Helvetica 12'))
    secondnumber.place(x=90, y=220)



    enter.destroy()

    enter2 = Button(window, text="Enter", command=button_command2, width=10, height=2, bg='gray', borderwidth=5 )
    enter2.place(x=150, y=315)


    return None




def button_command2():
    global b
    b = int(input.get())
    input.delete(0, END)
    print(b)



    thirdnumber=Label(window, text="Addition (+), Substraction (-), Multiplication (*), or Division (/): ", bg='gray', fg='black', font=('Helvetica 11'))
    thirdnumber.place(x=5, y=220)







    enter3 = Button(window, text="Enter", command=button_command3, width=10, height=2, bg='gray', borderwidth=5 )
    enter3.place(x=150, y=315)
    return None

def button_command3():
    global op
    op = input.get()
    input.delete(0, END)
    print(op)

    input.destroy()

    fourthnumber=Label(window, text="                       Your result is:                         ", bg='gray', fg='black', font=('Helvetica 15'))
    fourthnumber.place(x=0, y=220)

    def add(a, b):
        global result
        result = a + b
        print("Result: ", result)

    def sub(a, b):
        global result
        result = a - b
        print("Result: ", result)

    def mul(a, b):
        global result
        result = a * b
        print("Result: ", result)

    def div(a, b):
        global result
        result = a / b
        print("Result: ", result)




    if op == "+":
        add(a, b)
    elif op == "-":
        sub(a, b)
    elif op == "*":
        mul(a, b)
    elif op == "/":
        div(a, b)



    box = Label(window, text="                                      ", bg='gray', fg='black', font=("Helvetica", 70))
    box.place(x=0, y=255)

    result_label = Label(window, text=result, bg='gray', fg='black', font=("Helvetica", 70))
    result_label.place(x=170, y=255)


    enter3 = Button(window, text=" Close MarKalc ", command=Close_MarKalc, width=15, height=2, bg='gray', borderwidth=5 )
    enter3.place(x=140, y=375)


    return None


def Close_MarKalc():
    window.quit()pp

enter=Button(window, text="Enter", command=button_command, width=10, height=2, bg='gray', borderwidth=5 )
enter.place(x=150, y=315)



name=Label(window, text="MarKalc", bg='gray', fg='black', font=("Helvetica", 70))
name.place(x=30, y=30)
rights=Label(window, text="All bragging right reserved to Mark Pyvovarov, creator of MarKalc?? ", bg='gray', fg='black', font=("Helvetica", 10))
rights.place(x=10, y=570)
future=Label(window, text="                        The calculator of the future                                     ", bg='gray', fg='black', font=("Helvetica", 10))
future.place(x=30, y=130)
window.resizable(0, 0)
window.title("MarKalc")
window.configure(width=400, height=600)
window.configure(bg='gray')
window.mainloop()





