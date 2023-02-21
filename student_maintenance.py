from data_validation import get_string
from data_validation import get_num

# Initialize an empty dictionary to store student information

students = {}


# Function to add a new student
def add_student():
    # Get student ID
    student_id = get_num("Enter student ID: ")
    # Check if student ID is already in use
    if student_id in students:
        print("Student ID already exists.")
        return
    # Get first name and last name
    first_name = get_string("Enter first name: ")
    last_name = get_string("Enter last name: ")
    # Add student to dictionary
    students[student_id] = {"first name": first_name, "last name": last_name}
    print("Student added successfully.")


# Function to list or display a student
def list_student():
    # Get student ID
    student_id = get_num("Enter student ID: ")
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
    # Get student ID
    student_id = get_num("Enter student ID: ")
    # Check if student ID exists
    if student_id not in students:
        print("Student ID does not exist.")
        return
    # Get first name and last name, if user chooses to update
    first_name = input("Enter first name (press enter to skip): ").strip().title() or students[student_id]["first name"]
    last_name = input("Enter last name (press enter to skip): ").strip().title() or students[student_id]["last name"]
    # Update student information
    students[student_id]["first name"] = first_name
    students[student_id]["last name"] = last_name
    print("Student updated successfully.")


# Function to delete a student
def delete_student():
    # Get student ID
    student_id = get_num("Enter student ID: ")
    # Check if student ID exists
    if student_id not in students:
        print("Student ID does not exist.")
        return
    # Confirm delete action
    confirm = input("Are you sure you want to delete this student? (y/n): ").strip().lower()
    if confirm == "y":
        # Remove student from dictionary
        del students[student_id]
        print("Student deleted successfully.")
    else:
        print("Action canceled.")


# Main program loop
while True:
    print("\nStudent Maintenance")
    print("1. List a student")
    print("2. Add a student")
    print("3. Update a student")
    print("4. Delete a student")
    print("5. Quit")
    choice = get_num("Enter your choice: ")

    if choice == 1:
        list_student()
    elif choice == 2:
        add_student()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        break
    else:
        print("Invalid choice.")
