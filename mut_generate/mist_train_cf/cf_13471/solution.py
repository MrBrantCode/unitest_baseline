"""
QUESTION:
Implement a function named `is_even` that determines whether a given integer is even or odd without using the modulo operator. The function should take one integer argument, `number`, and return a boolean value indicating whether the number is even.
"""

def is_even(number):
    """
    Determines whether a given integer is even or odd without using the modulo operator.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return (number & 1) == 0