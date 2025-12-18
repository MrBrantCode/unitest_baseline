"""
QUESTION:
Design a function `hexadecimal_converter` that takes an input `n` and returns its hexadecimal notation. The function should handle the following error conditions: negative integers, floating-point numbers, and non-integer types. Use error handlers to pinpoint the exact error. The function should return an error message for invalid inputs.
"""

def hexadecimal_converter(n):
    try:
        assert isinstance(n, (int, float))  # check if input is a number
        assert n >= 0  # check if number is non-negative
        assert n == int(n)  # check if number is an integer
        return hex(int(n)) # convert to hexadecimal
    except AssertionError:
        return "Error: Invalid input. Please enter a non-negative integer."