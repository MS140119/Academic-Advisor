class Course:
    def __init__(self, course_num, semester_taken, delivery_meth, status, grade):
        self.__course_num = course_num
        self.__semester_taken = semester_taken
        self.__delivery_meth = delivery_meth
        self.__status = status
        self.__grade = grade

    def set_course_num (self, course_num):
        self.__course_num = course_num

    def set_semester(self, semester_taken):
        self.__semester_taken = semester_taken

    def set_delivery_meth(self, deliver_method):
        self.__delivery_meth = deliver_method

    def set_status(self, status):
        self.__status = status

    def set_grade(self, grade):
        self.__grade = grade



    def get_course_num(self):
        return self.__course_num
    
    def get_semester_taken(self):
        return self.__semester_taken
    
    def get_delivery_meth(self):
        return self.__delivery_meth
    
    def get_grade(self):
        return self.__status
    
    def get_grade(self):
        return self.__grade
    


    def __str__(self):
        return (
        f"Course: {self.__course_num}\n"
        f"Semester: {self.__semester_taken}\n"
        f"Delivery method: {self.__delivery_meth}\n"
        f"Status: {self.__status}\n"
        f"Grade: {self.__grade}\n"
    )