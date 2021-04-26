
from details.phone import Phone
from details.address import Address
from details.address_email import Email
import unittest


# here we need to create for contact details
class Contact:
    def __init__(self, firstname, surname, n=None):
        self.first_name = firstname
        self.surname = surname
        self.phone = Phone()
        self.address = Address()
        self.email = Email()
        self.next_node = n

    def get_next(self):
        return self.nextNode

    def set_next(self, n):
        self.next_node = n

    def set_first_name(self, name):
        self.first_name = name

    def get_all_contact_details(self):
        contact_details = 'Contact details of {} {}: \n'.format(
            self.first_name, self.surname).upper()
        contact_details += "Phones: " + self.phone.get_all_phones() + "\n" + "Addresses: " + \
            self.address.get_all_addresses() + "\n" + "Emails: " + \
            self.email.get_emails() + "\n"
        return contact_details

    def get_name_and_surname(self):
        if self.surname != "":
            return "{} {}".format(self.first_name, self.surname)
        return self.first_name

    def set_surname(self, surname):
        self.surname = surname

    def edit_name(self, new_name):
        self.first_name = new_name

    def edit_surname(self, new_surname):
        self.surname = new_surname

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email


class testContact(unittest.TestCase):
    # test set details - name, sname, phone, address and email
    # test first name
    def testName(self):
        testContact = Contact("Name", "Second")
        self.assertEqual(testContact.first_name, "Name")

    def testNameWrong(self):
        testContact = Contact("Name", "Second")
        self.assertNotEqual(testContact.first_name, "James")

    def testNameString(self):
        testContact = Contact("Name", "Second")
        self.assertTrue(isinstance(testContact.first_name, str))

    def testNameWrong(self):
        testContact = Contact("Name", "Second")
        self.assertIsNotNone(testContact.first_name)

    # test surname
    def testSname(self):
        testContact = Contact("Name", "second")
        self.assertEqual(testContact.surname, "second")

    def testSnameWrong(self):
        testContact = Contact("Name", "second")
        self.assertNotEqual(testContact.surname, "James")

    def testSnameString(self):
        testContact = Contact("Name", "second")
        self.assertTrue(isinstance(testContact.surname, str))

    def testSnameWrong(self):
        testContact = Contact("Name", "second")
        self.assertIsNotNone(testContact.surname)

    # test phone
    def testPhone(self):
        testContact = Contact("Name", "second")
        testContact.phone.add_phone("1234567890")
        self.assertEqual(testContact.get_phone().get_phone(), "1234567890")

    def testWrongPhone(self):
        testContact = Contact("Name", "second")
        testContact.phone.add_phone("1234567890")
        self.assertNotEqual(testContact.get_phone().get_phone(), "9")

    def testNonePhone(self):
        testContact = Contact("Name", "second")
        testContact.phone.add_phone("1234567890")
        self.assertIsNotNone(testContact.get_phone().get_phone())

    # test phone
    def testAddress(self):
        testContact = Contact("Name", "second")
        testContact.address.add_address("KF")
        self.assertEqual(testContact.get_address().get_address(), "KF")

    def testWrongAddress(self):
        testContact = Contact("Name", "second")
        testContact.address.add_address("KF")
        self.assertNotEqual(testContact.get_address().get_address(), "K")

    def testNoneAddress(self):
        testContact = Contact("Name", "second")
        testContact.address.add_address("KF")
        self.assertIsNotNone(testContact.get_address().get_address())

    # test email
    def testEmail(self):
        testContact = Contact("Name", "second")
        testContact.email.add_email("ke")
        self.assertEqual(testContact.get_email().get_email(), "ke")

    def testWrongEmail(self):
        testContact = Contact("Name", "second")
        testContact.email.add_email("ke")
        self.assertNotEqual(testContact.get_email().get_email(), "k")

    def testNoneEmail(self):
        testContact = Contact("Name", "second")
        testContact.email.add_email("ke")
        self.assertIsNotNone(testContact.get_email().get_email())

    # test edits
    def testEditName(self):
        testContact = Contact("Name", "second")
        testContact.edit_name("new")
        self.assertEqual(testContact.first_name, "new")

    def testEditPhone(self):
        testContact = Contact("Name", "second")
        testContact.phone.add_phone("10")
        testContact.phone.modify_phone("01")
        self.assertEqual(testContact.phone.get_phone(), "01")


if __name__ == "__main__":
    unittest.main()
