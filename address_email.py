#we create the email class
class Email:
    def __init__(self):
        self.emailAdresses = []
#we create a functiom to get email
    def get_emails(self):
        if len(self.emailAdresses) > 0:
            emails = "E-mail addresses:\n" + "\n".join(self.emailAdresses)
            return emails
        else:
            return ""
#we cre
    def get_email(self, index=0):
        return self.emailAdresses[index]

    def add_email(self, email):
        self.emailAdresses.append(email)

    def modify_email(self, index, email):
        self.emailAdresses[index] = email
