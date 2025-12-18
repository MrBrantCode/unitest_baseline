"""
QUESTION:
Write a function `check_odd_even` that determines whether a given number is odd or even using bitwise operators without conditional statements or loops. The function should accept integers, floats, and fractions as input and return a boolean value indicating whether the number is even. If the input is not a number, the function should return an error message.
"""

import fractions

def check_odd_even(number):
    if isinstance(number, (int, float, fractions.Fraction)):
        binary = bin(int(number))
        return binary[-1] == '0'
    else:
        return "Error: Input is not a number"