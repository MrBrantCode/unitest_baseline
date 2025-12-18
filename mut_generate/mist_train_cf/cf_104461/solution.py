"""
QUESTION:
Create a function `calculate_student_average` that stores a student's name and marks as key-value pairs in a dictionary and calculates the average of the student's marks. The student's name should be stored as a string, and the marks should be stored as a dictionary with the subject name as the key and the marks as the value. The function should return the dictionary containing the student's information and the calculated average marks.
"""

def calculate_student_average(name, marks):
    """
    Stores a student's name and marks as key-value pairs in a dictionary and calculates the average of the student's marks.

    Args:
        name (str): The student's name.
        marks (dict): A dictionary with subject names as keys and marks as values.

    Returns:
        dict: A dictionary containing the student's information and the calculated average marks.
    """
    student_dict = {name: marks}
    total_marks = sum(marks.values())
    average_marks = total_marks / len(marks)
    student_dict[f"{name}'s average"] = average_marks
    return student_dict