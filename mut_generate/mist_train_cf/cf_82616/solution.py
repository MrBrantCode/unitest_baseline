"""
QUESTION:
Create a recursive function named `factorial` that calculates the factorial of a given number `n`. The function should handle both integers and non-integer values (including negative numbers) by invoking the Gamma function. The function should not use the math library's built-in `factorial` function but can utilize other library functions. The input `n` can be a floating-point number or an integer where `n >= 0`.
"""

import math

def factorial(n):

    # Base case
    if n == 0:
        return 1
    
    # Recursive case for positive integers
    elif n > 0 and n == int(n):
        return n * factorial(n-1)

    # Using Gamma function to handle negative and non-integer numbers
    else:
        return math.gamma(n + 1)