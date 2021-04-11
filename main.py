
from contact import Contact


print()
print("""Hello and welcome, lets create a phonebook for you!
Lets first get your details""")
print()
username = input("Whats your name : ")
print()
print("Welcome " + username)

# create a phonebook
mybook = {}
print()
print("Welcome to the main menu")


# we check if th value entered is a string and not number
def validatename(value):
    if len(value) < 2 or value.isalpha() is False:
        return False
    return True


# we check if the phone value entered is valid by checking if it has 10 digits
def validatePhone(value):
    if len(value) != 10:
        return False
    return True


# here we check if the email is valid by looking for '@' in the input
def validateEmail(value):
    exists = "@" in value
    if exists:
        return True
    return False


# we check if the adrress value has more than two characters
def validateAddress(value):
    if len(value) < 2:
        return False
    return True


# main loop - program
while True:
    print()
    print("MAIN MENU: \n(1) -> Add Contact (2) -> Modify Contact (3) -> Delete a contact (4) -> Search Contact (5) -> View all contacts (q) -> Quit")
    action = input("Choose Option : ")
    print()
    if action == "1":
        while True:
            nm = input("Name : ")
            if validatename(nm) is False:
                print("Name should be atleast 2 characters long and not integers")
                print()
                continue
            break

        while True:
            snm = input("Surname : ")
            if validatename(snm) is False:
                print("Surname should be atleast 2 characters long and not integers")
                print()
                continue
            break

        while True:
            phn = input("Phone : ")
            if validatePhone(phn) is False:
                print("Phone should be 10 digits")
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

        # create the contact
        p = Contact(nm, snm)
        p.phone.add_phone(phn)
        p.email.add_email(eml)
        p.address.add_address(addr)
        mybook[nm] = p
        # Show details
        print(p.get_all_contact_details())
    elif action == "2":
        # choose contact
        print()
        while True:
            try:
                toModifyName = input(
                    "Enter name of contact to modify : ").lower()
                toModifyContact = mybook[toModifyName]
            except KeyError:
                print("No result, try a different name")
                continue
            break
        print()
        print("Choose item to edit\n(1) -> Name (2) -> Surname (3) -> Phone (4) -> Address (5) -> Email (q) -> Quit")
        toEdit = input("Choose Option : ")
        if toEdit == "1":
            while True:
                nNm = input("Enter new name : ")
                if validatename(nNm) is False:
                    print("Name should be atleast 2 characters long and not integers")
                    print()
                    continue
                toModifyContact.edit_name(nNm)
                print("Name modified")
                break
        elif toEdit == "2":
            while True:
                nSnm = input("Enter new surname : ")
                if validatename(nSnm) is False:
                    print(
                        "Surname should be atleast 2 characters long and not integers")
                    print()
                    continue
                toModifyContact.edit_surname(nSnm)
                print("Surname modified")
                break
        elif action == "3":
            while True:
                nPhn = input("Enter new phone : ")
                if validatePhone(nPhn) is False:
                    print("Phone should be 10 digits")
                    print()
                    continue
                toModifyContact.get_phone().modify_phone(nPhn)
                print("Phone modified")
                break
        elif action == "4":
            while True:
                nAddr = input("Enter new address : ")
                if validateAddress(nAddr) is False:
                    print("Address should be atleast 2 characters long")
                    print()
                    continue
                toModifyContact.get_address().modify_address(nAddr)
                print("Address modified")
                break
        elif action == "5":
            while True:
                nEml = input("Enter new email : ")
                if validateEmail(nEml) is False:
                    print("Email is invalid")
                    print()
                    continue
                toModifyContact.get_email().modify_email(0, nEml)
                print("Email modified")
                break
        elif action == "q" or "Q":
            continue
        else:
            print("Invalid Option!")
            break
    elif action == "3":
        while True:
            try:
                toDeleteName = input(
                    "Enter name of contact to delete : ").lower()
                del mybook[toDeleteName]
                print("Contact deleted")
                break
            except KeyError:
                print("Name not found, try a different name")
                continue
    elif action == "4":
        while True:
            try:
                toSearchName = input("Enter name : ").lower()
                print(mybook[toSearchName].get_all_contact_details())
                break
            except KeyError:
                print("Name not found, try a different name ")
                continue
    elif action == "5":
        for name, contact in mybook.items():
            print(contact.get_all_contact_details())
    elif action == "q" or "Q":
        break
    else:
        print("invalid choice")
        print()
    continue
