"""
QUESTION:
Create a function called `get_students_by_grade` that takes a grade as an integer between 0 and 100 and a list of students as input, where each student is represented as a dictionary containing the student's name and grade. The function should return a list of student names who have the specified grade.
"""

def get_students_by_grade(students, grade):
    """
    Returns a list of student names with the specified grade.

    Args:
        students (list): A list of dictionaries containing student information.
        grade (int): The grade to filter students by.

    Returns:
        list: A list of student names with the specified grade.
    """
    return [student['name'] for student in students if student['grade'] == grade]