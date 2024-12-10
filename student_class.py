from linked_list import LinkedList
from mailing_address import MailingAddress
from date import Date
from email import Email
from phone_number import PhoneNumber
from semester_class import Semester

class Student:
    def __init__(self, first_name, middle_name, last_name, student_id, mailing_address, emails, phone_numbers, birth_date, acceptance_date, start_semester, intended_major): #intializing Student constructure 
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__student_id = student_id
        self.__mailing_address = mailing_address
        self.__emails = emails
        self.__phone_numbers = phone_numbers
        self.__birth_date = birth_date
        self.__acceptance_date = acceptance_date
        self.__start_semester = start_semester
        self.__intended_major = intended_major
        self.__courses = LinkedList()

    def add_course(self, course):       
        self.__courses.add(course)
        print(f"Course {course.get_course_num()} added.")

    def remove_course(self, course_num):
        current = self.__courses.head
        while current:
            if current.data.get_course_num() == course_num:
                self.__courses.remove(course_num)
                print(f"Course {course_num} removed.")
                return
            current = current.next
        print(f"Course {course_num} not found.")

    def get_all_courses(self):
        return str(self.__courses)


    def set_first_name(self, first_name): #setting first name
        self.__first_name = first_name

    def set_middle_name(self, middle_name): #setting middle name
        self.__middle_name = middle_name

    def set_last_name(self, last_name): #setting last name
        self.__last_name = last_name

    def set_student_id(self, student_id): #setting student id
        self.__student_id = student_id

    def set_mailing_address(self, mailing_address): #setting mailing address class
        self.__mailing_address = mailing_address

    def set_emails(self, emails): #setting email class
        self.__emails = emails

    def set_phone_numbers(self, phone_numbers): #setting phone_number class
        self.__phone_numbers = phone_numbers

    def set_birth_date(self, birth_date): #setting birth day
        self.__birth_date = birth_date

    def set_acceptance_date(self, acceptance_date): #setting acceptance date
        self.__acceptance_date = acceptance_date

    def set_start_semester(self, start_semester): #setting semester start
        self.__start_semester = start_semester

    def set_intended_major(self, intended_major): #setting intended major
        self.__intended_major = intended_major




    def get_first_name(self): #getting first
        return self.__first_name

    def get_middle_name(self): #getting middle name
        return self.__middle_name

    def get_last_name(self): #getting last name
        return self.__last_name

    def get_student_id(self): #getting student id
        return self.__student_id

    def get_mailing_address(self): #getting mailing address
        return self.__mailing_address

    def get_emails(self): #getting email
        return self.__emails

    def get_phone_numbers(self): #getting phone number
        return self.__phone_numbers

    def get_birth_date(self): #getting birth date
        return self.__birth_date

    def get_acceptance_date(self): #getting acceptance date
        return self.__acceptance_date

    def get_start_semester(self): #getting starting semester
        return self.__start_semester

    def get_intended_major(self): #getting intended major
        return self.__intended_major




    def display_student_info(self): #displaying student information in specific format 
        print("Student Information:")
        print(f"Name: {self.__first_name} {self.__middle_name} {self.__last_name}")
        print(f"Student ID: {self.__student_id}")
        print(f"Mailing Address: {self.__mailing_address}")
        print("Emails:")
        for email in self.__emails:
            print(f" - {email}")
        print("Phone Numbers:")
        for phone in self.__phone_numbers:
            print(f" -{str(phone)}")
        print(f"Birth Date: {self.__birth_date}")
        print(f"Acceptance Date: {self.__acceptance_date}")
        print(f"Start Semester: {self.__start_semester}")
        print(f"Intended Major: {self.__intended_major}")



    def __str__(self): #Display student details along with courses
        return (
        f"Student:\n"
        f"Name: {self.__first_name} {self.__middle_name} {self.__last_name}\n"
        f"ID: {self.__student_id}\n"
        f"Intended Major: {self.__intended_major}\n"
        f"Courses:\n{self.get_all_courses()}"
    )



