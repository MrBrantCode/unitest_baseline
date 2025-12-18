"""
QUESTION:
Write a function `check_sum_cubes(number)` that takes a number as input and returns `True` if the number is equal to the sum of the cube of its digits and `False` otherwise. The range of numbers to check is from 10 to 354294. Find the sum of all numbers within this range that satisfy this condition.
"""

def check_sum_cubes(number):
    """
    This function checks if the number is equal to the sum of the cube of its digits.
    
    Args:
    number (int): The number to check.
    
    Returns:
    bool: True if the number is equal to the sum of the cube of its digits, False otherwise.
    """
    sum_cubes = sum([int(digit)**3 for digit in str(number)])
    return sum_cubes == number