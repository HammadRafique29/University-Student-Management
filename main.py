
"""
 References:
 Multiple values in dictionary:https://stackoverflow.com/questions/31426095/assign-multiple-values-of-a-list
 * Use this as coding strategy for storing value since other ways I thought was too difficult to execute
 Formatting dates modules: https://docs.python.org/3/library/datetime.html
"""

import csv
from datetime import datetime
import os

# Defines Student class that represent student and information about the student(Start at line 10)


class Student:
    # Define a constructor and initialize attributes about the student like ID,last name,first name,etc(Line 12-19)
    def __init__(self, s_id, l_name, f_name, s_majoir, s_gpa, s_grad, d_action):
        self.s_id = s_id
        self.l_name = l_name
        self.f_name = f_name
        self.s_majoir = s_majoir
        self.s_gpa = s_gpa
        self.s_grad = s_grad
        self.d_action = d_action

# Function that helps to extract the information needed(Line 19-32)


def obtain_last_names(id_of_student):
    return id_of_student.l_name


def obtain_student_id(student_identification):
    return student_identification.s_id


def obtain_student_gpa(gpa_student):
    return gpa_student.s_gpa


def obtain_grad_date(grad_student):
    return grad_student.s_grad


# Define a University class to extract and manage university records(Starts at 43)


class UniversityRecords:
    def __init__(self):
        # Initialize a dictionary to store student information with student ID as the key(Line 45)
        self.students = {}

    # Define a function that extract needed students information from 'StudentsMajorsList-3.csv'(Line 49-62)
    def extract_student_majoir(self, major_file):
        # Open the 'StudentsMajorsList-3.csv' in read mode(Line 51)
        with open(major_file, 'r') as m_file:
            # Creates a csv reader to parse everything in the file.(Line 52)
            major_reader = csv.reader(m_file)
            # Skip the Csv Header Line
            header = next(major_reader)
            # Loop through all the line/rows in the file(Line 56)
            for majoir_rows in major_reader:
                # Extract the relevant information and store it(Line 58)
                student_id, last_name, first_name, student_majoir, disciplinary_action = majoir_rows[:5]
                # Create a new Student object(Line 60)
                s_new = Student(student_id, last_name, first_name, student_majoir, None, None, disciplinary_action)
                # Store all information from s_new into the student dictionary(Line 62)
                self.students[student_id] = s_new

    # Creates a function to extract needed student information from 'GPAList-1.csv'(Line 65-76)
    def extract_gpa_data(self, gpa_file):
        # Open the 'GPAList-1.csv' in read mode(Line 51)
        with open(gpa_file, 'r') as file:
            # Creates a csv reader to parse everything in the file(line 69)
            reader_gpa = csv.reader(file)
            # Skip the Csv Header Line
            header = next(reader_gpa)
            # Loop through each row in the file(Line 71)
            for rows_grads in reader_gpa:
                # Extract the id of student from the row and store it (Line 73)
                id_student, student_gpa = rows_grads
                # If the student ID is part of the student dictionary, then update the graduation date
                if id_student in self.students:
                    self.students[id_student].s_gpa = float(student_gpa)

    # Creates a function that extract need student information from 'GraduationDatesList-1.csv'(Line 79-89)
    def extract_grad_data(self, grad_file):
        # Open the ''GraduationDatesList-1.csv' in read mode(Line 81)
        with (open(grad_file, 'r') as g_file):
            # Creates a csv reader to parse everything in the file(line 82)
            graduate_file = csv.reader(g_file)
            # Skip the Csv Header Line
            header = next(graduate_file)
            # Loop through each row in the file(Line 85)
            for rows_grads in graduate_file:
                # Extract the student ID and graduation date and store it(Line 87)
                students_id, student_grad = rows_grads
                # Format the graduation date in to proper format(Line 89)
                student_grad = datetime.strptime(student_grad, "%m/%d/%Y")
                # Check if the student ID is present in the student dictionary, it is update the student graduate(91-92)
                if students_id in self.students:
                    self.students[students_id].s_grad = student_grad
            
    def interactive_query(self):
        input_majoir = input("Enter the major: ")
        input_gpa = float(input("Enter the GPA: "))

        # List of possible majors
        majors = ["computerscience", "mathematics", "physics", "chemistry", "biology", "engineering", "economics", "psychology", "english", "history", "politicalscience", "sociology", "business", "finance", "marketing", "accounting", "art", "music", "physicaleducation", "healthsciences", "nursing", "education", "communications", "philosophy", "religiousstudies", "environmentalscience", "geology", "astronomy", "statistics", "informationtechnology", "criminaljustice", "premed", "prelaw", "predental", "preveterinary", "undecided"]
        
        # convert the input major in lower case and remove spaces ( if user type: "Computer Science" output:"computerscience")
        # IN this case we will check the occurance of mojor by raplace the 1 major with empty and setting True
        # If we find second mojor than we set the validMajor to False and return by printing message
        checkMajor = "".join(input_majoir.split(' ')).lower()
        
        validMajor = False
        for major in majors:
            # Temporary var for comparing the values
            check = checkMajor.replace(major, "")
            if check != checkMajor: 
                if not validMajor:
                    validMajor = True
                    checkMajor = check
                elif validMajor: 
                    print("INVALID MAJOR: Using Majors More Than Once")
                    return 0

        # List of matching students
        # List of suggested students
        student_matching = []
        suggested_students = []

        # Loop through student data
        for m_student in self.students.values():

            # Compare major with data in student.major
            if input_majoir.lower() in m_student.s_majoir.lower():

                # Compare GPA with data in student.gpa (-0.1 & +0.1)
                if m_student.s_gpa >= input_gpa - 0.1 and m_student.s_gpa <= input_gpa + 0.1:
                    # Add the student to the matching_student list
                    student_matching.append(m_student)

                # Compare GPA with data in student.gpa (-0.25 & +0.25)
                elif m_student.s_gpa >= input_gpa - 0.25 and m_student.s_gpa <= input_gpa + 0.25:
                    # Add the student to the suggested_student list
                    suggested_students.append(m_student)

        # Check if there are matching students
        if student_matching:
            print("\nMatching Students:")
            for student in student_matching:
                print(f"Student ID: {student.s_id}, Name: {student.f_name} {student.l_name}, GPA: {student.s_gpa}")

        # Check if there are suggested students
        if suggested_students:
            print("\nSuggested Students:")
            for student in suggested_students:
                print(f"Student ID: {student.s_id}, Name: {student.f_name} {student.l_name}, GPA: {student.s_gpa}")

        # If no matching or suggested students are found
        if not student_matching and not suggested_students:
            print("No students found for the given criteria.")



if __name__ == "__main__":
    # Creates an instance of the UniversityRecords class
    records = UniversityRecords()

    # Extract all data from the input file by calling the respective function in the class(Line 208- 210)
    records.extract_student_majoir('StudentsMajorsList.csv')
    records.extract_grad_data('GraduationDatesList.csv')
    records.extract_gpa_data('GPAList.csv')

    while True:
        os.system("cls")
        records.interactive_query()
        choice = input("\nHave Another Query (Y/N): ")
        if choice.lower()=="n": break
        else: continue