"""
QUESTION:
Write a Python function named `int_to_bin` that takes an integer input and recursively converts it to its binary representation as a string. The function should raise a custom exception if the input is not an integer. The function should also handle negative numbers by prepending a negative sign to the result. Do not use built-in functions for binary conversion.
"""

class InvalidInputException(Exception):
    pass

def int_to_bin(n):
    if not isinstance(n, int):
        raise InvalidInputException("Input is not an integer")
        
    if n < 0:
        return "-" + int_to_bin(-n)
    elif n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return int_to_bin(n//2) + str(n%2)