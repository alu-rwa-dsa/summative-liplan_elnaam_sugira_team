import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter.constants import E, END, LEFT, TOP, BOTTOM, RIGHT, W, Y
from contact import Contact
from tkinter.font import Font
from tkinter import messagebox


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
        self['bg'] = 'black'

        self.v = ttk.Scrollbar(self)
        self.v.pack(side=RIGHT, fill=Y)

        # change the background color to black
        self.style = ttk.Style(self)
        self.style.configure(
            'TLabel',
            background='black',
            foreground='#572780')
        self.style.configure('W.TButton', font=(
            'Arial', 15), foreground='black', background="#572780")

        # label
        self.welcome = ttk.Label(
            self, text="Your Phone Book", font=self.heading)
        self.welcome.pack(pady=10)

        self.label = tk.Text(
            self, font=self.contactsLabels, foreground="white")

        self.name = ttk.Label(self, text="Name", font=self.labels)

        # vname = self.register(self.validatename)
        # vphone = self.register(self.validatePhone)
        # vemail = self.register(self.validateEmail)
        # vaddr = self.register(self.validateAddress)
        
        self.ename = ttk.Entry(self, width=30)
        # self.ename.config(validate="focusout", validatecommand=(vname, "%P"))
        
        self.sname = ttk.Label(self, text="Surname", font=self.labels)
        
        self.esname = ttk.Entry(self, width=30)
        
        self.phne = ttk.Label(self, text="Phone", font=self.labels)
        
        self.ephne = ttk.Entry(self, width=30)
        
        self.email = ttk.Label(self, text="Email", font=self.labels)
        
        self.eemail = ttk.Entry(self, width=30)
        
        self.addr = ttk.Label(self, text="Address", font=self.labels)
        
        self.eaddr = ttk.Entry(self, width=30)
        
        self.saveAdd = ttk.Button(
            self, text="Save Contact", command=self.clickedSave, style="W.TButton")
        
        # schedule an update every 1 second
        self.label.after(1000, self.update)

        # edit contact
        self.editNamel = ttk.Label(
            self, text="Search a contact", font=self.labels)

        self.editName = ttk.Entry(self, width=30)

        self.searchNa = ttk.Button(
            self, text="Search Contact", command=self.searchN, style="W.TButton")

        self.sNam = ttk.Label(self, font=self.labels)

        self.edNameE = ttk.Entry(self, width=30)

        self.edSnameE = ttk.Entry(self, width=30)

        self.edPhoneE = ttk.Entry(self, width=30)

        self.edEmailE = ttk.Entry(self, width=30)

        self.edAddressE = ttk.Entry(self, width=30)

        self.saveEdit = ttk.Button(
            self, text="Update Details", command=self.modifyC, style="W.TButton")

        self.searchThis = None

        # database
        try:
            self.connection = mysql.connector.connect(host='us-cdbr-east-03.cleardb.com', database='heroku_8837d61ef32d131', user='b7c1f87fd3c12d', password='8480f5d9')

        except Error as e:
            print("Error while connecting to MySQL", e)

        self.ref = 0

        self.btn = ttk.Button(self, text="Delete Contact", command=self.deleteContact, style="W.TButton")

        self.showAdd = ttk.Button(self, text="Add Contact", command=self.showAddC, style="W.TButton")
        self.showAdd.pack(pady=10)
        self.showMo = ttk.Button(self, text="Modify or Delete a contact", command=self.showEditC, style="W.TButton")
        self.showMo.pack(pady=10)

        self.allContactsB = ttk.Label(
            self, text="Contacts List", font=self.labels)
        self.allContactsB.pack(pady=10)

        self.goHome = ttk.Button(self, text="Back Home", command=self.goHomeB, style="W.TButton")
    
    def goHomeB(self):
        self.showAdd.pack(pady=10)
        self.showMo.pack(pady=10)
        self.allContactsB.pack(pady=10)
        self.label.pack(padx=10, pady=20, expand=True)
        
        self.name.pack_forget()
        self.ename.pack_forget()
        self.sname.pack_forget()
        self.esname.pack_forget()
        self.phne.pack_forget()
        self.ephne.pack_forget()
        self.email.pack_forget()
        self.eemail.pack_forget()
        self.addr.pack_forget()
        self.eaddr.pack_forget()
        self.saveAdd.pack_forget()

        self.editNamel.pack_forget()
        self.editName.pack_forget()
        self.searchNa.pack_forget()

        self.sNam.pack_forget()
        self.edNameE.pack_forget()
        self.edSnameE.pack_forget()
        self.edPhoneE.pack_forget()
        self.edEmailE.pack_forget()
        self.edAddressE.pack_forget()

        self.btn.pack_forget()
        self.saveEdit.pack_forget()

        self.goHome.pack_forget()

    def showEditC(self):
        self.label.pack_forget()
        self.allContactsB.pack_forget()

        self.editNamel.pack()
        self.editName.pack()
        self.searchNa.pack(pady=10)

        self.showAdd.pack_forget()
        self.showMo.pack_forget()

        self.goHome.pack(pady=10)
    
    def validatename(self, value):
        if len(value) < 2 or value.isalpha() is False:
            return False
        return True
    
    def validatePhone(self, value):
        if len(value) != 10:
            return False
        return True
    
    def validateEmail(self, value):
        exists = "@" in value
        if exists:
            return True
        return False
    
    def validateAddress(self, value):
        if len(value) < 2:
            return False
        return True

    def showAddC(self):
        self.allContactsB.pack_forget()
        self.label.pack_forget()

        self.goHome.pack(pady=10)
        self.name.pack()
        self.ename.pack()
        self.sname.pack()
        self.esname.pack()
        self.phne.pack()
        self.ephne.pack()
        self.email.pack()
        self.eemail.pack()
        self.addr.pack()
        self.eaddr.pack()
        self.saveAdd.pack(pady=10)

        self.showAdd.pack_forget()
        self.showMo.pack_forget()

    def searchN(self):
        self.editNamel.pack_forget()
        self.editName.pack_forget()
        self.searchNa.pack_forget()

        snm = self.editName.get()

        self.searchThis = snm

        defaultV = []

        # retrieve name from db and set defaults
        sql_select_Query = "select * from contacts"
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute(sql_select_Query)
        allContacts = cursor.fetchall()

        upTo = len(allContacts)
        notIn = 0
        for row in allContacts:
            if snm != row[1]:
                notIn += 1
            if notIn == upTo:
                messagebox.showerror("Error", "Contact name not available")
                self.label.pack_forget()
                self.allContactsB.pack_forget()
                self.goHome.pack(pady=10)
                self.editNamel.pack()
                self.editName.pack()
                self.searchNa.pack()
                self.showAdd.pack_forget()
                self.showMo.pack_forget()
                return

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

        self.goHome.pack(pady=10)
        self.sNam.pack(pady=5)

        self.edNameE.pack(pady=5)
        self.edSnameE.pack(pady=5)
        self.edPhoneE.pack(pady=5)
        self.edEmailE.pack(pady=5)
        self.edAddressE.pack(pady=5)

        self.btn.pack(pady=5)
        self.saveEdit.pack(pady=5)

        self.label.pack_forget()
        self.allContactsB.pack_forget()

        self.newC = False
    
    def deleteContact(self):
        self.goHome.pack_forget()
        if messagebox.askokcancel("Confirm Delete", "Are you sure you want to delete the contact?"):
            snm = self.searchThis

            sql_Delete_query = """Delete from contacts where name = %s"""

            self.connection.reconnect()
            cursor = self.connection.cursor()
            cursor.execute(sql_Delete_query, (snm,))
            self.connection.commit()

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

            self.btn.pack_forget()
            messagebox.showinfo("Contact Deleted", "Contact deleted successfully")
            self.showAdd.pack(pady=10)
            self.showMo.pack(pady=10)
            self.allContactsB.pack(pady=10)
            self.newC = True

            cursor.close()
            self.connection.close()

    def modifyC(self):
        self.goHome.pack_forget()
        snm = self.searchThis
        # update db
        mySql_update_query = """Update contacts set name = %s, surname = %s, phone = %s,  email = %s, address = %s where name = %s"""
        
        cursor = self.connection.cursor()
        print("Second name : " + self.edSnameE.get())
        upD = (self.edNameE.get(), self.edSnameE.get(), self.edPhoneE.get(), self.edEmailE.get(), self.edAddressE.get(), snm)
      
        cursor.execute(mySql_update_query, upD)
        self.connection.commit()
        print("Updated in db")
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
        self.btn.pack_forget()

        messagebox.showinfo("Contact Modified", "Contact modified successfully")

        self.showAdd.pack(pady=10)
        self.showMo.pack(pady=10)
        self.allContactsB.pack(pady=10)

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
                insertToText += row[1] + "  " + row[2] + "  " + row[0] + "  " + row[3] + "  " + row[4] + "\n\n"
            
            self.connection.close()
            cursor.close()

            self.label.insert(END, insertToText)
            self.label.pack(padx=10, pady=20, expand=True)
            self.label.config(width=60, background="#37474f", borderwidth=0)
            self.ref = 1
            self.goHome.pack_forget()

    def update(self):
        self.time_string()
        self.v.config(command=self.label.yview)
        self.newC = False
        self.label.after(1000, self.update)

    def clickedSave(self):
        self.goHome.pack_forget()
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
            messagebox.showerror("Error", "The email is already in use")
            self.ename.delete(0, "end")
            self.esname.delete(0, "end")
            self.eemail.delete(0, "end")
            self.ephne.delete(0, "end")
            self.eaddr.delete(0, "end")
            self.goHome.pack(pady=10)
            self.connection.close()
            return

        self.ename.delete(0, "end")
        self.esname.delete(0, "end")
        self.eemail.delete(0, "end")
        self.ephne.delete(0, "end")
        self.eaddr.delete(0, "end")

        messagebox.showinfo("Contact Saved", "Contact saved successfully")

        self.name.pack_forget()
        self.ename.pack_forget()
        self.sname.pack_forget()
        self.esname.pack_forget()
        self.phne.pack_forget()
        self.ephne.pack_forget()
        self.email.pack_forget()
        self.eemail.pack_forget()
        self.addr.pack_forget()
        self.eaddr.pack_forget()
        self.saveAdd.pack_forget()
        self.showAdd.pack(pady=10)
        self.showMo.pack(pady=10)
        self.allContactsB.pack(pady=10)

        self.newC = True


if __name__ == "__main__":
    phonebook = PhoneBook()
    phonebook.mainloop()
