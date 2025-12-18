"""
QUESTION:
Write a function named `validate_sum` that takes two integers as input and returns True if their sum is correct and greater than 100, otherwise return False.
"""

def validate_sum(num1, num2):
    """
    Validate if the sum of two integers is correct and greater than 100.

    Args:
    num1 (int): The first integer.
    num2 (int): The second integer.

    Returns:
    bool: True if the sum is correct and greater than 100, False otherwise.
    """
    return num1 + num2 > 100 and num1 + num2 == sum([num1, num2])