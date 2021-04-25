import unittest


class Phone:
    # init for the phone numbers
    def __init__(self):
        self.phone = []

    # retrieve a phone
    def get_phone(self, index=0):
        return self.phone[index]

    # add a phone
    def add_phone(self, phone):
        self.phone.append(phone)

    def modify_phone(self, phone, index=0):
        self.phone[index] = phone

    def get_all_phones(self):
        all_phones = []
        for phn in self.phone:
            all_phones.append(phn)
        return " ".join(all_phones)


class testPhone(unittest.TestCase):
    # correct Phone saved
    def testadd(self):
        phone = Phone()
        phone.add_phone("1234567890")
        self.assertEqual(phone.get_phone(), "1234567890")
    
    # saved phone not wrong
    def testaddWrong(self):
        phone = Phone()
        phone.add_phone("1234567890")
        self.assertNotEqual(phone.get_phone(), "")
    
    # correct instance saved
    def testPhoneType(self):
        phone = Phone()
        phone.add_phone("1234567890")
        self.assertIsInstance(phone.get_phone(), str)
    
    # saved type is not int
    def testPhoneTypeWrong(self):
        phone = Phone()
        phone.add_phone("1234567890")
        self.assertNotIsInstance(phone.get_phone(), int)
    
    # modify works correctly
    def testPhoneModify(self):
        phone = Phone()
        phone.add_phone("1234567890")
        phone.modify_phone("0987654321")
        self.assertEqual(phone.get_phone(), "0987654321")
    
    # returns all phones
    def testPhoneAll(self):
        phone = Phone()
        phone.add_phone("0987654321")
        phone.add_phone("1234567890")
        self.assertEqual(phone.get_all_phones(), "0987654321 1234567890")


if __name__ == "__main__":
    unittest.main()

