"""
QUESTION:
Write a recursive function `calculate_factorial(n)` to calculate the factorial of a positive integer `n`. The function should return the factorial of `n` if `n` is a positive integer, otherwise it should return a meaningful error message. The input `n` should be a positive integer.
"""

def calculate_factorial(n):
    # Error handling for non-integer input
    if not isinstance(n, int):
        return "Error: Non-integer Input"
    
    # Error handling for negative input
    elif n < 0:
        return "Error: Negative Input"
    
    # Factorial of 0 is 1
    elif n == 0:
        return 1
    
    else:
        return n * calculate_factorial(n - 1)