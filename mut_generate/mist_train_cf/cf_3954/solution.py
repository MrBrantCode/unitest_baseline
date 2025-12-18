"""
QUESTION:
Implement a function `calculate_square_root(number)` that calculates the square root of a given positive number without using any built-in square root functions or libraries. The function should be able to handle numbers with up to 1000 digits.
"""

def calculate_square_root(number):
    # Initial guess for the square root
    guess = number / 2

    # Iterate until the difference between the guess and the actual square root is very small
    while abs(number - guess**2) > 0.000001:
        guess = (guess + number / guess) / 2

    return guess