"""
QUESTION:
Write a function `parity(num)` that takes an integer as input and returns a string indicating whether the integer is odd or even. The function should include error handling to ensure that the input is indeed an integer. The function should return "even" if the input is an even integer, "odd" if the input is an odd integer, and "Error: input must be an integer" if the input is not an integer.
"""

def parity(num):
    try:
        if num % 2 == 0:
            return "even"
        else:
            return "odd"
    except TypeError:
        return "Error: input must be an integer"