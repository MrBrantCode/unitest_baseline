"""
QUESTION:
Create a function `fibonacci_word(n)` that calculates the nth value in the Fibonacci word sequence, defined as F(0) = '0', F(1) = '1', and F(n) = F(n-1) + F(n-2) for n > 1. The function should accept a single non-negative integer as input and return the corresponding Fibonacci word as a string. The function should handle edge cases, including input validation to ensure the input is a non-negative integer, and should be optimized to handle large inputs without exceeding Python's recursion depth limit.
"""

def fibonacci_word(n, computed={0: '0', 1: '1'}):
    if not isinstance(n, int):
        return 'Error: input must be an integer.'
    elif n < 0:
        return 'Error: input must be non-negative.'
    elif n not in computed:
        computed[n] = fibonacci_word(n-1, computed) + fibonacci_word(n-2, computed)
    return computed[n]