"""
QUESTION:
Write a function `checkNumbers(x, y)` that checks if both `x` and `y` are within the range of -1000 to 1000, and if `x` is a multiple of 3 and `y` is a multiple of 5. The function should also verify that both `x` and `y` are even numbers using bitwise operators. Ensure the function has a time complexity of O(1) and a space complexity of O(1).
"""

def checkNumbers(x, y):
    """
    Checks if both x and y are within the range of -1000 to 1000, 
    if x is a multiple of 3, y is a multiple of 5, and both x and y are even numbers.

    Args:
        x (int): The first number to check.
        y (int): The second number to check.

    Returns:
        bool: True if all conditions are met, False otherwise.
    """
    return -1000 <= x <= 1000 and -1000 <= y <= 1000 and x % 3 == 0 and y % 5 == 0 and (x & 1) == 0 and (y & 1) == 0