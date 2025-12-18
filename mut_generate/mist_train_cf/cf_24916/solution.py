"""
QUESTION:
Create a function called `check_odd_or_even` to determine whether a given integer is odd or even. The function should take an integer as input and return a string indicating whether the number is "odd" or "even".
"""

def check_odd_or_even(number):
    """
    This function determines whether a given integer is odd or even.

    Args:
        number (int): The number to be checked.

    Returns:
        str: A string indicating whether the number is "odd" or "even".
    """
    if number % 2 == 0:
        return "even"
    else:
        return "odd"