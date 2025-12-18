"""
QUESTION:
Create a function `sqrt_newton(n, precision)` to calculate the square root of a given number `n` using Newton's method with a specified `precision`. The function should take two parameters: `n` (the number to find the square root of) and `precision` (the level of accuracy for the result, defaulting to 0.00001).
"""

def sqrt_newton(n, precision=0.00001):
    guess = n
    while True:
        better_guess = (guess + n / guess) / 2
        if abs(guess - better_guess) < precision:
            return better_guess
        guess = better_guess