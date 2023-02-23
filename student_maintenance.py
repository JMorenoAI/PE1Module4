import data_validation as dv  # user input data validation

# the following are module level dunders (metadata) for the authorship information
__author__ = 'Joshua Moreno'
__version__ = '1.0'
__date__ = '2023.02.20'
__status__ = 'Release'

# This is a Python program for managing student information. You can add, list, update, and delete a student.

# Data validation used to verify whether the user entered a valid data input

# Display an input prompt to get a string value, which can not be an empty string
# and loop again if invalid

students = {}  # students 2D dictionary {id: {'first_name': value}, {'last_name': value}}
next_student_id = 1


# Function to add a new student
def add_student(students, next_student_id):
    # Get first name and last name
    first_name = dv.get_string("Enter first name: ")
    last_name = dv.get_string("Enter last name: ")
    # Add student to dictionary
    students[next_student_id] = {"first name": first_name, "last name": last_name}
    print("Student added successfully.")


# Function to list or display a student
def list_student():
    # Get student ID
    student_id = dv.get_num("Enter student ID: ")
    # Check if student ID exists
    if student_id not in students:
        print("Student ID does not exist.")
        return
    # Print student information
    student = students[student_id]
    print(f"Student ID: {student_id}")
    print(f"First Name: {student['first name']}")
    print(f"Last Name: {student['last name']}")


# Function to update a student
def update_student():
    # Check if there are students to update their information.
    if len(students) == 0:
        print("There are no students to update")
        return
    # Get student ID
    student_id = dv.get_num("Enter student ID: ")
    # Check if student ID exists
    if student_id not in students:
        print("Student ID does not exist.")
        return

    # Get first name and last name, if user chooses to update
    first_name = input("Enter first name: ").students[student_id]["first name"]
    last_name = input("Enter last name: ").students[student_id]["last name"]
    # Update student information
    students[student_id]["first name"] = first_name
    students[student_id]["last name"] = last_name
    print("Student updated successfully.")


# Function to delete a student
def delete_student():
    # Check if there are students to delete
    if len(students) == 0:
        print("There are no students to delete.")
        return
    # Get student ID
    student_id = dv.get_num("Enter student ID: ")
    # Check if student ID exists
    if student_id not in students:
        print("Student ID does not exist.")
        return

    # Confirm delete action
    confirm = input("Are you sure you want to delete this student? (y/n): ")
    if confirm == "y":
        # Remove student from dictionary
        del students[student_id]
        print("Student deleted successfully.")
    else:
        print("Action canceled.")

