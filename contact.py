from phone import Phone
from address import Address
from address_email import Email

# here we need to create for contact details


class Contact:
    def __init__(self, name, surname="", n=None):
        self.first_name = name
        self.surname = surname
        self.phone = Phone()
        self.address = Address()
        self.email = Email()
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def set_first_name(self, name):
        self.first_name = name

    def get_all_contact_details(self):
        contact_info = 'Contact details of {} {}: \n'.format(self.first_name, self.surname)
        contact_info += self.phone.get_all_phones() + "\n" + self.address.get_all_addresses() + "\n" + self.email.get_emails() + "\n"
        return contact_info

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
