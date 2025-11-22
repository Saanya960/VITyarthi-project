# PYTHON ESSENTIALS
PROJECT-'COLLEGE MARKS TRACKER SYSTEM'
# OVERVIEW
In most colleges, student marks are recorded manually using registers or simple spreadsheets, due to which there are high chances of calculation mistakes (totals).Also, it is time-consuming and inefficient for faculty during exams or assessments. A digital solution is required to simplify the process of entering, storing, analyzing, and exporting student marks.
# features
A marks tracker system offering marks of 8 courses to be stored in excel form.
1. Provides a simple and user-friendly GUI.
2. Allows entering Student ID and navigating through the interface.
3. Validates user input (e.g., empty fields, incorrect values).
4. Displays error and success messages for proper guidance.
5. Exports all stored student data to an Excel file.
6. Includes Student ID, course-wise marks, and total marks in the report.
7. Shows a confirmation message once the file is saved.
8. Ensures the report can be printed, shared, or stored for institutional use.
# Technologies and Purpose

Python - Core programming language
Tkinter - GUI interface for entering marks
Pandas - Data handling, manipulation, and Excel export
OpenPyXL - Writing data into Excel format

# Methods used
Object-oriented and functional programming for modular design

Tkinter widgets (Entry, Label, Button, Treeview) for GUI

DataFrames for storing marks systematically

Excel Writer for multi-sheet export

Input validation to ensure marks are correctly entered
# Steps to install and run the project
1.Install Python
Download and install the latest version of Python from the official website.
2. Install Required Libraries
Open Command Prompt (Windows) or Terminal (Mac/Linux) and run:
pip install numpy pandas matplotlib openpyxl
(Tkinter comes pre-installed with Python on most systems.)
3. Download or Copy the Project Code
Save the Python file (e.g., marks_tracker.py) into a folder on your system.
4. Run the Application
Navigate to the project folder using the terminal:
cd path_to_your_project_folder
Run the program:
python marks_tracker.py
5. Use the GUI
A window will open with input fields for Student ID and Course Marks.
Enter marks → Click Add Record → Click Save to Excel when done.

# Instructions for testing

-Input Field Testing
Enter valid numeric marks (0–100) to confirm the system accepts correct data.
Enter invalid inputs like letters, blanks, or negative numbers to ensure error messages appear.
    
-Functional Testing
Add multiple records and verify they appear correctly in the GUI table.
Check if total marks are calculated accurately for each student.
Ensure duplicate Student IDs produce expected behavior (if applicable).

-Excel Export Testing
Click Save to Excel and verify that the generated file:
Opens properly
Contains all rows
Displays marks and totals correctly
Matches the GUI data

-Usability Testing
Ensure the GUI layout is clear and buttons work smoothly.
Verify that error dialogs appear at correct times.

-Performance Testing
Enter 50 student records and check if the system remains responsive.
Verify Excel export for large entries works without delays or crashes.








  


  

  

