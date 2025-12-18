"""
QUESTION:
Create a function called `factorial(n)` that calculates the factorial of a given non-negative integer `n`. The function should only accept integers between 2 and 10 (inclusive), and return an error message if `n` is outside this range.
"""

def entance(n):
    if n < 2 or n > 10:
        return "Error: The input number should be between 2 and 10."
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result