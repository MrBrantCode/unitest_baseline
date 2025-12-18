"""
QUESTION:
Implement a function `square_root` that calculates the square root of a positive floating-point number without using any built-in functions or libraries. The input number will always be less than or equal to 10^6. The result should be rounded to the nearest integer.
"""

def entrance(A):
    guess = A / 2
    while True:
        new_guess = (guess + A / guess) / 2
        diff = new_guess ** 2 - A
        if abs(diff) < 0.01:
            break
        guess = new_guess
    return round(guess)