# encoding=utf-8
# frontend
from tkinter import *
from tkinter import messagebox
# import stdDatabase

class Student:

    def __init__(self, root):
        self.root = root
        self.root.title('Students Database Management System')
        # self.root.geometry('1350x750+0+0')
        self.root.config(bg='cadet blue')

        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()  # 出生日期
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        #=========================================Frames===========================================
        MainFrame = Frame(self.root, bg='cadet blue')
        MainFrame.grid()
        # 标题Frame
        TitFrame = Frame(MainFrame, bd=2, padx=54, bg='Ghost White', relief = RIDGE)
        TitFrame.pack(side='top')
        # 标题Label
        self.lblTit = Label(TitFrame, font=('arial', 38, 'bold'), text='Students Database Management System', bg='Ghost White')
        self.lblTit.grid()
        # 按钮Frame
        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg='Ghost White', relief=RIDGE)
        ButtonFrame.pack(side='bottom')

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, bg='Ghost White', relief=RIDGE)
        DataFrame.pack(side='bottom')

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, bg='Ghost White', relief=RIDGE,
                                   font=('arial', 20, 'bold'), text='Student Info\n')
        DataFrameLEFT.pack(side='left')

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, bg='Ghost White',
                                    relief=RIDGE, font=('arial', 20, 'bold'), text='Student Details\n')
        DataFrameRIGHT.pack(side='right')
        # =========================================Labels and Entry Widgets========================
        self.lblStdID = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text='Students ID:', padx=2, pady=2, bg='Ghost White')
        self.lblStdID.grid(row=0, column=0, sticky=W)
        self.textStdID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID, width=39)
        self.textStdID.grid(row=0, column=1)

        self.lblfna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text='Firstname:', padx=2, pady=2, bg='Ghost White')
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.textfna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Firstname, width=39)
        self.textfna.grid(row=1, column=1)

        self.lblSna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text='Surname:', padx=2, pady=2, bg='Ghost White')
        self.lblSna.grid(row=2, column=0, sticky=W)
        self.textSna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Surname, width=39)
        self.textSna.grid(row=2, column=1)

        self.lblDoB = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text='Date of Birth:', padx=2, pady=2, bg='Ghost White')
        self.lblDoB.grid(row=3, column=0, sticky=W)
        self.textDoB = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=DoB, width=39)
        self.textDoB.grid(row=3, column=1)

        self.lblAge = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text='Age:', padx=2, pady=2, bg='Ghost White')
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.textAge = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Age, width=39)
        self.textAge.grid(row=4, column=1)

        self.lblGender = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text='Gender:', padx=2, pady=2, bg='Ghost White')
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.textGender = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Gender, width=39)
        self.textGender.grid(row=5, column=1)

        self.lblAdr = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text='Address:', padx=2, pady=2, bg='Ghost White')
        self.lblAdr.grid(row=6, column=0, sticky=W)
        self.textAdr = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Address, width=39)
        self.textAdr.grid(row=6, column=1)

        self.lblMobile = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text='Mobile:', padx=2, pady=2, bg='Ghost White')
        self.lblMobile.grid(row=7, column=0, sticky=W)
        self.textMobile = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Mobile, width=39)
        self.textMobile.grid(row=7, column=1)
        #================================ListBox & ScrollBar Widget================================

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky=NS)

        studentlist = Listbox(DataFrameRIGHT, width=41, height=16, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        studentlist.grid(row=0, column=1, padx=8)
        scrollbar.config(command = studentlist.yview)

        #======================================Button Widget========================================
        self.btnAddData = Button(ButtonFrame, text='Add New', font=('arial', 20, 'bold'), height=1, width=10, bd=4)
        self.btnAddData.grid(row=0, column=0, padx=8)
        self.btnDisplayData = Button(ButtonFrame, text='Display New', font=('arial', 20, 'bold'), height=1, width=10, bd=4)
        self.btnDisplayData.grid(row=0, column=1, padx=8)
        self.btnClearData = Button(ButtonFrame, text='Clear', font=('arial', 20, 'bold'), height=1, width=10, bd=4)
        self.btnClearData.grid(row=0, column=2, padx=8)
        self.btnDeleteData = Button(ButtonFrame, text='Delete', font=('arial', 20, 'bold'), height=1, width=10, bd=4)
        self.btnDeleteData.grid(row=0, column=3, padx=8)
        self.btnSearchData = Button(ButtonFrame, text='Search', font=('arial', 20, 'bold'), height=1, width=10, bd=4)
        self.btnSearchData.grid(row=0, column=4, padx=8)
        self.btnUpdateData = Button(ButtonFrame, text='Update', font=('arial', 20, 'bold'), height=1, width=10, bd=4)
        self.btnUpdateData.grid(row=0, column=5, padx=8)
        self.btnExit = Button(ButtonFrame, text='Exit', font=('arial', 20, 'bold'), height=1, width=10, bd=4)
        self.btnExit.grid(row=0, column=6, padx=8)










if __name__ == '__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
