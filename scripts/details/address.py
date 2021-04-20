import unittest


class Address:
    def __init__(self):
        self.addresses = []

    # Time Complexity :
    # Space Complexity :
    # Auxiliary Space :
    def get_address(self, index=0):
        out_address = self.addresses[index]
        return out_address

    # Time Complexity :
    # Space Complexity :
    # Auxiliary Space :
    def get_all_addresses(self):
        all_addresses = []
        for addr in self.addresses:
            all_addresses.append(addr)
        return " ".join(all_addresses)

    # Time Complexity :
    # Space Complexity :
    # Auxiliary Space :
    def add_address(self, address):
        self.addresses.append(address)

    # Time Complexity :
    # Space Complexity :
    # Auxiliary Space :
    def modify_address(self, address, index=0):
        self.addresses[index] = address


class testAddress(unittest.TestCase):
    # add correct address
    def testAddAddress(self):
        testAddresses = Address()
        testAddresses.add_address("KHHE")
        self.assertEqual(testAddresses.get_address(), "KHHE")
    
    # wrong address
    def testAddAddressWrong(self):
        testAddresses = Address()
        testAddresses.add_address("KHHE")
        self.assertNotEqual(testAddresses.get_address(), "ke")
    
    # returns correct address type
    def testAddAddressGet(self):
        testAddresses = Address()
        testAddresses.add_address("KHHE")
        self.assertIsInstance(testAddresses.get_address(), str)

    # does not return address
    def testAddAddressGetWrong(self):
        testAddresses = Address()
        testAddresses.add_address("KHHE")
        self.assertNotIsInstance(testAddresses.get_address(), int)
    
    # get all addresses
    def testAddAddress(self):
        testAddresses = Address()
        testAddresses.add_address("KHHE")
        testAddresses.add_address("another")
        self.assertEqual(testAddresses.get_all_addresses(), "KHHE another")
    
    # modify contact
    def testAddAddressModify(self):
        testAddresses = Address()
        testAddresses.add_address("KHHE")
        testAddresses.modify_address("new")
        self.assertEqual(testAddresses.get_address(), "new")
    

if __name__ == "__main__":
    unittest.main()