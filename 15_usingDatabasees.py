from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('Learn Tkinter')
root.iconbitmap('./images/favicon.ico')  # add icon
root.geometry('400x400')

# Databases

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Creaate table
c.execute("""CREATE TABLE address (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode interger        
    )""")

# Commit changes
conn.commit()
# Close Connection
conn.close()

root.mainloop()