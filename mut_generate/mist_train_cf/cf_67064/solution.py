"""
QUESTION:
Write a Python function `group_students_by_grade` that takes a list of tuples representing students and their grades, groups the students by their grade, and returns the grouped students. The function should take into consideration that the students with the same grade are not necessarily consecutive in the input list. The function should also handle cases where there are multiple students with the same grade.
"""

from itertools import groupby

def group_students_by_grade(students):
    """
    This function takes a list of tuples representing students and their grades, 
    groups the students by their grade, and returns the grouped students.

    Args:
        students (list): A list of tuples, where each tuple contains a student's name and their grade.

    Returns:
        dict: A dictionary where the keys are the grades and the values are lists of students with that grade.
    """

    # First, we sort the list of students based on their grades
    students = sorted(students, key=lambda student: student[1])

    # Initialize an empty dictionary to store the grouped students
    grouped_students = {}

    # Use groupby to group the students by their grade
    for key, group in groupby(students, lambda student: student[1]):
        # For each group, add the grade as a key in the dictionary and the list of students as the value
        grouped_students[key] = list(group)

    return grouped_students