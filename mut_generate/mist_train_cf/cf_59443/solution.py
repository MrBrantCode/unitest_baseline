"""
QUESTION:
Design a data structure to efficiently store and retrieve student information. The data structure should store the following student details: student ID, name, class, gender, date of birth, and marks (which can include multiple subjects). The structure should support adding new students, retrieving student information by ID, and updating existing student information.
"""

def student_info(student_id, student_name, class_name, gender, date_of_birth, marks):
    """
    Data structure design for student information system.
    
    Args:
    student_id (str): Unique identifier for the student.
    student_name (str): Name of the student.
    class_name (str): Class of the student.
    gender (str): Gender of the student.
    date_of_birth (str): Date of birth of the student.
    marks (dict): Marks of the student in different subjects.
    
    Returns:
    dict: A dictionary containing the student's information.
    """
    
    student_info = {
        'ID': student_id, 
        'Name': student_name, 
        'Class': class_name, 
        'Gender': gender, 
        'DOB': date_of_birth, 
        'Marks': marks
    }
    
    return student_info