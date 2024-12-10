from linked_list import LinkedList

class Advisor:
    def __init__(self, first_name, middle_name, last_name, title, department):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__title = title
        self.__department = department
        self.__advisees = LinkedList()

    def add_advisee(self, student): #adds a student to the linked list of the advisees
        self.__advisees.add(student)
    
    def remove_advisees(self, student_id): #removes the student from the linked list by there ID's
        if self.__advisees.remove(student_id):
            print(f'Advisee with ID {student_id} has been removed.')
        else:
            print(f'Sorry but no advisee with ID {student_id} has been found.')

    def set_first_name(self,first_name):
        self.__first_name = first_name
    
    def set_middle_name(self, middle_name):
        self.__middle_name = middle_name
    
    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_title(self, title):
        self.__title = title

    def set_department(self, department):
        self.__department = department

    
    def get_first_name(self):
        return self.__first_name

    def get_middle_name(self):
        return self.__middle_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_title(self):
        return self.__title
    
    def get_department(self):
        return self.__department
    

    def __str__(self):
        return (
        f"Advisor:\n"
        f"First name: {self.__first_name}\n"
        f"Middle name: {self.__middle_name}\n"
        f"Last name: {self.__last_name}\n"
        f"Title: {self.__title}\n"
        f"Department: {self.__department}\n"
    )