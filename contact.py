from phone import Phone
from address import Address
from address import Email

# here we need to create for contact details
class Contact:
    def __init__(self, firstname, surname="", n=None):
        self.first_name = firstname
        self.surname = surname
        self.phone = Phone()
        self.address = Address()
        self.email_address = Email()
        self.nextNode = n

    def get_next(self):
        return self.nextNode

    def set_next(self, n):
        self.nextNode = n
#function to get all contact details
    def get_all_contact_details(self):
        info = 'Phone details of {} {}: \n'.format(self.first_name, self.surname)
        info += self.phone.get_all_phones() + "\n" + self.address.get_all_addresses() + "\n" + \
                        self.email_address.get_emails()
        return info
#this function will return the firstname and surname if surname is not empty or retur only firstaname if the surname is null 
    def get_name_and_surname(self):
        if self.surname != "":
            return "{} {}".format(self.first_name, self.surname)
        return self.first_name
#functionto add a surname
    def set_surname(self, surname):
        self.surname = surname
# edit the the previous name and set the new one
    def edit_name(self, newName):
        self.first_name = newName
#edit  the previous surename and set the new one
    def edit_surname(self, newSurname):
        self.surname = newSurname
