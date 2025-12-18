"""
QUESTION:
Write a function named handle_overflow that handles integer overflow when adding two numbers. The function should take two integers as input and return their sum without overflowing. The function should use a data type that can handle arbitrarily large integers. The function should not use any specialized libraries for arbitrary precision arithmetic.
"""

def handle_overflow(num1, num2):
    """
    Handles integer overflow when adding two numbers.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        int: The sum of num1 and num2 without overflowing.
    """
    # Python's built-in arbitrary precision arithmetic can handle large integers
    # So, no need for explicit checks or handling
    return num1 + num2