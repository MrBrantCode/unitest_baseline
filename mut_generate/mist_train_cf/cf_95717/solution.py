"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given integer `n`. The function should handle negative values for `n` and ensure the final result is within the range of a 64-bit signed integer. The function should return `None` if `n` is negative or if the result exceeds the limit of a 64-bit signed integer.
"""

def factorial(n):
    if n < 0:
        return None
    
    result = 1

    for i in range(2, abs(n) + 1):
        result *= i

        if result > 9223372036854775807:
            return None
    
    if n < 0:
        result = -result
    
    return result