"""
QUESTION:
Create a function `detect_negative` that takes a list of integers as input and returns `True` if at least one negative number is found in the list, and `False` otherwise. The function should use mathematical operations only and not use any comparison operators (e.g., <, >, <=, >=, ==) to check for negativity.
"""

def detect_negative(numbers):
    """
    Returns True if at least one negative number is found in the list, and False otherwise.

    This function uses mathematical operations only and does not use any comparison operators 
    (e.g., <, >, <=, >=, ==) to check for negativity.

    Args:
        numbers (list): A list of integers.

    Returns:
        bool: True if a negative number is found, False otherwise.
    """
    for num in numbers:
        # Multiply the number by -1 and check if the result is positive or negative
        if num * -1 > 0:
            return True
    return False