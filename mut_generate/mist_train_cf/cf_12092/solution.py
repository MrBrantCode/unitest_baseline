"""
QUESTION:
Write a function named `is_armstrong` that takes an integer `num` as input and returns a boolean indicating whether the number is an Armstrong number. An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits.
"""

def is_armstrong(num):
    """
    Checks if a given number is an Armstrong number.
    
    An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits.
    
    Args:
        num (int): The number to check.
    
    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == num