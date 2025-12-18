"""
QUESTION:
Write a function named "multiply_string_by_int" that takes a string and an integer as input and returns the result of their multiplication in Python. The function should utilize Python's string repetition feature using the `*` operator. The function must be able to handle cases where the integer is zero or negative.
"""

def multiply_string_by_int(s, n):
    """
    This function multiplies a given string by an integer.
    
    Args:
        s (str): The input string to be multiplied.
        n (int): The number of times the string should be repeated.
    
    Returns:
        str: The result of the string multiplication.
    """
    return s * n