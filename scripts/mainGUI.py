import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter.constants import END, LEFT, TOP, BOTTOM, RIGHT
from contact import Contact
from tkinter.font import Font


class PhoneBook(tk.Tk):
    def __init__(self):
        super().__init__()
        self.book1 = {}
        self.newC = False
        self.heading = Font(family="Helvetica", size=25, weight="bold")
        self.labels = Font(family="Helvetica", size=18, weight="bold")
        # configure the root window
        self.title('Phone Book')
        self.resizable(0, 0)
        self.geometry('900x700')
        self['bg'] = 'sky blue'

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
        self.label = ttk.Label(
            self)

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
        self.sNam.pack_forget()

        self.edNameE = ttk.Entry(self, width=30)
        self.edNameE.pack_forget()

        self.edSnameE = ttk.Entry(self, width=30)
        self.edSnameE.pack_forget()

        self.edPhoneE = ttk.Entry(self, width=30)
        self.edPhoneE.pack_forget()

        self.edEmailE = ttk.Entry(self, width=30)
        self.edEmailE.pack_forget()

        self.edAddressE = ttk.Entry(self, width=30)
        self.edAddressE.pack_forget()

        self.saveEdit = ttk.Button(
            self, text="Update Details", command=self.modifyC, style="W.TButton")
        self.saveEdit.pack_forget()

        self.searchThis = None

        self.allContactsB = ttk.Label(
            self, text="Contacts List", font=self.labels)

    def searchN(self):
        snm = self.editName.get()
        self.searchThis = snm
        defaultV = []
        for k, v in self.book1.items():
            if snm == k:
                self.sNam.configure(text=k + " " + v.surname)
                defaultV.append(v.first_name)
                defaultV.append(v.surname)
                defaultV.append(v.phone.get_phone())
                defaultV.append(v.email.get_email())
                defaultV.append(v.address.get_address())

        self.editName.delete(0, "end")

        self.edNameE.insert(END, defaultV[0])
        self.edSnameE.insert(END, defaultV[1])
        self.edPhoneE.insert(END, defaultV[2])
        self.edEmailE.insert(END, defaultV[3])
        self.edAddressE.insert(END, defaultV[4])

        self.sNam.pack()
        self.edNameE.pack()
        self.edPhoneE.pack()
        self.edEmailE.pack()
        self.edAddressE.pack()
        self.saveEdit.pack()

    def modifyC(self):
        snm = self.searchThis

        editCo = self.book1[snm]

        editCo.edit_name(self.edNameE.get())
        editCo.edit_surname(self.edSnameE.get())
        editCo.get_phone().modify_phone(self.edPhoneE.get())
        editCo.get_email().modify_email(self.edEmailE.get())
        editCo.get_address().modify_address(self.edAddressE.get())
        self.book1[self.edNameE.get()] = editCo
        del self.book1[snm]

        self.edNameE.delete(0, "end")
        self.edSnameE.delete(0, "end")
        self.edPhoneE.delete(0, "end")
        self.edEmailE.delete(0, "end")
        self.edAddressE.delete(0, "end")

        self.sNam.pack_forget()
        self.edNameE.pack_forget()
        self.edPhoneE.pack_forget()
        self.edEmailE.pack_forget()
        self.edAddressE.pack_forget()
        self.saveEdit.pack_forget()

        self.newC = True

    def time_string(self):
        if self.newC:
            allC = ""
            for k, v in self.book1.items():
                allC += k + "  " + v.surname + "  " + v.phone.get_phone() + "  " + \
                    v.email.get_email() + "  " + v.address.get_address() + "\n"

            return allC

    def update(self):
        self.label.configure(text=self.time_string())
        self.allContactsB.pack(pady=5)
        self.label.pack(pady=20)
        self.newC = False
        self.label.after(1000, self.update)

    def clickedSave(self):
        n = self.ename.get()
        sm = self.esname.get()
        em = self.eemail.get()
        ad = self.eaddr.get()
        pn = self.ephne.get()
        c = Contact(n, sm)
        c.phone.add_phone(pn)
        c.address.add_address(ad)
        c.email.add_email(em)
        self.book1[n] = c
        self.ename.delete(0, "end")
        self.esname.delete(0, "end")
        self.eemail.delete(0, "end")
        self.ephne.delete(0, "end")
        self.eaddr.delete(0, "end")
        self.newC = True


if __name__ == "__main__":
    phonebook = PhoneBook()
    phonebook.mainloop()
