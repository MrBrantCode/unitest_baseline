"""
QUESTION:
Implement a function `square_root(A)` to find the square root of a given positive floating-point number `A` without using any built-in functions or libraries. The number `A` will always be less than or equal to 10^6, and the result should be rounded to the nearest integer.
"""

def square_root(A):
    guess = A / 2
    while True:
        new_guess = (guess + A / guess) / 2
        diff = new_guess ** 2 - A
        if abs(diff) < 0.01:
            break
        guess = new_guess
    return round(guess)