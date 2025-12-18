"""
QUESTION:
Write a function `decimal_to_binary(number)` that takes a positive integer as input and returns its binary representation as a string. The function should not use any built-in functions or libraries to convert decimal to binary and should have a time complexity of O(log n), where n is the input number.

Write another function `sum_binary_numbers(binary_numbers)` that takes a list of binary numbers as strings and returns their decimal sum.

The program should handle cases where the input is not a positive integer and should display an error message for such cases.
"""

def decimal_to_binary(number):
    """
    Converts a decimal number to its binary representation as a string.
    
    Args:
    number (int): A positive integer.
    
    Returns:
    str: The binary representation of the input number as a string.
    """
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary


def sum_binary_numbers(binary_numbers):
    """
    Calculates the decimal sum of a list of binary numbers.
    
    Args:
    binary_numbers (list): A list of binary numbers as strings.
    
    Returns:
    int: The decimal sum of the input binary numbers.
    """
    total = 0
    for binary in binary_numbers:
        total += int(binary, 2)
    return total