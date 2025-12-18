"""
QUESTION:
Create a function `calculate_grade` that takes an integer between 1 and 100 as input and returns the corresponding letter grade based on the following scale: 
90-100 = A, 80-89 = B, 70-79 = C, 60-69 = D, and below 60 = F. The function should handle inputs outside the valid range and return a relevant message. 

Additionally, create a function `calculate_gpa` that takes a letter grade as input and returns the corresponding GPA based on the standard 4.0 GPA scale: A = 4.0, B = 3.0, C = 2.0, D = 1.0, and F = 0.0. 

Implement exception handling to handle invalid inputs and ensure the program does not crash when encountering invalid data.
"""

def calculate_grade(points):
    """
    Calculate the letter grade based on the given points.

    Args:
    points (int): An integer between 1 and 100.

    Returns:
    str: The corresponding letter grade.
    """
    if points < 0 or points > 100:
        return "Invalid input. Please enter a number between 0 and 100."
    elif points >= 90:
        return 'A'
    elif points >= 80:
        return 'B'
    elif points >= 70:
        return 'C'
    elif points >= 60:
        return 'D'
    else:
        return 'F'

def calculate_gpa(grade):
    """
    Calculate the GPA based on the given grade.

    Args:
    grade (str): A letter grade (A, B, C, D, F).

    Returns:
    float: The corresponding GPA.
    """
    if grade not in ['A', 'B', 'C', 'D', 'F']:
        return "Invalid input. Please enter a valid letter grade."
    grade_gpa_map = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }
    return grade_gpa_map[grade]