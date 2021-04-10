from tkinter import *
from contact import Contact

root = Tk()
root.title("Your Phone Book")
root.geometry('800x800')

a = Label(root, text="Welcome [name]").grid(columnspan=3)


def clicked():
    pass


addContact = Button(root, text="Create").grid(column=6, row=1)

# create contact -- start
namel = Label(root, text="Enter name").grid(column=1, row=2)
name = Entry(root, width=10).grid(column=2, row=2)

snamel = Label(root, text="Enter surname").grid(column=1, row=3)
sname = Entry(root, width=10).grid(column=2, row=3)

phonel = Label(root, text="Enter phone").grid(column=1, row=4)
phone = Entry(root, width=10).grid(column=2, row=4)

emaill = Label(root, text="Enter email")
emaill.grid(column=1, row=5)
email = Entry(root, width=10)
email.grid(column=2, row=5)

addressl = Label(root, text="Enter address").grid(column=1, row=6)
address = Entry(root, width=10).grid(column=2, row=6)

saveAdd = Button(root, text="Save Contact").grid(column=2, row=11)
# create contact -- end

phonel = Label(root, text="Contacts").grid(column=1, row=12)

book1 = {}
p1 = Contact("First Name", "Second Name")
book1[p1.get_name_and_surname()] = p1

r = 13

for k, v in book1.items():
    Label(root, text=k).grid(row=r, column=1)
    Button(root, text="View Contact").grid(row=r, column=2)
    r += 1

# class editContact():
# https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/
root.mainloop()
