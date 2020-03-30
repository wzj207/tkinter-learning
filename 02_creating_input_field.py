from tkinter import *

root = Tk()
e = Entry(root,width=50,bg='white',fg='black',borderwidth=6)
e.pack()
# e.get()
e.insert(0,'Enter Your Name:')

def myClick():
    hello = 'Hello! '+e.get()[len('Enter Your Name:'):]
    myLabel = Label(root, text=hello, bg='red', fg='black')
    myLabel.pack()

myButton = Button(root, text='Enter Your Stock Quote', padx=50, command=myClick, fg='white', bg='#000000')
myButton.pack()

root.mainloop()