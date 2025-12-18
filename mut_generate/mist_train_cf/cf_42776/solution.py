"""
QUESTION:
Create a function `calculate_average` that takes a list of grades and returns the average grade. 

The function should calculate the average grade from the given list and handle potential division by zero errors. The grades should be in the range of 0 to 100. 

Restrictions: the input list will contain at least one grade.
"""

def calculate_average(grades):
    """
    Calculate the average grade from a given list of grades.
    
    Args:
    grades (list): A list of grades in the range of 0 to 100.
    
    Returns:
    float: The average grade.
    """
    return sum(grades) / len(grades)