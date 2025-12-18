"""
QUESTION:
Create a function `factorial_and_one_less` that takes a list of integers as input. For each number `n` in the list, calculate the result as the factorial of `n` plus the factorial of `n-1`. If `n` is 0, the result should be 1 (since the factorial of 0 is 1). Return a new list containing these results.
"""

import math

def factorial_and_one_less(input_list):
    """
    Calculate the factorial of each number in the input list plus the factorial of one less than that number.
    
    If the number is 0, return 1 (since the factorial of 0 is 1).

    Args:
        input_list (list): A list of integers.

    Returns:
        list: A new list containing the calculated results.
    """
    result = [math.factorial(n) + math.factorial(n-1) if n != 0 else 1 for n in input_list]
    return result