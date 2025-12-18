"""
QUESTION:
Write a function `sqrt(n)` that calculates the square root of a given number `n`. The function should handle different types of input (integers, floats, complex numbers) and return an exact result if `n` is a perfect square. For non-perfect squares, it should approximate the square root using an algorithm like Newton's method. The function should also handle exceptions, including `ValueError` and `TypeError`, and provide meaningful error messages to the user.
"""

import math
import cmath

def sqrt(n):
    try:
        if isinstance(n, complex):
            return cmath.sqrt(n)
        else:
            root = math.sqrt(n)
            if int(root + 0.5) ** 2 == n:
                return int(root)
            else:
                guess = n / 2.0
                while abs(guess * guess - n) > 1e-10:
                    guess = (guess + n / guess) / 2
                return guess
    except ValueError:
        print("Error: The value cannot be negative for real numbers. Enter a positive number or a complex number.")
    except TypeError:
        print("Error: The input is not a number. Please enter a numerical value.")