import unittest
from contact import Contact


print()
print("""Hello and welcome, lets create a phonebook for you!
Lets first get your name""")
print()
username = input("Whats your name : ").upper()
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


# check if the phone value entered is valid by checking if it has 10 digits
# Time Complexity :
# Space Complexity : 
# Auxiliary Space :
def validatePhone(value):
    if len(value) != 10:
        return False
    return True


# check if the email is valid by looking for '@' in the input
# Time Complexity :
# Space Complexity : 
# Auxiliary Space :
def validateEmail(value):
    exists = "@" in value
    if exists:
        return True
    return False


# check if the adrress value has more than two characters
# Time Complexity :
# Space Complexity : 
# Auxiliary Space :
def validateAddress(value):
    if len(value) < 2:
        return False
    return True


# main loop - program
while True:
    print()
    print("MAIN MENU: \n(1) Add Contact ||(2) Modify Contact ||(3) Delete a contact ||(4) Search Contact ||(5) View all contacts ||(q) Quit")
    action = input("Choose Option : ")
    print()
    if action == "1":
        print()
        print("ADD CONTACT")
        print()
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
        print()
        print("Details of " + nm.upper() + " saved")
        print()
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
        print("EDIT MENU \nContact selected: " + toModifyName + "\n(1) Name ||(2) Surname ||(3) Phone ||(4) Address ||(5) Email ||(q) Quit")
        toEdit = input("Choose Option : ")
        print()
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
        elif toEdit == "3":
            while True:
                nPhn = input("Enter new phone : ")
                if validatePhone(nPhn) is False:
                    print("Phone should be 10 digits")
                    print()
                    continue
                toModifyContact.get_phone().modify_phone(nPhn)
                print("Phone modified")
                break
        elif toEdit == "4":
            while True:
                nAddr = input("Enter new address : ")
                if validateAddress(nAddr) is False:
                    print("Address should be atleast 2 characters long")
                    print()
                    continue
                toModifyContact.get_address().modify_address(nAddr)
                print("Address modified")
                break
        elif toEdit == "5":
            while True:
                nEml = input("Enter new email : ")
                if validateEmail(nEml) is False:
                    print("Email is invalid")
                    print()
                    continue
                toModifyContact.get_email().modify_email(nEml)
                print("Email modified")
                break
        elif toEdit == "q" or "Q":
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
                print(toDeleteName + " Contact deleted")
                break
            except KeyError:
                print("Name not found, try a different name")
                continue
    elif action == "4":
        while True:
            try:
                toSearchName = input("Enter name : ").lower()
                print()
                print(mybook[toSearchName].get_all_contact_details())
                break
            except KeyError:
                print("Name not found, try a different name ")
                continue
    elif action == "5":
        print(str(len(mybook)) + " contacts found")
        print()
        for name, contact in mybook.items():
            print(contact.get_all_contact_details())
    elif action == "q" or "Q":
        break
    else:
        print("invalid choice")
        print()
    continue


class testMain(unittest.TestCase):
    # test validate - validates correctly
    def testValName(self):
        testContact = Contact("Name", "second")
        self.assertTrue(validatename(testContact.first_name))

    def testValNameWrong(self):
        testContact = Contact("Name", "s")
        self.assertFalse(validatename(testContact.surname))

    def testValPhone(self):
        testContact = Contact("Name", "second")
        testContact.phone.add_phone("1234567890")
        self.assertTrue(validatePhone(
            testContact.get_phone().get_phone()))

    def testValPhoneWrong(self):
        testContact = Contact("Name", "second")
        testContact.phone.add_phone("1234")
        self.assertFalse(validatePhone(
            testContact.get_phone().get_phone()))

    def testValEmail(self):
        testContact = Contact("Name", "second")
        testContact.email.add_email("e@e")
        self.assertTrue(validateEmail(testContact.get_email().get_email()))

    def testValEmailWrong(self):
        testContact = Contact("Name", "second")
        testContact.email.add_email("etdgchggc")
        self.assertFalse(validateEmail(testContact.get_email().get_email()))

    def testValAddress(self):
        testContact = Contact("Name", "second")
        testContact.address.add_address("KGE")
        self.assertTrue(validateAddress(
            testContact.get_address().get_address()))

    def testValAddressWrong(self):
        testContact = Contact("Name", "second")
        testContact.address.add_address("K")
        self.assertFalse(validateAddress(
            testContact.get_address().get_address()))

    # contact is saved with all details
    def testContactName(self):
        book1 = {}
        testContact = Contact("Name", "second")
        testContact.phone.add_phone("1234567890")
        testContact.address.add_address("KGE")
        testContact.email.add_email("e@e")
        book1[testContact.first_name] = testContact
        self.assertEqual(testContact.first_name, "Name")

    def testContactPhone(self):
        book1 = {}
        testContact = Contact("Name", "second")
        testContact.phone.add_phone("1234567890")
        testContact.address.add_address("KGE")
        testContact.email.add_email("e@e")
        book1[testContact.first_name] = testContact
        self.assertEqual(testContact.get_phone(
        ).get_phone(), "1234567890")

    def testContactEmail(self):
        book1 = {}
        testContact = Contact("Name", "second")
        testContact.phone.add_phone("1234567890")
        testContact.address.add_address("KGE")
        testContact.email.add_email("e@e")
        book1[testContact.first_name] = testContact
        self.assertEqual(testContact.get_email().get_email(), "e@e")

    def testContactAddress(self):
        book1 = {}
        testContact = Contact("Name", "second")
        testContact.phone.add_phone("1234567890")
        testContact.address.add_address("KGE")
        testContact.email.add_email("e@e")
        book1[testContact.first_name] = testContact
        self.assertEqual(testContact.get_address().get_address(), "KGE")

    # key in dictionary is first name
    def testContactKey(self):
        book1 = {}
        testContact = Contact("Name", "second")
        book1[testContact.first_name] = testContact
        self.assertEqual(testContact.first_name, book1["Name"].first_name)

    # contact modification is successful
    def testContactModify(self):
        book1 = {}
        testContact = Contact("Name", "second")
        book1[testContact.first_name] = testContact
        book1["Name"].edit_surname("third")
        self.assertNotEqual(book1["Name"].surname, "second")

    # correct contact returned on search
    def testContactSearch(self):
        book1 = {}
        testContact = Contact("Name", "second")
        book1[testContact.first_name] = testContact
        self.assertEqual(book1["Name"], testContact)

    # contact deleted from book successfully
    def testContactDel(self):
        book1 = {}
        testContact = Contact("Name", "second")
        book1[testContact.first_name] = testContact
        del book1["Name"]
        with self.assertRaises(KeyError) as raises:
            book1["name"]


if __name__ == "__main__":
    unittest.main()
