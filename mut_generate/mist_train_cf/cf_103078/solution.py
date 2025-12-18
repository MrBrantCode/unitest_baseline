"""
QUESTION:
Write a function named `sum_of_squares` that takes a positive integer as input and returns the sum of the squares of its digits.
"""

def sum_of_squares(num):
    """
    This function calculates the sum of squares of the digits of a given number.
    
    Parameters:
    num (int): A positive integer.
    
    Returns:
    int: The sum of squares of the digits of the input number.
    """
    sum_of_squares = 0
    while num > 0:
        digit = num % 10
        sum_of_squares += digit ** 2
        num //= 10
    return sum_of_squares