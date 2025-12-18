"""
QUESTION:
Write a function `identify_types` that takes three variables `a`, `b`, and `c` as input, where `a` is an integer, `b` is a character between 'A' and 'Z', and `c` is a floating-point number between 0 and 1. Identify the types of `a`, `b`, and `c` in C++. The function should return the types of `a`, `b`, and `c` in C++.
"""

def identify_types(a, b, c):
    """
    This function identifies the types of variables 'a', 'b', and 'c' in C++.
    
    Parameters:
    a (int): An integer variable
    b (str): A character variable between 'A' and 'Z'
    c (float): A floating-point number between 0 and 1
    
    Returns:
    dict: A dictionary containing the types of 'a', 'b', and 'c' in C++
    """
    return {
        'a': 'int',
        'b': 'char',
        'c': 'float'  # or 'double'
    }