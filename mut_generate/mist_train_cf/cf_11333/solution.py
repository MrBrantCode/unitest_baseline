"""
QUESTION:
Write a function `grade_converter` that takes a numerical grade as input and returns the corresponding letter grade. The function should handle cases where the numerical grade is outside the valid range of 1-100, returning an error message in such cases. The letter grades should be assigned based on the following ranges: A (90-100), B (80-89), C (70-79), D (60-69), and F (below 60).
"""

def grade_converter(num_grade):
    """
    This function converts a numerical grade to its corresponding letter grade.

    Args:
        num_grade (int): A numerical grade between 1 and 100.

    Returns:
        str: The corresponding letter grade or an error message if the input is outside the valid range.
    """
    if num_grade < 0 or num_grade > 100:
        return "Error: Invalid grade entered."
    elif num_grade >= 90:
        return 'A'
    elif num_grade >= 80:
        return 'B'
    elif num_grade >= 70:
        return 'C'
    elif num_grade >= 60:
        return 'D'
    else:
        return 'F'