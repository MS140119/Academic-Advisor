class Email:
    def __init__(self, email_address, email_type): #intializing email constructure 
        self.__email_address = email_address
        self.__email_type = email_type



    def set_email_address(self, email_address): #setting email address
        self.__email_address = email_address

    def set_email_type(self, email_type): #setting email type
        self.__email_type = email_type



    def get_email_address(self): #getting email address
        return self.__email_address

    def get_email_type(self): #getting email type
        return self.__email_type



    def __str__(self): #intializing __str__ to ouput proper output
        return f"{self.__email_address} ({self.__email_type})"
