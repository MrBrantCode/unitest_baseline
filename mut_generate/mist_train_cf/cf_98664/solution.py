"""
QUESTION:
Write a function called `parity` that takes an integer as input and returns a string indicating whether the integer is "even" or "odd". The function should include error handling to ensure that the input is indeed an integer. If the input is not an integer, the function should return "Error: input must be an integer".
"""

def parity(num):
    try:
        if num % 2 == 0:
            return "even"
        else:
            return "odd"
    except TypeError:
        return "Error: input must be an integer"