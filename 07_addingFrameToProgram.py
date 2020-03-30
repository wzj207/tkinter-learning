from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn Tkinter')
root.iconbitmap('./images/favicon.ico')  # add icon

# frame = LabelFrame(root, text='This is my Frame...', padx=50, pady=50)
frame = LabelFrame(root, padx=10, pady=50)
frame.pack(padx=80, pady=10)

b1 = Button(frame, text="Don't Click Here!")
b1.grid(row=0, column=0)

b2 = Button(frame, text="...Or Here!")
b2.grid(row=1, column=1)

root.mainloop()