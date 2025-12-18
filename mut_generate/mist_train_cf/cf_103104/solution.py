"""
QUESTION:
Write a function named `check_number` that takes an integer as input and checks if it is between 1 and 10 (inclusive). The function should then determine if the number is divisible by 2, returning "Even" if it is, and "Odd" if it is not.
"""

def check_number(num):
    """
    This function checks if a number is between 1 and 10 (inclusive) and determines if it's even or odd.

    Args:
        num (int): The number to check.

    Returns:
        str: "Even" if the number is even, "Odd" if it's odd.
    """
    if 1 <= num <= 10:
        if num % 2 == 0:
            return "Even"
        else:
            return "Odd"
    else:
        return "Number is out of range"