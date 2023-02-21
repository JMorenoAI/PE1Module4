# Student Information Management System
This is a Python program for managing student information.

## Features
Add a new student
List or display student information
Update a student's information
Delete a student's information
Quit the program

##Usage
Run the program.
Select an option from the menu.
Enter the required information to perform the chosen action.
Repeat steps 2-3 as desired.
Select option 5 to quit the program.

## Functions
### add_student()
Adds a new student to the system. Prompts the user to enter the student's ID, first name, and last name. Checks if the student ID is already in use before adding the new student to the system.

### list_student()
Displays a student's information. Prompts the user to enter the student's ID and displays the student's ID, first name, and last name.

### update_student()
Updates a student's information. Prompts the user to enter the student's ID and allows the user to update the student's first name and last name.

### delete_student()
Deletes a student's information. Prompts the user to enter the student's ID and confirms the user's decision before deleting the student's information.

### Main Program Loop
The main program loop displays a menu with five options for managing student information. The user selects an option by entering a number from 1 to 5. The program then calls the appropriate function to perform the chosen action. The loop repeats until the user selects option 5 to quit the program.
