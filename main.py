from phonebook import PhoneBook
import csv
import time


# here we will add our contanct information as linkedlist
# def add_all_contact_info(linkedlist):
#     with open("./100-contacts.csv") as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         line_count = 0
#         for row in csv_reader:
#             if line_count == 0:
#                 # skip headers
#                 line_count += 1
#             else:
#                 # add name and surname, cols 1, 2
#                 linkedlist.add_contact(row[0], row[1])
#                 # add address, col 3
#                 linkedlist.find_contacts(row[0], row[1]).Address.add_address(row[3])
#                 # add phones, cols 8, 9
#                 linkedlist.find_contacts(row[0], row[1]).Address.add_phone(row[8])
#                 linkedlist.find_contacts(row[0], row[1]).Address.add_phone(row[9], "Home")
#                 # add email, col 10
#                 linkedlist.find_contacts(row[0], row[1]).Address.add_email(row[10])
#                 # go to next line
#                 line_count += 1

# one contact
person1PhoneBook = PhoneBook()

person1 = person1PhoneBook
person1.add_contact("fdsf", "fdsfsd", "5345345", "ewrwefsd", "rrerwer")
print(person1.print_all_contact_details())
# person1PhoneBook.add_contact("fd", "sa")
# person1PhoneBook.add_contact("ewqe", "wq")
# person1PhoneBook.find_contacts()[0].address.add_address("rdfsdfsd")
# person1PhoneBook.find_contacts()[0].phone.add_phone("r3rdrsdf", "Home")
# person1PhoneBook.find_contacts()[0].email.add_email("fdsfsdf")















