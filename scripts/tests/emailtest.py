import unittest
from details.address_email import Email


class testEmail(unittest.TestCase):
    # functions
    def testadd(self):
        email = Email()
        email.add_email("test@mail")
        self.assertEqual(email.get_email(0), "test@mail")


if __name__ == "__main__":
    unittest.main()
