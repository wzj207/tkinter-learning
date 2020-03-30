from tkinter import *

root = Tk()
root.title('Simple Calculator')
# root.geometry('500x700')

e = Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
# e.insert(0,'')

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_num = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_num)
    e.delete(0,END)

def button_equal():
    second_num = e.get()
    e.delete(0,END)

    if math == 'addition':
        e.insert(0,f_num + int(second_num))

    elif math == 'subtraction':
        e.insert(0,f_num - int(second_num))

    elif math == 'multiplication':
        e.insert(0,f_num * int(second_num))

    elif math == 'division':
        e.insert(0,f_num / int(second_num))

def button_subtract():
    first_num = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_num)
    e.delete(0, END)

def button_multiply():
    first_num = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_num)
    e.delete(0, END)

def button_divide():
    first_num = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_num)
    e.delete(0, END)
# Define Buttons

button_01 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_02 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_03 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_04 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_05 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_06 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_07 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_08 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_09 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda:button_click(0))
button_add = Button(root, text='+', padx=39, pady=20, command=button_add)
button_equal = Button(root, text='=', padx=97, pady=20, command=button_equal)
button_clear = Button(root, text='Claer', padx=84, pady=20, fg='red', command=button_clear)
button_subtract = Button(root, text='-', padx=41, pady=20, command=button_subtract)
button_multiply = Button(root, text='X', padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text='/', padx=41, pady=20, command=button_divide)

# Put the button on the screen

button_01.grid(row=3,column=0)
button_02.grid(row=3,column=1)
button_03.grid(row=3,column=2)

button_04.grid(row=2,column=0)
button_05.grid(row=2,column=1)
button_06.grid(row=2,column=2)

button_07.grid(row=1,column=0)
button_08.grid(row=1,column=1)
button_09.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

root.mainloop()