"""
QUESTION:
Write a function `check_odd_even` that takes a number as input and returns `True` if the number is even, `False` if it's odd, and an error message if the input is not a number. The function should handle integers, floats, and fractions, support negative numbers and decimals, and use bitwise operators to check for odd/even without using conditional statements or loops.
"""

import fractions

def check_odd_even(number):
    if isinstance(number, (int, float, fractions.Fraction)):
        binary = bin(int(number))
        return binary[-1] == '0'
    else:
        return "Error: Input is not a number"