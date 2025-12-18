"""
QUESTION:
Create a function called `create_student_record` that takes in a student's name, age, and a list of subjects as parameters, and returns a tuple representing the student record. The tuple should contain the student's name (a string), age (an integer), and the list of subjects (a list). The function should not modify the input parameters and should return a tuple with the provided information.
"""

def create_student_record(name, age, subjects):
    """
    Creates a student record as a tuple containing the student's name, age, and list of subjects.

    Args:
    name (str): The student's name.
    age (int): The student's age.
    subjects (list): A list of subjects the student is enrolled in.

    Returns:
    tuple: A tuple containing the student's name, age, and list of subjects.
    """
    return (name, age, subjects)