"""
QUESTION:
Write a function `check_conditions` that takes an integer as input and returns True if the number is between 1 and 10 (inclusive), divisible by 2, and not a multiple of 3, and False otherwise. The function should not take any other parameters.
"""

def check_conditions(num):
    """
    Checks if a number is between 1 and 10 (inclusive), divisible by 2, and not a multiple of 3.

    Args:
        num (int): The number to be checked.

    Returns:
        bool: True if the number satisfies the given conditions, False otherwise.
    """
    return 1 <= num <= 10 and num % 2 == 0 and num % 3 != 0