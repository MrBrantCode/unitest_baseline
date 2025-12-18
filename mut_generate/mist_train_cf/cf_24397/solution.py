"""
QUESTION:
Create a function called `calculate_grade` that takes one argument, `percentage`, and returns the corresponding grade based on the percentage. The grade should be determined by the following conditions: 90 and above is 'A', 80-89 is 'B', 70-79 is 'C', 60-69 is 'D', below 60 is 'F'. If the input is not a valid percentage, return 'Invalid'.
"""

def calculate_grade(percentage):
    """
    Calculate the grade based on the given percentage.

    Args:
    percentage (float): The percentage to calculate the grade from.

    Returns:
    str: The grade corresponding to the percentage.
    """
    if not isinstance(percentage, (int, float)) or percentage < 0 or percentage > 100:
        return 'Invalid'
    elif percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'