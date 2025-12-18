"""
QUESTION:
Create a function `check_range` that takes an integer `number` as input and returns a boolean value indicating whether the number is between 1 and 10 (inclusive).
"""

def check_range(number):
    """
    Checks if the given number is between 1 and 10 (inclusive).
    
    Args:
        number (int): The number to check.
    
    Returns:
        bool: True if the number is between 1 and 10, False otherwise.
    """
    return 1 <= number <= 10