from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn Tkinter')
root.iconbitmap('./images/favicon.ico')  # add icon
root.geometry('400x400')

# var = IntVar()
var = StringVar()

c = Checkbutton(root, text='Check this box, I dare you!', variable=var,
                onvalue='on', offvalue='off')
c.deselect()
c.pack()
def show():
    my_label = Label(root, text=var.get()).pack()

myButton = Button(root, text='Show Selection', command=show).pack()

root.mainloop()