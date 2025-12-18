"""
QUESTION:
Develop a function called `find_parity` that takes two integer input parameters `x` and `y`, and returns a boolean value indicating the parity of `x` raised to the power of `y`. If the result is even (i.e., divisible by 2), return `True`; otherwise, return `False`. The function should handle edge cases, including when `y` is negative and when both `x` and `y` are zero.
"""

def find_parity(x, y):
    if y < 0 and x not in [1, -1, 0]:  
        return True  
    elif y < 0 and x in [1, -1, 0]:  
        result = x ** abs(y)
    else: 
        result = x ** y
    
    return result % 2 == 0