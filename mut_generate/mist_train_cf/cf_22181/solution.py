"""
QUESTION:
Create a function called `multiply` that takes two parameters, `a` and `b`, representing numbers to be multiplied. The function should return the product of `a` and `b` if both are positive integers. If either `a` or `b` is not a positive integer, the function should return an error message. If the inputs are floating-point numbers, the function should round the result to the nearest integer.
"""

def multiply(a, b):
    if a <= 0 or b <= 0:
        return "Both numbers must be positive and greater than zero"
    elif type(a) != int or type(b) != int:
        return round(a * b)
    else:
        return a * b