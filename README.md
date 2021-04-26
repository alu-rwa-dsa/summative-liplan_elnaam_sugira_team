# Contacts Phone Book
## Team Members
* Elnaam Umutoni
* Jules Iradukunda
* Serge Sugira
* Liplan Lekipising
## Data Structure and Algorithm Used
* Linked List
* Simple List
* Dictionary
## Purpose Data Structure and Algorithms Used
**Linked List** :
Used in contacts to represent a contact in a phone book. Holds details such as names, phone, addresses and emails. Operations such as get next node and set next node are implemented to enable actions such as retrieval of contacts details. 

**Simple List** :
Used to store user emails, phones and addresses. A contact may have more than one phone, email or address. The items can be accessed using indexes. Operations such as get the length of a list which gets the number of phones or emails present in a collection.

**Dictionary** : 
Used to store the user contacts. The whole phonebook is represented using a dictionary and the contacts are stored as; key and value which represent name and the contact object respectively. Operations such as searching a contact, getting all contacts and number of contacts present are made possible. 
## Project Description

The phonebook will be used to hold information such as name, phone number, email, and addresses. This project demonstrates the working of a phone book application and data structures like simple lists, linked lists, and dictionaries. The phonebook will have capabilities such as:
Add contact to give our users the ability to add a new contact and provide details such as name, surname, email address, phone number, and address. The phone, address, and email can be more than one and are stored in a list.

Edit contact will enable our users to edit the details saved on a registered contact where there are changes needed.  The following details can be edited; name, surname, email, phone, and address. 

The Get size option will enable our users to get the number of contacts available. 

Delete contacts will enable the user to remove contacts from the phonebook. 

Get details once the user selects this option on any contact it will show all details saved on that contact in the list. 

View all will show all stored contacts in the user’s list. 

Search gives users the option to search for any contact saved. 

Get all emails option will display all emails saved in the contacts. 

Get all phones gives users the ability to get all the present addresses in the phonebook either for one contact or all contacts.

Get all addresses gives the user the ability to get all the present addresses in the phonebook either for one contact or all contacts.
The phonebook will have validations for different fields such as names and email addresses to ensure that they meet specific requirements. 
## Motivation
Nowadays building an application that helps the community to do a specific task in a convenient way is the most important thing. There are a number of reasons why we want to do this program. After observing the current phonebook apps available, we identified that users would like an easy-to-use and efficient app for phonebooks. We want to learn how to build efficient programs and good performance. We also want to get the knowledge on how to design and build data structures that are efficient. We want to build a phonebook which provides more features. Another thing, we have seen that it is not enough for someone to have only names and phone numbers in the phonebook. We aim to build a phonebook that takes more details about the user. 

## Technology Used
* Python 3
* MySQL
* Tkinter

## Project File Structure
* Scripts
    * Details
        * address.py
        * phone.py
        * address_email.py
    * Tests
    * contact.py
    * MainGUI.py
    * MainCLI.py
* contributing.md
* README.md

## Correctness and Efficiency of Algorithms used
### Correctness
#### Email
* get emails  
This method is used to return all emails stored in the email list
Uses a for loop to iterate through the stored emails. 
Tests implemented in the scripts/details/address_email.py file.

* get email  
This method is used to retrieve one email address, it  
takes on parameter, index of email to retrieve. 
Tests implemented in the scripts/details/address_email.py file.

* add email  
This method is used to append or add an email address to the email list.
Tests implemented in the scripts/details/address_email.py file.

* Modify email  
This method is used to edit an email address. Takes two parameters, new email address and the
index of the email to edit. Tests implemented in the scripts/details/address_email.py file.
#### Address 
* get address  
This method is used to retrieve on address and takes one parameter, the index of the 
address to retrieve. Tests implemented in the scripts/details/address.py file.

* get all addresses  
This method is used to get all the store email addresses of a contact. It takes no parameters. Uses 
a for loop. Tests implemented in the scripts/details/address.py file.

* add addresses  
This method is used to add or append an address to the address list. Tests implemented in the scripts/details/address.py file.

* modify address  
This method is used to edit an address. It takes in 2 parameters, new address and the index of 
the address to modify. Tests implemented in the scripts/details/address.py file.
#### Phone
* get phone  
This method is used to return one phone. Takes in one parameter, the index of the phone 
to retrieve. Tests implemented in the scripts/details/phone.py file.

* add phone  
This method is used to append or add a phone to the phone list. Takes no parameters. 
Tests implemented in the scripts/details/phone.py file.

* modify phone  
This method is used to edit a phone in the phone list. Takes in 2 parameters, new phone and the
index of the phone to be replaced. Tests implemented in the scripts/details/phone.py file.

* get all phones  
This method is used to retrieve all the phones available in the phone list. Uses a for
loop. Tests implemented in the scripts/details/phone.py file.
#### Contact
* get all contact details  
This method is used to retrieve all the details about a contact. Returns details, name, 
surname, phone, email and address. Tests implemented in the scripts/contact.py file.


### Analysis
Asymptotic upper bound, O-notation is used to analyze all the algorithms below.

* get emails  
```
def get_emails(self):
        all_emails = [] # O(1)
        for em in self.emailAddresses:
            all_emails.append(em)  # O(N) where N is the size of the list
        return " ".join(all_emails)  # O(1)
```
Time complexity = O(1) + O(N) + O(1) = O(N)  
Space complexity = O(N) - space for the array of emails

* get email  
```
def get_email(self, index=0):
        return self.emailAddresses[index]  # O(1)
```
Time complexity = O(1)  
Space complexity = O(1) - space for the returned email address

* add email  
```
def add_email(self, email):
        self.emailAddresses.append(email)  # O(1)
```
Time complexity = O(1)  
Space complexity = O(1) - space for the email address to be added

* Modify email  
```
def modify_email(self, email, index=0):
        self.emailAddresses[index] = email  # O(1)
```
Time complexity = O(1)  
Space complexity = O(1) - space for the email address to be modified

* get address  
```
def get_address(self, index=0):
        out_address = self.addresses[index]  # O(1)
        return out_address  # O(1)
```
Time complexity = O(1) + O(1) = O(1) 
Space complexity = O(1) - space for the address to be returned

* get all addresses  
```
def get_all_addresses(self):
        all_addresses = []  # O(1)
        for addr in self.addresses:
            all_addresses.append(addr)  # O(N) where N is the size of the address list
        return " ".join(all_addresses)  # O(1)
```
Time complexity = O(1) + O(N) + O(1) = O(N)
Space complexity = O(N) - space for the array of the address

* add addresses  
```
def add_address(self, address):
        self.addresses.append(address)  # O(1)
```
Time complexity = O(1)  
Space complexity = O(1) - space for the address to be added

* modify address  
```
def modify_address(self, address, index=0):
        self.addresses[index] = address  # O(1)
```
Time complexity = O(1)  
Space complexity = O(1) - space for the address to be modified

* get phone  
```
def get_phone(self, index=0):
        return self.phone[index]  # O(1)
```
Time complexity = O(1) 
Space complexity = O(1) - space for the phone to be returned

* add phone  
```
def add_phone(self, phone):
        self.phone.append(phone)  # O(1)
```
Time complexity = O(1)  
Space complexity = O(1) - space for the phone to be added

* modify phone  
```
def modify_phone(self, phone, index=0):
        self.phone[index] = phone  # O(1)
```
Time complexity = O(1)  
Space complexity = O(1) - space for the phone to be modified

* get all phones  
```
def get_all_phones(self):
        all_phones = []  # O(1)
        for phn in self.phone:
            all_phones.append(phn)  # O(N) where N is the size of the phone list
        return " ".join(all_phones)  # O(1)
```
Time complexity = O(1) + O(N) + O(1) = O(N)
Space complexity = O(N) - space for the array of the phones

* get all contact details  
```
def get_all_contact_details(self):
        contact_details = 'Contact details of {} {}: \n'.format(self.first_name, self.surname).upper()  # O(1)
        contact_details += "Phones: " + self.phone.get_all_phones() + "\n" + "Addresses: " + self.address.get_all_addresses() + "\n" + "Emails: " + self.email.get_emails() + "\n"  # O(P) + O(A) + O(E) where P, A and E are phone list size, address list size and email list size respectively
        return contact_details  # O(1)
```
Time complexity = O(1) + O(P) + O(A) + O(E) + O(1) = O(P + A + E)
Space complexity = O(P + A + E) - space for the array of the phones, addresses and emails
## Solution
A phonebook program is a simple program that simulates a contact book. A typical contacts book is used to hold the names of people and their contact details. Contact details can be as simple as phone numbers only or a range of more information such as email addresses and addresses. Our phonebook program is a complete phonebook which has the following five important information:
* Name
* Surname
* Phone
* Email
* Address  

The phone, email, and address are lists that hold multiple elements of the details. The community will benefit from our program in many ways but to mention a few:
* An all-in-one solution for storing multiple details about contact such as email address and addresses. This beats the traditional phonebook, which has only phone numbers.
* It is giving the community a chance to add multiple values to phones, emails, and addresses. This provides the user with the convenience of having all the ways of reaching loved ones or colleagues. 
* Our phonebook program is efficient and reliable. This is enabled by the use of efficient algorithms to save or retrieve values of the contact details. 
* The program also has a simple and intuitive interface for the user to have an easy time interacting with it. 

## Presentation
[Slides Link](https://docs.google.com/presentation/d/17E7tnVS-ozu2IlklyHIKeUmIcT3SUrwLBp_qv3rROAA/edit?usp=sharing)

[Video Link](https://drive.google.com/file/d/1tiKLZLsuKHFesTWX48oMnOA36VXV4b8L/view?usp=sharing)


## How to Setup/Run
Console/CLI - Navigate to the scripts folder of the project and run the mainCLI.py file
GUI - Navigate to the scripts folder of the project and run the mainGUI.py file


## Contributing
Thanks for your interest in contributing! There are many ways to contribute to this project. Open Contributing to read guidelines.


## Bibliography
* docs.python-guide.org. (n.d.). Structuring Your Project — The Hitchhiker’s Guide to Python. [online] Available at: https://docs.python-guide.org/writing/structure/.

* Fliplet. (2017). 13 Features You Should Have in Your Contact Directory App. [online] Available at: https://fliplet.com/2017/01/23/13-features-contact-directory-app/ [Accessed 7 Apr. 2021].

* GeeksforGeeks. (2016). Implement a Phone Directory. [online] Available at: https://www.geeksforgeeks.org/implement-a-phone-directory/ [Accessed 7 Apr. 2021].

* Routledge & CRC Press. (n.d.). A Practical Guide to Data Structures and Algorithms using Java. [online] Available at: https://www.routledge.com/A-Practical-Guide-to-Data-Structures-and-Algorithms-using-Java/Goldman-Goldman/p/book/9781584884552 [Accessed 7 Apr. 2021].

* Sundriyal, M. (2020). Overview: Time & Space Complexity. [online] Medium. Available at: https://medium.com/@manishsundriyal/overview-time-space-complexity-f973513b701e [Accessed 25 Apr. 2021].
‌
* In Out Code. (2019). Big O: How to Calculate Time and Space Complexity. [online] Available at: https://www.inoutcode.com/concepts/big-o/ [Accessed 25 Apr. 2021].
‌
‌
