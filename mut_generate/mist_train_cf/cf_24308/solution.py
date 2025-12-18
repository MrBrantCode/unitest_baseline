"""
QUESTION:
Create a data structure to represent a student's information. The data structure should include the student's name, student ID, GPA, and course load. Implement the data structure in Python.
"""

def create_student(name, student_id, gpa, course_load):
    """
    Creates a dictionary representing a student's information.
    
    Args:
        name (str): The student's name.
        student_id (str): The student's ID.
        gpa (float): The student's GPA.
        course_load (list): A list of the student's courses.
    
    Returns:
        dict: A dictionary containing the student's information.
    """
    return {
        "name": name,
        "student_id": student_id,
        "gpa": gpa,
        "course_load": course_load
    }