import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter.constants import E, END, LEFT, TOP, BOTTOM, RIGHT, W, Y
from contact import Contact
from tkinter.font import Font
# mysql://
# b7c1f87fd3c12d
# 8480f5d9@
# #us-cdbr-east-03.cleardb.com/
# #heroku_8837d61ef32d131?reconnect=true


class PhoneBook(tk.Tk):
    def __init__(self):
        super().__init__()
        self.book1 = {}
        self.newC = False
        self.heading = Font(family="Helvetica", size=25, weight="bold")
        self.labels = Font(family="Helvetica", size=18, weight="bold")
        self.contactsLabels = Font(family="Helvetica", size=15, weight="bold")
        # configure the root window
        self.title('Phone Book')
        # self.resizable(0, 0)
        self.geometry('900x700')
        self['bg'] = 'sky blue'

        self.v = ttk.Scrollbar(self)
        self.v.pack(side=RIGHT, fill=Y)

        # change the background color to black
        self.style = ttk.Style(self)
        self.style.configure(
            'TLabel',
            background='sky blue',
            foreground='blue')
        self.style.configure('W.TButton', font=(
            'Arial', 15, 'underline'), foreground='Green')

        # label
        self.welcome = ttk.Label(
            self, text="Your Phone Book", font=self.heading)
        self.welcome.pack(pady=10)

        self.label = tk.Text(
            self, font=self.contactsLabels, foreground="white")

        # self.label = ttk.Label(self, font=self.contactsLabels)#

        self.name = ttk.Label(self, text="Name", font=self.labels)
        self.name.pack()
        self.ename = ttk.Entry(self, width=30)
        self.ename.pack()

        self.sname = ttk.Label(self, text="Surname", font=self.labels)
        self.sname.pack()
        self.esname = ttk.Entry(self, width=30)
        self.esname.pack()

        self.phne = ttk.Label(self, text="Phone", font=self.labels)
        self.phne.pack()
        self.ephne = ttk.Entry(self, width=30)
        self.ephne.pack()

        self.email = ttk.Label(self, text="Email", font=self.labels)
        self.email.pack()
        self.eemail = ttk.Entry(self, width=30)
        self.eemail.pack()

        self.addr = ttk.Label(self, text="Address", font=self.labels)
        self.addr.pack()
        self.eaddr = ttk.Entry(self, width=30)
        self.eaddr.pack()

        self.saveAdd = ttk.Button(
            self, text="Save Contact", command=self.clickedSave, style="W.TButton")
        self.saveAdd.pack(pady=10)

        # schedule an update every 1 second
        self.label.after(1000, self.update)

        # edit contact
        self.editNamel = ttk.Label(
            self, text="Search a contact to edit", font=self.labels)
        self.editNamel.pack()

        self.editName = ttk.Entry(self, width=30)
        self.editName.pack(pady=10)

        self.searchNa = ttk.Button(
            self, text="Search Contact", command=self.searchN, style="W.TButton")
        self.searchNa.pack()

        self.sNam = ttk.Label(self, font=self.labels)

        self.edNameE = ttk.Entry(self, width=30)

        self.edSnameE = ttk.Entry(self, width=30)

        self.edPhoneE = ttk.Entry(self, width=30)

        self.edEmailE = ttk.Entry(self, width=30)

        self.edAddressE = ttk.Entry(self, width=30)

        self.saveEdit = ttk.Button(
            self, text="Update Details", command=self.modifyC, style="W.TButton")

        self.searchThis = None

        self.allContactsB = ttk.Label(
            self, text="Contacts List", font=self.labels)
        self.allContactsB.pack(pady=10)

        # database
        try:
            self.connection = mysql.connector.connect(host='us-cdbr-east-03.cleardb.com', database='heroku_8837d61ef32d131', user='b7c1f87fd3c12d', password='8480f5d9')

        except Error as e:
            print("Error while connecting to MySQL", e)

        self.ref = 0

    def searchN(self):
        snm = self.editName.get()

        self.searchThis = snm

        defaultV = []

        # retrieve name from db and set defaults
        sql_select_Query = "select * from contacts"
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute(sql_select_Query)
        allContacts = cursor.fetchall()

        for row in allContacts:
            if snm == row[1]:
                self.sNam.configure(text="Modifying " + row[1] + " " + row[2])
                defaultV.append(row[1])
                defaultV.append(row[2])
                defaultV.append(row[0])
                defaultV.append(row[3])
                defaultV.append(row[4])

                self.edNameE.insert(END, defaultV[0])
                self.edSnameE.insert(END, defaultV[1])
                self.edPhoneE.insert(END, defaultV[2])
                self.edEmailE.insert(END, defaultV[3])
                self.edAddressE.insert(END, defaultV[4])

        self.editName.delete(0, "end")

        self.sNam.pack(pady=5)

        self.edNameE.pack(pady=5)
        self.edSnameE.pack(pady=5)
        self.edPhoneE.pack(pady=5)
        self.edEmailE.pack(pady=5)
        self.edAddressE.pack(pady=5)

        self.saveEdit.pack(pady=5)

        self.label.pack_forget()
        self.allContactsB.pack_forget()

        self.newC = False

    def modifyC(self):
        # update db
        mySql_update_query = """Update contacts set name = %s, surname = %s, phone = %s,  email = %s, address = %s where email = %s"""
        
        cursor = self.connection.cursor()
        upD = (self.edNameE.get(), self.edSnameE.get(), self.edPhoneE.get(), self.edEmailE.get(), self.edAddressE.get(), self.edEmailE.get())
      
        cursor.execute(mySql_update_query, upD)
        print("Updated in db")
        self.connection.commit()
        cursor.close()
        self.connection.close()
        
        self.edNameE.delete(0, "end")
        self.edSnameE.delete(0, "end")
        self.edPhoneE.delete(0, "end")
        self.edEmailE.delete(0, "end")
        self.edAddressE.delete(0, "end")

        self.sNam.pack_forget()
        self.edSnameE.pack_forget()
        self.edNameE.pack_forget()
        self.edPhoneE.pack_forget()
        self.edEmailE.pack_forget()
        self.edAddressE.pack_forget()
        self.saveEdit.pack_forget()

        self.newC = True

    def time_string(self):
        if self.newC or self.ref == 0:
            # get all contacts from db
            sql_select_Query = "select * from contacts"
            self.connection.reconnect()
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            allContacts = cursor.fetchall()

            self.label.delete(1.0, END)
            insertToText = ""

            for row in allContacts:
                insertToText += row[1] + " " + row[2] + " " + row[0] + " " + row[3] + " " + row[4] + "\n"
            
            self.connection.close()
            cursor.close()

            self.label.insert(END, insertToText)
            self.label.pack(padx=10, pady=10, expand=True)
            self.label.config(width=60)
            self.ref = 1

    def update(self):
        # self.label.configure(text=self.time_string(), foreground="black")
        self.time_string()
        self.v.config(command=self.label.yview)
        self.newC = False
        self.label.after(1000, self.update)

    def clickedSave(self):
        n = self.ename.get()
        sm = self.esname.get()
        em = self.eemail.get()
        ad = self.eaddr.get()
        pn = self.ephne.get()

        # save to db
        mySql_insert_query = """INSERT INTO contacts (email, name, surname, phone, address)
                           VALUES (%s, %s, %s, %s, %s)"""
        
        allD = (em, n, sm, pn, ad)
        try:
            self.connection.reconnect()
            cursor = self.connection.cursor()
            cursor.execute(mySql_insert_query, allD)
            self.connection.commit()
            cursor.close()
            self.connection.close()
        except mysql.connector.IntegrityError as err:
            print("Email already in use")
            self.ename.delete(0, "end")
            self.esname.delete(0, "end")
            self.eemail.delete(0, "end")
            self.ephne.delete(0, "end")
            self.eaddr.delete(0, "end")
            self.connection.close()
            return

        self.ename.delete(0, "end")
        self.esname.delete(0, "end")
        self.eemail.delete(0, "end")
        self.ephne.delete(0, "end")
        self.eaddr.delete(0, "end")

        self.newC = True


if __name__ == "__main__":
    phonebook = PhoneBook()
    phonebook.mainloop()
