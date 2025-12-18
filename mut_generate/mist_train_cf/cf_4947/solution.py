"""
QUESTION:
Create a function `factorial(n)` that calculates the factorial of a given number `n` without using any built-in factorial functions or operators. The function should handle both positive and negative values for `n` and return the result as a floating-point number.
"""

def factorial(n):
    # Check if n is negative
    if n < 0:
        # For negative n, use the formula: factorial(n) = (-1)^n * |n|!
        n = abs(n) # Calculate the factorial of |n|
        sign = -1 if n % 2 == 1 else 1 # Determine the sign (-1 or 1)
    else:
        sign = 1

    result = 1.0 # Initialize the result as a floating-point number

    # Calculate the factorial
    for i in range(1, n + 1):
        result *= i

    return sign * result