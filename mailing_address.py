class MailingAddress:
    def __init__(self, street_address, city, state, zip_code, address_type): #intializing the constructure 
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__address_type = address_type



    def set_street_address(self, street_address): #setting street address
        self.__street_address = street_address

    def set_city(self, city): #setting city
        self.__city = city

    def set_state(self, state): #setting state
        self.__state = state

    def set_zip_code(self, zip_code): #setting zip code
        self.__zip_code = zip_code

    def set_address_type(self, address_type): #setting address type
        self.__address_type = address_type



    def get_street_address(self): #getting street addres
        return self.__street_address

    def get_city(self): #getting city
        return self.__city

    def get_state(self): #getting state
        return self.__state

    def get_zip_code(self): #gettting zip
        return self.__zip_code


    def get_address_type(self): #getting address type
        return self.__address_type



    def __str__(self): #calling __str__ method to format address output 
        return f"{self.__street_address}, {self.__city}, {self.__state}, {self.__zip_code} ({self.__address_type})"