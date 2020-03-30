# encoding=utf-8
# frontend
from tkinter import *
from tkinter import messagebox
# import stdDatabase






if __name__ == '__main__':
    root = Tk()
    # root.title('Students Database Management System')
    root.geometry('1350x7500+0+0')
    root.config(bg='Ghost White')
    # root.config(bg='white')

    DataFrameLEFT = LabelFrame(root, bd=1, width=1000, height=600, padx=20, bg='Ghost White', relief=RIDGE)
    DataFrameLEFT.pack(side='left')

    DataFrameRIGHT = LabelFrame(root, bd=1, width=450, height=300, padx=31, pady=3, bg='Ghost White', relief=RIDGE)
    DataFrameRIGHT.pack(side='right')
    root.mainloop()
