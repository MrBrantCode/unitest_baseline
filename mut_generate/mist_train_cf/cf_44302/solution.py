"""
QUESTION:
Implement a function `sqrt(n)` that calculates the square root of a given number `n` without using built-in square root functions or libraries. The function should handle negative input values by raising an exception, and it should be able to compare and output results with a precision of up to 8 decimal places. The input `n` will be in the range `[-10^4, 10^4]`.
"""

def sqrt(n):
    if n < 0:
        raise Exception("Invalid input! Cannot compute square root of a negative number.")
    elif n == 0 or n == 1:
        return n

    guess = n / 2.0
    for _ in range(100000):  
        better_guess = (guess + n / guess) / 2.0
        if abs(guess - better_guess) < 0.00000001:  
            return round(better_guess, 8)
        guess = better_guess
    return guess