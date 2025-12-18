"""
QUESTION:
Create a function called `max_of_two_numbers` that takes two parameters, both integers or floats, and returns the maximum value. If both parameters are equal, the function should raise a custom `EqualNumbersException`. The function should be able to handle negative integers and floating-point numbers as input, but it is assumed that the inputs will be positive integers, and there is no need to validate this.
"""

class EqualNumbersException(Exception):
    pass

def max_of_two_numbers(a, b):
    if a == b:
        raise EqualNumbersException("The numbers are equal")
    return max(a, b)