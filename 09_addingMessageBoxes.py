from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('Learn Tkinter')
root.iconbitmap('./images/favicon.ico')  # add icon


def popup():
    # messagebox.showinfo('This is my Popup!', 'Hello world!')
    # messagebox.showwarning('This is my Popup!', 'Warning!')
    # messagebox.showerror('This is my Popup!', 'Error!')
    # messagebox.askquestion('This is my Popup!', 'Sure?')
    # messagebox.askokcancel('This is my Popup!', 'Sure?')
    response = messagebox.askyesno('This is my Popup!', 'Sure?')
    # Label(root, text=response).pack()
    if response == 1:
        Label(root, text='You Clicked Yes!').pack()
    else:
        Label(root, text='You Clicked No!').pack()

Button(root, text='Popup', command=popup).pack()


root.mainloop()