import unittest


class Email:
    def __init__(self):
        self.emailAddresses = []
    # we create a functiom to get email

    def get_emails(self):
        if len(self.emailAddresses) > 0:
            emails = "E-mail addresses:\n" + "\n".join(self.emailAddresses)
            return emails
        else:
            return ""

    def get_email(self, index=0):
        return self.emailAddresses[index]

    def add_email(self, email):
        self.emailAddresses.append(email)

    def modify_email(self, index, email):
        self.emailAddresses[index] = email


class testEmail(unittest.TestCase):
    # functions
    def testadd(self):
        email = Email()
        email.add_email("test@mail")
        self.assertEqual(email.get_email(0), "test@mail")
    # more functions


if __name__ == "__main__":
    unittest.main()
