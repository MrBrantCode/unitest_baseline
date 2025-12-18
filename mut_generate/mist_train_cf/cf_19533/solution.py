"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given integer `n`. The function should handle negative values of `n` and ensure the result is within the range of a 64-bit signed integer. If `n` is negative or the result exceeds the 64-bit signed integer limit, the function should return `None`.
"""

def factorial(n):
    # Check for negative values
    if n < 0:
        return None
    
    # Initialize result
    result = 1

    # Calculate factorial using efficient algorithm
    for i in range(2, abs(n) + 1):
        result *= i

        # Check if the result exceeds 64-bit signed integer limit
        if result > 9223372036854775807:
            return None
    
    # If n is negative, invert the result
    if n < 0:
        result = -result
    
    return result