from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Students database")
root.iconbitmap("e:/Coding STUFF/Python/Image/meteor_asteroid_icon_149797.ico")

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
 
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))


#Databases
#Create a database or connect to one
conn=sqlite3.connect("Users.db")

#Create cursor
c = conn.cursor()

#Create table
#c.execute("""CREATE TABLE Users (
#            f_name text,
#            last_name text,
#            e_mail text,
#            password text,
#            domain text)""")

#Create submit function 
def submit():
    #Create a database or connect to one
    conn=sqlite3.connect("Users.db")

    #Create cursor
    c = conn.cursor()

    #Insert into tablesearch_box = Entry(root, width = 46)
    c.execute("INSERT INTO Users VALUES (:f_name, :last_name, :e_mail, :password, :domain)",
        {
            'f_name': f_name.get(),
            'last_name': last_name.get(),
            'e_mail': e_mail.get(),
            'password': password.get(),
            'domain': domain.get()
        })


    #Commit changes
    conn.commit()

    #Close connection
    conn.close()

    #Clear the boxes
    f_name.delete(0, END)
    last_name.delete(0, END)
    e_mail.delete(0, END) 
    password.delete(0, END)
    domain.delete(0, END)

#Create delete function
def delete():
    #Create a database or connect to one
    conn=sqlite3.connect("Users.db")

    #Create cursor
    c = conn.cursor()

    #Delete a record
    c.execute("DELETE from Users WHERE oid= " + delete_box.get())

    #Commit changes
    conn.commit()

    #Close connection
    conn.close()
    return

#Create query function
def query():
    top=Toplevel()
    top.title("Searched information")

    #Create a database or connect to one
    conn=sqlite3.connect("Users.db")

    #Create cursor
    c = conn.cursor()
    
    #Select information table
    c.execute("SELECT *, oid from Users")
    records=c.fetchall()

    #Loop through results
    print_records = ''
    for record in records:
        print_records += str(record[4]) + "\t" + "\t"+ str(record[3]) + "\t" + "\t"+ str(record[2] + "\t" + "\t"+ str(record[1])) + "\n"
    #my_label = Label(top, text=print_records, bd=1, relief="solid", font="Times 18", justify= LEFT).pack()
    button_close = Button(top, text="close window", command=top.destroy).pack()
    search_box.delete(0, END)

    #Commit changes
    conn.cursor()

    #Close connection
    conn.close()
    return

#Create open function
def open():
    top=Toplevel()
    top.title("Searched information")
    i=0
     #Create a database or connect to one
    conn=sqlite3.connect("Users.db")

    #Create cursor
    c = conn.cursor()

    #Select information table
    c.execute("SELECT *, domain from Users")
    records=c.fetchall()
    print_records = ''
    for record in records:
        if search_box.get() == record[4]:
            print_records += str(record[4]) + "\t" + "\t"+ str(record[3]) + "\t" + "\t" + str(record[2] + "\t" + "\t" + str(record[1])) + "\n"
            i+=i
    if i ==0:
        my_label = Label(top, text="NO MATCH", bd=1, relief="solid", font="Times 18", justify= LEFT).pack()
    else:
        my_label = Label(top, text=print_records, bd=1, relief="solid", font="Times 18", justify= LEFT).pack()
    button_close = Button(top, text="close window", command=top.destroy).pack()
    search_box.delete(0, END)


    #Commit changes
    conn.cursor()

    #Close connection
    conn.close()
    return

#Creating boxes
f_name = Entry(root, width=20)
f_name.grid(row = 0, column = 1, padx = 20, ipadx=50)
last_name = Entry(root, width=20)
last_name.grid(row=1, column=1, padx= 20, ipadx=50)
e_mail = Entry(root, width=20)
e_mail.grid(row=2, column=1, padx =20, ipadx=50)
password = Entry(root, width = 20)
password.grid(row=3, column=1, padx=20, ipadx=50)
domain = Entry(root, width=20)
domain.grid(row=4, column=1, padx=20, ipadx=50)
delete_box = Entry(root, width = 46)
delete_box.grid(row=8, column=0, columnspan = 10, padx=20)
search_box = Entry(root, width = 46)
search_box.grid(row=12, column=0, columnspan = 10, padx=20)

#Create labels

f_name_label = Label(root, text="First name")   
f_name_label.grid(row=0, column=0)
last_name_label = Label(root, text="Last name")   
last_name_label.grid(row=1, column=0)
e_mail_label = Label(root, text="E-mail")   
e_mail_label.grid(row=2, column=0)
password_label = Label(root, text="Password")   
password_label.grid(row=3, column=0)
domain_label = Label(root, text="Course")  
domain_label.grid(row=4, column=0)

#Create submit button
submit_btn = Button(root, text="Add new record", command=submit)
submit_btn.grid(row=5, column=0, columnspan=2, padx=10, pady=10, ipadx=94)

#Create a query button 
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

#Create a delete button
delete_btn = Button(root, text="Delete record", command=delete)
delete_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=101)

#Create a search button
search_btn = Button(root, text="Search record by domain", command=open)
search_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=72)

#Commit changes
conn.commit()

#Close connection
conn.close()


root.mainloop()