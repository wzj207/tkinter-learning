from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn Tkinter')
root.iconbitmap('./images/favicon.ico')  # add icon
root.geometry('400x400')

def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Fridat',
    'Saturday'
]

clicked = StringVar()
# clicked.set('Monday')
clicked.set(options[0])

# drop = OptionMenu(root, clicked, 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Fridat')
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text='Show Selection', command=show).pack()

root.mainloop()