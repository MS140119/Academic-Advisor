class PhoneNumber:
    def __init__(self, phone_number, phone_type): #intializing phone constructure 
        self.__phone_number = phone_number
        self.__phone_type = phone_type



    def set_phone_number(self, phone_number): #setting phone number
        self.__phone_number = phone_number

    def set_phone_type(self, phone_type): #setting phone type
        self.__phone_type = phone_type



    def get_phone_number(self): #getting phone number
        return self.__phone_number

    def get_phone_type(self): #getting phone type
        return self.__phone_type
    
    

    def __str__(self): #intializing __str__ to ouput proper output
        return f'{self.__phone_number}, {self.__phone_type}'
    