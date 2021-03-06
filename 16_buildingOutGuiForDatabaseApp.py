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
'''
c.execute("""CREATE TABLE address (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode interger        
    )""")
'''
# Create Submit Function for Database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Insert Into Table
    c.execute('INSERT INTO address VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)',
              {
                  "f_name": f_name.get(),
                  "l_name": l_name.get(),
                  "address": address.get(),
                  "city": city.get(),
                  "state": state.get(),
                  "zipcode": zipcode.get(),
              })

    # Commit changes
    conn.commit()
    # Close Connection
    conn.close()

    # Clear The Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Query the Database
    c.execute("SELECT *, oid FROM address")
    records = c.fetchall()
    # c.fetchone()
    # c.fetchmany(50)
    print(records)

    # Loop thru results
    print_records = ''
    for record in records:
        # print_records += str(record) + '\n'
        # print_records += str(record[1]) + '\n'
        print_records += str(record[0]) + ' ' +str(record[1]) +  '\n'
    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    # Commit changes
    conn.commit()
    # Close Connection
    conn.close()

# Create Text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

# Create Text Box Labels
f_name_label = Label(root, text='First Name')
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text='Last Name')
l_name_label.grid(row=1, column=0)
address_label = Label(root, text='Address')
address_label.grid(row=2, column=0)
city_label = Label(root, text='City')
city_label.grid(row=3, column=0)
state_label = Label(root, text='State')
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text='Zipcode')
zipcode_label.grid(row=5, column=0)

# Create Submit Button
submit_btn = Button(root, text='Add Record To Database', command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Create a Query a Button
query_btn = Button(root, text='Show Records', command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Commit changes
conn.commit()
# Close Connection
conn.close()

root.mainloop()