"""
QUESTION:
Write a function `check_number_in_range` that checks if a given decimal number is within a specified inclusive range. The function should also verify that the number has at most 2 decimal places. The function should return `True` if the number is within the range and has at most 2 decimal places, and `False` otherwise.
"""

def check_number_in_range(number, min_range, max_range):
    """
    Checks if a given decimal number is within a specified inclusive range and has at most 2 decimal places.
    
    Args:
        number (float): The number to be checked.
        min_range (float): The minimum value of the range.
        max_range (float): The maximum value of the range.
    
    Returns:
        bool: True if the number is within the range and has at most 2 decimal places, False otherwise.
    """
    if number >= min_range and number <= max_range:
        return len(str(number).split('.')[1]) <= 2
    return False