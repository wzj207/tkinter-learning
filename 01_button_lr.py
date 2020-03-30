from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text='Look I clicked a Button!', bg='gray', fg='black')
    myLabel.pack()

myButton = Button(root, text='Click Me!', padx=50, command=myClick, fg='white', bg='#000000')
myButton.pack()

root.mainloop()