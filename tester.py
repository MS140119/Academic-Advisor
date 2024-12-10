from advisor import Advisor
from course import Course
from mailing_address import MailingAddress
from date import Date
from email import Email
from phone_number import PhoneNumber
from semester_class import Semester
from student_class import Student
from node import Node

def create_student():
    # Get basic information from the user
    first_name = input("Enter first name: ")
    middle_name = input("Enter middle name: ")
    last_name = input("Enter last name: ")
    student_id = input("Enter student ID: ")

    # Create mailing address
    street = input("Enter street address: ")
    city = input("Enter city: ")
    state = input("Enter state: ")

    # Zip Code with integer validation
    while True:
        try:
            zip_code = int(input("Enter zip code: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric zip code.")

    address_type = input("Enter address type (home/school): ")
    mailing_address = MailingAddress(street, city, state, zip_code, address_type)

    # Collect emails
    emails = []
    while True:
        email_address = input("Enter email address (or 'done' to finish): ")
        if email_address.lower() == "done":
            break
        email_type = input("Enter email type (e.g., personal, school): ")
        emails.append(Email(email_address, email_type))

    # Collect phone numbers
    phone_numbers = []
    while True:
        phone_number = input("Enter phone number (or 'done' to finish): ").strip()
        if phone_number.lower() == "done":
            break
        try:
            # Validate input by attempting to strip invalid characters
            cleaned_number = "".join([char for char in phone_number if char.isdigit() or char in "+-() "])
            if not cleaned_number:
                raise ValueError("Phone number must contain digits.")
            
            phone_type = input("Enter phone type (e.g., mobile, home): ").strip()
            phone_numbers.append(PhoneNumber(phone_number, phone_type))
            print("Phone number added successfully.")
        except ValueError as e:
            print(f"Invalid input: {e}")

    # Date of birth with integer validation
    while True:
        try:
            birth_day = int(input("Enter day of birth: "))
            birth_month = int(input("Enter birth month: "))
            birth_year = int(input("Enter birth year: "))
            birth_date = Date(birth_day, birth_month, birth_year)
            break
        except ValueError:
            print("Invalid input. Please enter numeric values for the date of birth.")

    # Acceptance date with integer validation
    while True:
        try:
            acceptance_day = int(input("Enter acceptance day: "))
            acceptance_month = int(input("Enter acceptance month: "))
            acceptance_year = int(input("Enter acceptance year: "))
            acceptance_date = Date(acceptance_day, acceptance_month, acceptance_year)
            break
        except ValueError:
            print("Invalid input. Please enter numeric values for the acceptance date.")

    # Start semester year with integer validation
    semester_name = input("Enter start semester (e.g., Fall): ")
    while True:
        try:
            semester_year = int(input("Enter start semester year: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric year.")

    start_semester = Semester(semester_name, semester_year)
    intended_major = input("Enter intended major: ")

    # Create and return the Student instance
    return Student(
        first_name, middle_name, last_name, student_id, mailing_address,
        emails, phone_numbers, birth_date, acceptance_date, start_semester,
        intended_major)






def edit_student(student):
    # Edit student details
    print("\nEditing student information. Leave field blank to keep current value.\n")

    first_name = input(f"Enter first name [{student.get_first_name()}]: ") or student.get_first_name()
    middle_name = input(f"Enter middle name [{student.get_middle_name()}]: ") or student.get_middle_name()
    last_name = input(f"Enter last name [{student.get_last_name()}]: ") or student.get_last_name()
    student_id = input(f"Enter student ID [{student.get_student_id()}]: ") or student.get_student_id()

    # Assuming the methods below exist in the Student class to get and set mailing addresses and phone numbers
    mailing_address = input(f"Enter mailing address [{student.get_mailing_address()}]: ") or student.get_mailing_address()
    phone_number = input(f"Enter phone number [{student.get_phone_numbers()}]: ") or student.get_phone_numbers()

    # Update values in the student object
    student.set_first_name(first_name)
    student.set_middle_name(middle_name)
    student.set_last_name(last_name)
    student.set_student_id(student_id)
    student.set_mailing_address(mailing_address)
    student.set_phone_numbers(phone_number)





def display_student(student):
    # Display student information using a method in the Student class
    student.display_student_info()






def edit_menu():
    print('a. Edit Student information')
    print('b. Student Mailing Address')
    print('c. Student contact information')
    print('d. Exit menu')





def menu():
    print("\n--- Student Management Menu ---")
    print("a. Add a new student")
    print("b. Edit an existing student")
    print("c. Delete a student")
    print("d. Display a student's information")
    print('e. Manage Advisor (add/remove/display)') #Managing advisor
    print("f. Manage courses") #Managing courses
    print('g. Exit. Thank you!')



def main():
    #Creating a instance below
    advisor = Advisor('Mohammad', 'A', 'Hoque', 'Professor', 'CS')
    
    
    students = {
        "S001": Student(
            "Mark", "A", "Frank", "S001",
            MailingAddress("123 Apple St", "Philadelphia", "Pa", 19008, "home"),
            [Email("frank.bob@gmail.com", "personal")],
            [PhoneNumber("123-456-7890", "mobile")],
            Date(1, 1, 2000),
            Date(8, 15, 2022),
            Semester("Fall", 2022),
            "Computer Science"
        ),
        "S002": Student(
            "Jane", "B", "Smith", "S002",
            MailingAddress("456 Oak St", "Springfield", "IL", 62705, "home"),
            [Email("jane.smith@gmail.com", "personal"), Email("jane.smith@psu.edu", "school")],
            [PhoneNumber("123-555-5678", "home")],
            Date(12, 31, 1999),
            Date(8, 15, 2021),
            Semester("Fall", 2021),
            "Biology"
        )
    }

    while True:
        menu()  # Display the menu options to the user

        # Get the user's choice and convert it to lowercase for consistency
        choice = input("Choose an option: ").lower()

        # Option 'a': Add a new student
        if choice == 'a':
            while True:
                try:
                    new_student = create_student()  # Call the function to create a new student
                    student_id = new_student.get_student_id()  # Retrieve the student ID
                    
                    # Check if the student ID already exists
                    if student_id in students:
                        print("Error: A student with this ID already exists. This student was not added.")
                    else:
                        # Add the new student to the dictionary
                        students[student_id] = new_student
                        print("Student added successfully.")
                    break  # Exit the loop after successfully adding the student

                except ValueError:
                    # Handle invalid input during student creation
                    print("Please enter a valid input.")

        # Option 'b': Edit an existing student's information
        elif choice == 'b':
            if not students:  # Check if there are any students to edit
                print("No students available to edit.")
                break  # Exit if no students are available

            # Display the list of students (Name and ID)
            print("Student List (Name, ID):")
            for student_id, student in students.items():
                print(f"{student.get_first_name()} (ID: {student_id})")

            # Prompt the user to enter the ID of the student to edit
            student_id = input("Enter the student ID of the student to edit (or type 'exit' to quit): ")
            if student_id.lower() == 'exit':  # Exit the edit mode
                print("Exiting edit mode.")
            elif student_id in students:
                # Call the edit_student function to update the student's information
                edit_student(students[student_id])
                print("Student information updated successfully.")
            else:
                # Handle case where the entered student ID is not found
                print("Student not found.")

        # Option 'c': Delete an existing student
        elif choice == 'c':
            if not students:  # Check if there are any students to delete
                print("No students available to delete.")
                continue  # Return to the menu if no students are available

            # Display the list of students (Name and ID)
            print("Student List (Name, ID):")
            for student_id, student in students.items():
                print(f"{student.get_first_name()} (ID: {student_id})")

            # Prompt the user to enter the ID of the student to delete
            student_id = input("Enter the student ID of the student to delete (or type 'exit' to quit): ")
            if student_id.lower() == 'exit':  # Exit the delete mode
                print("Exiting delete mode.")
            elif student_id in students:
                # Confirm deletion of the student
                confirmation = input(f"Are you sure you want to delete student {students[student_id].get_first_name()}? (yes/no): ").lower()
                if confirmation == 'yes':
                    del students[student_id]  # Delete the student from the dictionary
                    print("Student deleted successfully.")
                else:
                    print("Student not deleted.")  # Handle cancellation of deletion
            else:
                print("Student not found.")  # Handle case where the entered student ID is not found

        # Option 'd': Display a student's information
        elif choice == 'd':
            if not students:  # Check if there are any students to display
                print("No students available to display.")
                continue  # Return to the menu if no students are available

            # Display the list of students (Name and ID)
            print("Student List (Name, ID):")
            for student_id, student in students.items():
                print(f"{student.get_first_name()} (ID: {student_id})")

            # Prompt the user to enter the ID of the student to display
            student_id = input("Enter the student ID of the student to display (or type 'done' to return): ")
            if student_id.lower() == 'done':  # Allow the user to return to the main menu
                continue
            elif student_id in students:
                # Call the display_student function to show the student's details
                display_student(students[student_id])
            else:
                print("Student not found.")  # Handle case where the entered student ID is not found
        
    
        # Option 'e' to manage advisor
        elif choice == 'e':
            print('\n -- Advisor Management --')
            print('1. Add an advisee')
            print('2. Remove an advisee')
            print('3. Display advisee info')
            sub_choice = input('Choose an option between 1 and 3: ').strip()

            if sub_choice == '1':
                student_id = input('Enter student ID to add as advisee: ').strip()
                if student_id in students:
                    advisor.add_advisee(students[student_id])
                    print(f'Student {students[student_id].get_first_name()} added as an advisee.')
                else:
                    print('Student not found')
            
            elif sub_choice == '2':  # Remove an advisee
                student_id = input("Enter student ID to remove as advisee: ")
                advisor.remove_advisee(student_id)
            
            elif sub_choice == '3':
                print(advisor)
            
            else:
                print('invalid choice sorry')

        #Option 'f' to manage courses for a student
        elif choice == 'f':
            student_id = input("Enter the student ID: ").strip()
            if student_id in students:  # Check if the student exists
                student = students[student_id]
                print("\n--- Course Management ---")
                print("1. Add a course")
                print("2. Remove a course")
                print("3. Display all courses")
                sub_choice = input("Choose an option: ").strip()
                
                if sub_choice == '1':  # Add a course
                    course_num = input("Enter course number (e.g., CMPSC 122): ").strip()
                    semester = input("Enter semester (e.g., Spring 2023): ").strip()
                    delivery = input("Enter delivery method (in-person/hybrid/remote): ").strip()
                    status = input("Enter status (completed/dropped/on-going): ").strip()
                    grade = input("Enter grade (A/B/C/D/F/N/A): ").strip()
                    course = Course(course_num, semester, delivery, status, grade)
                    student.add_course(course)
                    print("Course added successfully.")

                elif sub_choice == '2':  # Remove a course
                    course_num = input("Enter course number to remove: ").strip()
                    student.remove_course(course_num)
                
                elif sub_choice == '3':  # Display all courses
                    print(f"Courses for {student.get_first_name()}:\n{student.get_all_courses()}")
                
                else:
                    print("Invalid choice. Please select a valid option (1-3).")
                
            else:
                print("Student not found. Please enter a valid student ID.")

        # Option 'g': Exit the program
        elif choice == 'g':
            print("Thank you for using the student academic advisor.")  # Farewell message
            break  # Exit the program

        # Handle invalid menu choice
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()