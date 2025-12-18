"""
QUESTION:
Write a function `sqrt_babylonian(s)` that calculates the square root of a given number `s` without using the math library. The input `s` is a string representing a non-negative integer, and the function should return the integer square root of `s` rounded to the nearest integer using the Babylonian method (or Heron's method) for computing square roots.
"""

def sqrt_babylonian(s):
    x = int(s)
    guess = x / 2.0
    while True:
        better_guess = (guess + x / guess) / 2.0
        if abs(guess - better_guess) < 0.5:
            return round(better_guess)
        guess = better_guess