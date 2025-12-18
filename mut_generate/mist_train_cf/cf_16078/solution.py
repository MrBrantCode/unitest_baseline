"""
QUESTION:
Create a function `sum_preceding_numbers(num)` that takes an integer `num` as input and returns the sum of all integers from 1 to `num - 1`. The input `num` should be a prime number greater than 1, less than 100, and divisible by 3.
"""

def sum_preceding_numbers(num):
    """
    This function calculates the sum of all integers from 1 to num - 1.
    
    Args:
        num (int): A prime number greater than 1, less than 100, and divisible by 3.
    
    Returns:
        int: The sum of all integers from 1 to num - 1.
    """
    total = 0
    for i in range(1, num):
        total += i
    return total