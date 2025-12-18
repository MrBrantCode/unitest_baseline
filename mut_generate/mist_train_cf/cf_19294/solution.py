"""
QUESTION:
Write a function `square_if_even_positive` that takes an integer as input and returns the square of the number if it is positive, less than 10, and even. If the number is odd, return the negative of the number squared. The function should return None for non-positive numbers or numbers greater than or equal to 10.
"""

def square_if_even_positive(x):
    if x > 0 and x < 10:
        if x % 2 == 0:
            return x**2
        else:
            return -(x**2)
    else:
        return None