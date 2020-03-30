from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('Learn Tkinter')
root.iconbitmap('./images/favicon.ico')  # add icon

def open_new_window():
    global my_img
    top = Toplevel()
    top.title('吴倩')
    top.iconbitmap('./images/favicon.ico')  # add icon
    my_img = ImageTk.PhotoImage(Image.open('./images/wuqian_01.jpg'))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text='close window', command=top.destroy).pack()

btn = Button(root, text='New Window', command=open_new_window).pack()



root.mainloop()