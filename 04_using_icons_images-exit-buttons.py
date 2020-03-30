from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn Tkinter')
root.iconbitmap('./images/favicon.ico')  # add icon

# add images
my_img = ImageTk.PhotoImage(Image.open('./images/wuqian_01.jpg'))
my_label = Label(image=my_img)
my_label.pack()

# Quit Button
button_quit = Button(root, text='Exit Program', command=root.quit)
button_quit.pack()



root.mainloop()