
from contact import Contact

# create a phonebook
print("""Hello and welcome, lets create a phonebook for you!
Lets first get your details""")

username = input("Whats your name : ")

print("Welcome " + username)

mybook = {}

print("Welcome to the main menu")

while True:
    print("Available actions: \nAdd Contact (1)\nModify Contact (2)\nDelete a contact(3)\nSearch Contact(4)\nView all contacts(5)\nQuit (q)")
    action = input("Choose Option : ")
    if action == "1":
        nm = input("Name : ")
        snm = input("Surname : ")
        phn = input("Phone : ")
        eml = input("Email : ")
        addr = input("Address : ")
        p = Contact(nm, snm)
        p.phone.add_phone(phn)
        p.email.add_email(eml)
        p.address.add_address(addr)
        mybook[nm] = p
        print(p.get_all_contact_details())
    elif action == "2":
        # choose contact
        toModifyName = input("Enter name of contact to modify : ").lower()
        toModifyContact = mybook[toModifyName]
        print("Choose item to edit\nName (1)\nSurname (2)\nPhone (3)\nAddress (4)\nEmail (5)\nQuit (q)")
        toEdit = input("Choose Option : ")
        if toEdit == "1":
            nNm = input("Enter new name : ")
            toModifyContact.edit_name(nNm)
            print("Name modified")
        elif toEdit == "2":
            nSnm = input("Enter new surname : ")
            toModifyContact.edit_surname(nSnm)
            print("Surname modified")
        elif action == "3":
            nPhn = input("Enter new phone : ")
            toModifyContact.get_phone().modify_phone(nPhn)
            print("Phone modified")
        elif action == "4":
            nAddr = input("Enter new address : ")
            toModifyContact.get_address().modify_address(nAddr)
            print("Address modified")
        elif action == "5":
            nEml = input("Enter new email : ")
            toModifyContact.get_email().modify_email(0, nEml)
            print("Email modified")
        elif action == "q" or "Q":
            continue
        else:
            print("Invalid Option!")
    elif action == "3":
        toDeleteName = input("Enter name of contact to delete : ").lower()
        del mybook[toDeleteName]
        print("Contact deleted")
    elif action == "4":
        toSearchName = input("Enter name of contact to delete : ").lower()
        print(mybook[toSearchName].get_all_contact_details())
    elif action == "5":
        for name, contact in mybook.items():
            print(contact.get_all_contact_details())
    elif action == "q" or "Q":
        break
    else:
        print("invalid choice")
        continue
    