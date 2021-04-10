
from typing import cast
from contact import Contact

# create a phonebook
print()
print("""Hello and welcome, lets create a phonebook for you!
Lets first get your details""")
print()
username = input("Whats your name : ")
print()
print("Welcome " + username)

mybook = {}
print()
print("Welcome to the main menu")


# to do :
# - validations for modify contact - Elnaam - Ensure that no integers are entered for string fields - name, sname, email
# - Edit the validations for add contact - Ensure that no integers are entered for string fields - Jules
# - Try except in action 4 - Serge
# - add created date field in contact - main, contact file - record today's date - Serge


# git fetch
# checkout to exploratory branch
# git pull
# open the code in IDE/editor
# git checkout -b mybranch
# make your changes
# git add .
# git commit -m
# git push

def validateName(value):
    if len(value) < 2:
        return False
    return True


def validateSname(value):
    if len(value) < 2:
        return False
    return True


def validatePhone(value):
    if len(value) != 10:
        return False
    return True


def validateEmail(value):
    exists = "@" in value
    if exists:
        return True
    return False


def validateAddress(value):
    if len(value) < 2:
        return False
    return True


while True:
    print()
    print("MAIN MENU: \nAdd Contact (1) Modify Contact (2) Delete a contact(3) Search Contact(4) View all contacts(5) Quit (q)")
    action = input("Choose Option : ")
    print()
    if action == "1":
        while True:
            nm = input("Name : ")
            if validateName(nm) is False:
                print("Name should be atleast 2 characters long")
                print()
                continue
            break

        while True:
            snm = input("Surname : ")
            if validateSname(snm) is False:
                print("Surname should be atleast 2 characters long")
                print()
                continue
            break

        while True:
            phn = input("Phone : ")
            if validatePhone(phn) is False:
                print("Phone should have 10 integers")
                print()
                continue
            break

        while True:
            eml = input("Email : ")
            if validateEmail(eml) is False:
                print("Email is invalid")
                print()
                continue
            break

        while True:
            addr = input("Address : ")
            if validateAddress(addr) is False:
                print("Address should be atleast 2 characters long")
                print()
                continue
            break

        p = Contact(nm, snm)
        p.phone.add_phone(phn)
        p.email.add_email(eml)
        p.address.add_address(addr)
        mybook[nm] = p
        print(p.get_all_contact_details())
    elif action == "2":
        # choose contact
        print()
        while True:
            try:
                toModifyName = input("Enter name of contact to modify : ").lower()
                toModifyContact = mybook[toModifyName]
            except KeyError:
                print("No result, try a different name")
                continue
            break
        print()
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
        toSearchName = input("Enter name : ").lower()
        print(mybook[toSearchName].get_all_contact_details())
    elif action == "5":
        for name, contact in mybook.items():
            print(contact.get_all_contact_details())
    elif action == "q" or "Q":
        break
    else:
        print("invalid choice")
        print()
        continue
    continue
