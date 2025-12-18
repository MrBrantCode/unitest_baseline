"""
QUESTION:
Write a function `calculate_factorial(n)` that calculates the factorial of a given number `n`. The function should use a loop to calculate the factorial and handle edge cases where `n` is less than 0, 0, or 1. The function should return an error message for negative numbers and the correct factorial value for non-negative numbers. The loop should have a similar logic flow to a do-while loop, but since Python does not directly support do-while loops, a suitable alternative should be implemented.
"""

def calculate_factorial(n):
    if n < 0:
        return 'Invalid number'
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        i = 1
        while i <= n:
            fact *= i
            i += 1
        return fact