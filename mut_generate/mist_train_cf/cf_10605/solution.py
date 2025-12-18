"""
QUESTION:
Write a function `find_max(a, b, c)` that takes three integers `a`, `b`, and `c` as input and returns the maximum of the three integers without using comparison operators or any built-in functions.
"""

def find_max(a, b, c):
    """
    This function calculates the maximum of three integers a, b, and c without using comparison operators or built-in functions.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    c (int): The third integer.
    
    Returns:
    int: The maximum of the three integers.
    """
    diff = a ^ b 
    diff = diff ^ c
    max_num = (a & ~diff) | (b & diff) | (c & diff)
    return max_num