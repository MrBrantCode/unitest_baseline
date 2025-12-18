"""
QUESTION:
Write a function `check_number_in_range` that checks whether a given decimal number is within a specified inclusive range and has at most 3 decimal places. The number must also be positive. The function should take three parameters: `number`, `min_range`, and `max_range`.
"""

def check_number_in_range(number, min_range, max_range):
    """
    Checks whether a given decimal number is within a specified inclusive range and has at most 3 decimal places. The number must also be positive.
    
    Parameters:
    number (float): The number to check.
    min_range (float): The minimum value of the range (inclusive).
    max_range (float): The maximum value of the range (inclusive).
    
    Returns:
    bool: True if the number is within the range and satisfies the conditions, False otherwise.
    """
    return min_range <= number <= max_range and number > 0 and round(number, 3) == number