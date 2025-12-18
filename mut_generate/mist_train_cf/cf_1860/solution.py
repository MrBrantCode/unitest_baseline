"""
QUESTION:
Create a function `is_divisible_by_two(num)` that takes an integer as input and returns `True` if the number is divisible by two and `False` otherwise. The function should not use the modulo operator or any other built-in functions. The time complexity of the solution should be O(1). Implement this function and use it in the existing `divisible_by_two(numbers)` function to determine if each number in the input list is divisible by two and return the result as a list of boolean values.
"""

def is_divisible_by_two(num):
    """
    Checks if a number is divisible by two without using the modulo operator.

    Args:
    num (int): The number to check.

    Returns:
    bool: True if the number is divisible by two, False otherwise.
    """
    return (num & 1) == 0