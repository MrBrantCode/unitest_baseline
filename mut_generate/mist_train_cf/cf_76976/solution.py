"""
QUESTION:
Write a function named `binary_to_decimal` that takes a list of binary numbers in string format, converts each number to its decimal equivalent, and returns a list of these decimal numbers.

The input list will contain only valid binary numbers.
"""

def binary_to_decimal(binary_nums):
    """
    Converts a list of binary numbers to their decimal equivalents.

    Args:
        binary_nums (list): A list of binary numbers in string format.

    Returns:
        list: A list of decimal numbers corresponding to the input binary numbers.
    """
    decimal_nums = []
    for num in binary_nums:
        decimal = 0
        for digit in num:
            decimal = decimal * 2 + int(digit)
        decimal_nums.append(decimal)
    return decimal_nums