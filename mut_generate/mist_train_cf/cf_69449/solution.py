"""
QUESTION:
Design a function called `extract_integer` that takes a float as input and returns the largest integer less than or equal to the given number. If the input is zero, return zero. If the input number is infinity or too large, return 'Error: Number too large.' The function should handle both positive and negative numbers.
"""

import math

def extract_integer(number: float) -> int:
    """ Given a float, it separates into an integer component 
    (the largest integer less than or equal to the given number) and decimals 
    (remaining part always less than 1 and greater than -1).
    
    If the input is zero, return zero.
    If the input number is very large, return an error message instead.
    Provide the integer segment of the positive or negative number.
    """
    
    if number == 0:
        return 0
    elif number == float('inf') or number == -float('inf'):
        return 'Error: Number too large.'
    else:
        return math.floor(number)