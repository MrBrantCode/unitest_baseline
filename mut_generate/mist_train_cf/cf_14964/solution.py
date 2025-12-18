"""
QUESTION:
Write a function named `calculate_average_high_grade` that takes no arguments. It should return the average grade of students from the 'Students' table with grades above 90. Assume a database or data structure 'Students' with 'name' and 'grade' columns is available.
"""

def calculate_average_high_grade(Students):
    """
    Calculate the average grade of students with grades above 90.

    Args:
    Students (list of dictionaries): A list of dictionaries containing 'name' and 'grade' keys.

    Returns:
    float: The average grade of students with grades above 90.
    """
    grades_above_90 = [student['grade'] for student in Students if student['grade'] > 90]
    if grades_above_90:
        return sum(grades_above_90) / len(grades_above_90)
    else:
        return 0