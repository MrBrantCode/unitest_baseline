"""
QUESTION:
Write a function named `power_func` that takes two arguments `base` and `exponent`, both of which are expected to be numbers, and calculates the power of the base raised to the nth power (exponent) without using the power (**) operator or any built-in Python function like pow(). The function should handle edge cases like negative or zero exponents, and non-numeric inputs.
"""

def power_func(base, exponent):
    try:
        # Check if exponent is 0, return 1 cause anything power 0 is 1
        if exponent == 0:
            return 1
        # Check if base is 0, return 0 cause 0 power anything is 0
        elif base == 0:
            return 0
        # Check if exponent is less than 0. If so, reciprocate base and negate exponent to get the answer
        elif exponent < 0:
            return 1 / power_func(base, -exponent)
        # Initialize results to 1(cause 1 power anything is 1)
        result = 1
        # loop through the range of exponent
        for i in range(exponent):
            result *= base
        # Return result
        return result
    except TypeError: 
        return "Error: Both inputs need to be numbers."