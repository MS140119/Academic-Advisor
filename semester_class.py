class Semester:
    def __init__(self, semester, year): #intializing semester constructure 
        self.__semester = semester
        self.__year = year



    def set_semester(self, semester): #setting semester
        self.__semester = semester

    def set_year(self, year): #setting year
        self.__year = year



    def get_semester(self): #getting semester
        return self.__semester

    def get_year(self): #getting year
        return self.__year



    def __str__(self): #calling __str__ method to display semester and year
        return f'{self.__semester}, {self.__year}'
