"""
QUESTION:
Create a function named `is_power` that takes two parameters, `x` and `y`. The function should return `True` if `y` is a power of `x`, where both `x` and `y` are positive integers, and `False` otherwise. The function should also handle cases where `x` is a negative number or either `x` or `y` is not a positive integer.
"""

def is_power(x, y):
    if x <= 0 or y <= 0:  
        return False
    
    if x < 0:  
        return False
    
    while y % x == 0:  
        y = y // x
        if y == 1:
            return True
    
    return False