"""
QUESTION:
Create a function named `add_student_details` that takes a list of tuples as input, where each tuple contains a student's ID, name, age, and GPA. The function should return a dictionary with student IDs as keys and tuples of their details as values. 

The function should raise an `InvalidStudentDetails` exception if the student ID is not an integer, the age is not between 18 and 99, or the GPA is not between 0 and 4.
"""

class InvalidStudentDetails(Exception):
    pass

def add_student_details(student_details_list):
    student_details_dict = {}
    for details in student_details_list:
        student_id, student_name, student_age, student_gpa = details

        if type(student_id) != int:
          raise InvalidStudentDetails("Student ID should be an integer.")

        if not(18 <= student_age <= 99):
            raise InvalidStudentDetails("Age should be in the range 18-99.")
          
        if not(0 <= student_gpa <= 4):
            raise InvalidStudentDetails("GPA should be between 0 and 4.")
        
        student_details_dict[student_id] = (student_name, student_age, student_gpa)

    return student_details_dict