"""
QUESTION:
Write a function `check_equal` that takes two integers `num1` and `num2` as input and returns a boolean indicating whether they are equal without using any comparison operators.
"""

def check_equal(num1: int, num2: int) -> bool:
    """
    Checks if two integers are equal using bitwise XOR operator.

    Args:
        num1 (int): The first integer.
        num2 (int): The second integer.

    Returns:
        bool: True if the integers are equal, False otherwise.
    """
    return (num1 ^ num2) == 0