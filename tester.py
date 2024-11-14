from mailing_address import MailingAddress
from date import Date
from email import Email
from phone_number import PhoneNumber
from semester_class import Semester
from student_class import Student


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
        phone_number = input("Enter phone number (or 'done' to finish): ")
        if phone_number.lower() == "done":
            break
        phone_type = input("Enter phone type (e.g., mobile, home): ")
        phone_numbers.append(PhoneNumber(phone_number, phone_type))

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
    student.set_phone_number(phone_number)





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
    print("e. Exit")






def main():
    students = []  # Empty list to store student information 

    while True:
        menu()  # Print the menu
        choice = input("Choose an option: ").lower()

        if choice == 'a':
            while True:
                try:
                    new_student = create_student()
                    if any(s.get_student_id() == new_student.get_student_id() for s in students):
                        print("Error: A student with this ID already exists. This student was not added.")
                    else:
                        students.append(new_student)
                        print("Student added successfully.")
                        break
                
                except ValueError:
                    print("Please enter an actual input.")

        elif choice == 'b':
            while True:
                # Display each student's first name and ID
                student_display = [(s.get_first_name(), s.get_student_id()) for s in students]
                print("Student List (Name, ID):")
                for name, student_id in student_display:
                    print(f"{name} (ID: {student_id})")
                
                # Prompt user for student ID to edit
                student_id = input("Enter the student ID of the student to edit (or type 'exit' to quit): ")
                if student_id.lower() == 'exit':
                    print("Exiting edit mode.")
                    break  # Exit the loop if the user types 'exit'
                
                student = next((s for s in students if s.get_student_id() == student_id), None)
                if student:
                    edit_student(student)
                    print("Student information updated successfully.")
                else:
                    print("Student not found.")

        elif choice == 'c':
            while True:
                student_display = [(s.get_first_name(), s.get_student_id()) for s in students]
                print("Student List (Name, ID):")
                for name, student_id in student_display:
                    print(f"{name} (ID: {student_id})")
                
                # Prompt user for student ID to edit
                student_id = input("Enter the student ID of the student to edit (or type 'exit' to quit): ")
                if student_id.lower() == 'exit':
                    print("Exiting edit mode.")
                    break  # Exit the loop if the user types 'exit'
                else:
                    student = next((s for s in students if s.get_student_id() == student_id), None)
                    if student:
                        user_int = int('Are you sure you would like to delete this student (Type yes or no)')
                        if user_int == 'yes':
                            students.remove(student)
                            print("Student deleted successfully.")
                            break
                        else:
                            print('Ok, {student} will not be deleted')
                    else:
                        print("Student not found.")

        elif choice == 'd':
            while True:
                # Display a student's information
                student_id = input("Enter the student ID of the student to display: (if you would like to return type 'Done') ")
                if student_id == 'Done':
                    break
                else:
                    student = next((s for s in students if s.get_student_id() == student_id), None)
                    if student:
                        display_student(student)
                    else:
                        print("Student not found.")

        elif choice == 'e':
            print("Thank you for using the student academic advisor.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
