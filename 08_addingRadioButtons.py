from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn Tkinter')
root.iconbitmap('./images/favicon.ico')  # add icon

# r = IntVar()
# r.set('22')
# r.get()


TOPPINGS = [
    ('Pepperoni', 'Pepperoni'),
    ('Cheese', 'Cheese'),
    ('Mushroom', 'Mushroom'),
    ('Onion', 'Onion'),
]

pizz = StringVar()
pizz.set('Pepperoni')

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizz, value=topping).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

# Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda:clicked(r.get())).pack()
# Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda:clicked(r.get())).pack()

# myLabel = Label(root, text=pizz.get())
# myLabel.pack()

myButton = Button(root, text='Click Me!', command=lambda:clicked(pizz.get()))
myButton.pack()

root.mainloop()