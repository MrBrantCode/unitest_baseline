"""
QUESTION:
Write a function `check_divisibility_and_range` that takes an integer as input and returns a string indicating whether the number is divisible by 4 and greater than 100.
"""

def check_divisibility_and_range(num):
    """
    This function checks if a given number is divisible by 4 and greater than 100.

    Args:
        num (int): The number to be checked.

    Returns:
        str: A string indicating whether the number is divisible by 4 and greater than 100.
    """
    if num % 4 == 0 and num > 100:
        return "The number is divisible by 4 and greater than 100."
    else:
        return "The number is either not divisible by 4 or not greater than 100."