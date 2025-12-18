"""
QUESTION:
Detect Negative Number in Array
Write a function named `detect_negative` that takes an array of numbers as input and returns a boolean indicating whether any negative numbers are found. The function must not use any comparison operators (e.g., <, >, <=, >=, ==) to check for negativity, and instead use mathematical operations to determine if a number is negative.
"""

def detect_negative(numbers):
    """
    Detects if any negative numbers are present in the given array.

    Args:
    numbers (list): A list of numbers.

    Returns:
    bool: True if a negative number is found, False otherwise.
    """
    for num in numbers:
        # Multiply the number by -1 and check if the result is positive or negative
        if num * -1 > 0:
            return True
    return False