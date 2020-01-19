# This program creates a calculator using Tkinter to provide a GUI
# Inside the calculator itself it will be able to Multiply, Divide, Add, and Subtract
# Kipland Melton - 01/19/20

import tkinter

root = tkinter.Tk()
root.title("Kip's Calculator")

# TO DO:
# Implement Subtract, Divide, and Multiply Buttons



InputDisplay = tkinter.Entry(root, width='35', borderwidth='5')
InputDisplay.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(integer):
    current = InputDisplay.get()
    InputDisplay.delete(0, tkinter.END)
    InputDisplay.insert(0, str(current) + str(integer))

def button_clear():
    InputDisplay.delete(0, tkinter.END)

def button_add():
    first_int = InputDisplay.get()
    global f_int
    global math
    math = 'add'
    f_int = int(first_int)
    InputDisplay.delete(0, tkinter.END)
def button_subtract():
    first_int = InputDisplay.get()
    global f_int
    global math
    math = 'subtract'
    f_int = int(first_int)
    InputDisplay.delete(0, tkinter.END)
def button_multiply():
    first_int = InputDisplay.get()
    global f_int
    global math
    math = 'multiply'
    f_int = int(first_int)
    InputDisplay.delete(0, tkinter.END)
def button_divide():
    first_int = InputDisplay.get()
    global f_int
    global math
    math = 'divide'
    f_int = int(first_int)
    InputDisplay.delete(0, tkinter.END)


def button_submit():
    second_int = InputDisplay.get()
    InputDisplay.delete(0, tkinter.END)
    if math == 'add':
        InputDisplay.insert(0, f_int + int(second_int))
    elif math == 'subtract':
        InputDisplay.insert(0, f_int - int(second_int))
    elif math == 'multiply':
        InputDisplay.insert(0, f_int * int(second_int))
    elif math == 'divide':
        InputDisplay.insert(0, f_int / int(second_int))


# Defines the buttons 1-0
button_1 = tkinter.Button(root, text='1',padx=40,pady=20,command=lambda:button_click(1))
button_2 = tkinter.Button(root, text='2',padx=40,pady=20,command=lambda:button_click(2))
button_3 = tkinter.Button(root, text='3',padx=40,pady=20,command=lambda:button_click(3))
button_4 = tkinter.Button(root, text='4',padx=40,pady=20,command=lambda:button_click(4))
button_5 = tkinter.Button(root, text='5',padx=40,pady=20,command=lambda:button_click(5))
button_6 = tkinter.Button(root, text='6',padx=40,pady=20,command=lambda:button_click(6))
button_7 = tkinter.Button(root, text='7',padx=40,pady=20,command=lambda:button_click(7))
button_8 = tkinter.Button(root, text='8',padx=40,pady=20,command=lambda:button_click(8))
button_9 = tkinter.Button(root, text='9',padx=40,pady=20,command=lambda:button_click(9))
button_0 = tkinter.Button(root, text='0',padx=40,pady=20,command=lambda:button_click(0))

# Defines function buttons (Clear,Equals)

button_clear = tkinter.Button(root, text='Clear',padx=79,pady=20,command=button_clear)
button_submit = tkinter.Button(root, text='=',padx=91,pady=20,command=button_submit)

# Defines Operator Buttons
button_add = tkinter.Button(root, text='+',padx=39,pady=20,command=button_add)
button_subtract = tkinter.Button(root, text='-',padx=41,pady=20,command=button_subtract)
button_multiply = tkinter.Button(root, text='*',padx=40,pady=20,command=button_multiply)
button_divide = tkinter.Button(root, text='/',padx=39,pady=20,command=button_divide)

# Display buttons to screen

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)

button_clear.grid(row=5,column=1,columnspan=2)
button_submit.grid(row=6,column=1,columnspan=2)

button_add.grid(row=5,column=0)
button_subtract.grid(row=6,column=0)
button_divide.grid(row=4,column=1)
button_multiply.grid(row=4,column=2)








root.mainloop()