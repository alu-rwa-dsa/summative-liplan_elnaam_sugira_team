import unittest


class Email:
    def __init__(self):
        self.emailAddresses = []

    def get_emails(self):
        all_emails = []
        for em in self.emailAddresses:
            all_emails.append(em)
        return " ".join(all_emails)

    def get_email(self, index=0):
        return self.emailAddresses[index]

    def add_email(self, email):
        self.emailAddresses.append(email)

    def modify_email(self, email, index=0):
        self.emailAddresses[index] = email


class testEmail(unittest.TestCase):
    # correct email saved
    def testadd(self):
        email = Email()
        email.add_email("test@mail")
        self.assertEqual(email.get_email(), "test@mail")

    # saved email not wrong
    def testaddWrong(self):
        email = Email()
        email.add_email("test@mail")
        self.assertNotEqual(email.get_email(), "")

    # correct instance saved
    def testEmailType(self):
        email = Email()
        email.add_email("test@mail")
        self.assertIsInstance(email.get_email(), str)

    # saved type is not int
    def testEmailTypeWrong(self):
        email = Email()
        email.add_email("test@mail")
        self.assertNotIsInstance(email.get_email(), int)

    # modify works correctly
    def testEmailModify(self):
        email = Email()
        email.add_email("test@mail")
        email.modify_email("new@new")
        self.assertEqual(email.get_email(), "new@new")

    # returns all emails
    def testEmailAll(self):
        email = Email()
        email.add_email("test@mail")
        email.add_email("another@mail")
        self.assertEqual(email.get_emails(), "test@mail another@mail")


if __name__ == "__main__":
    unittest.main()
