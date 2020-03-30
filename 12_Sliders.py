from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title('Learn Tkinter')
root.iconbitmap('./images/favicon.ico')  # add icon
root.geometry('400x400')

vertical = Scale(root, from_=400, to=900)
vertical.pack()

def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+'x'+str(vertical.get()))

horizontal = Scale(root, from_=400, to=900, orient=HORIZONTAL)
horizontal.pack()
# horizontal.get()

my_btn = Button(root, text='Window Size', command=slide).pack()

root.mainloop()