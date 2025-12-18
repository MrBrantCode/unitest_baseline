"""
QUESTION:
Write a function named `parity(num)` that takes an integer as input and returns a string indicating whether the integer is odd or even. The function should include error handling to ensure that the input is indeed an integer.
"""

def parity(num):
    try:
        if num % 2 == 0:
            return "even"
        else:
            return "odd"
    except TypeError:
        return "Error: input must be an integer"