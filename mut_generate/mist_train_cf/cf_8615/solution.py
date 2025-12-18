"""
QUESTION:
Create a function `check_value` that takes one argument, a real number. The function should return `True` if the number is within the range -1000 to 1000 (inclusive), is divisible by both 2 and 3, is not a multiple of 4, and has exactly 3 decimal places, and `False` otherwise.
"""

def check_value(value):
    """
    Checks if a real number is within the range -1000 to 1000, 
    is divisible by both 2 and 3, is not a multiple of 4, and has exactly 3 decimal places.

    Args:
        value (float): The number to check.

    Returns:
        bool: True if the number meets all conditions, False otherwise.
    """
    return -1000 <= value <= 1000 and value % 2 == 0 and value % 3 == 0 and value % 4 != 0 and round(value, 3) == round(round(value, 3), 3)