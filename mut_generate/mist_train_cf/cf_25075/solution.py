"""
QUESTION:
Write a function `sum_of_digits` that takes an integer as input and returns the sum of its digits. The input integer is non-negative and can be any integer within the range of integer data type in Python. The function should not use recursion, string conversion, or any built-in functions to calculate the sum.
"""

def sum_of_digits(num):
    """
    This function calculates the sum of digits of a given non-negative integer.
    
    Parameters:
    num (int): A non-negative integer.
    
    Returns:
    int: The sum of digits of the input integer.
    """
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10
    return total