"""
QUESTION:
Write a function `calculate_sum` that takes no arguments and a float number as input, rounds it to the nearest whole number, converts it to an integer, calculates the sum of all the digits in the resulting integer, and returns the sum.
"""

def calculate_sum(number: float) -> int:
    """
    Calculate the sum of digits in the integer nearest to the given float number.
    
    Args:
    number (float): The input float number.
    
    Returns:
    int: The sum of digits in the integer nearest to the input float number.
    """
    result = int(round(number))
    return sum([int(digit) for digit in str(result) if digit.isdigit()])