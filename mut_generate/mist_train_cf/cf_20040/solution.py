"""
QUESTION:
Write a function `add_bitwise(a, b)` that takes two positive integers `a` and `b` as input and returns their sum. The function should only use bitwise operators (AND, OR, XOR, shift operators) and have a time complexity of O(log n), where n is the maximum number of bits required to represent the input numbers.
"""

def add_bitwise(a, b):
    """
    This function takes two positive integers a and b as input and returns their sum.
    It uses only bitwise operators and has a time complexity of O(log n), where n is the maximum number of bits required to represent the input numbers.

    Args:
        a (int): A positive integer.
        b (int): A positive integer.

    Returns:
        int: The sum of a and b.
    """
    # Iterate until there is no carry left
    while b != 0:
        # Calculate the carry
        carry = a & b

        # Calculate the sum without carry
        a = a ^ b

        # Shift the carry to the left by 1 position
        b = carry << 1

    return a