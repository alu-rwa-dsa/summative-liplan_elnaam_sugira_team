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
        return self.phones

    def get_email(self):
        return self.email


# create contact - names
p1 = Contact("C", "one")
# add contacts details - phone, address, email
p1.address.add_address("address")
p1.phone.add_phone("phone")
p1.email.add_email("email")
# view all details of a contact
# print(p1.get_all_contact_details())
# view name
print(p1.get_name_and_surname())
# view phones
print(p1.get_address().get_all_addresses())
# view email
print(p1.get_email().get_emails())
# view address
print(p1.get_address().get_all_addresses())
# edit name
p1.edit_name("contact")
p1.edit_surname("twoo")
# edit phone
p1.phone.modify_phone("32423")
# edit email
p1.email.modify_email(0, "rsfsdfs")
# edit address
p1.address.modify_address("dsadas")

# add contact to a dictionary
book1 = {}
book1["p1"] = p1

# remove contact
# del book1["p1"]

# view all contacts

for k, v in book1.items():
    print(v.get_name_and_surname())
