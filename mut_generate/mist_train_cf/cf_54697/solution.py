"""
QUESTION:
Create a function named `factorial` that takes a non-negative integer `n` as input and returns its factorial using recursion with memoization. The function should handle large numbers, check if the input is a valid non-negative integer, and return an error message for invalid inputs. The function should also utilize memoization to optimize performance for repeated calls with the same number.
"""

def factorial(n, memo = {}):
    """Calculate the factorial of n with memoization"""
    
    if not (isinstance(n, int) and n >= 0):
        return "Error: Invalid Input"
    
    if n == 0 or n == 1:
        return 1

    if n in memo:
        return memo[n]
    
    result = n * factorial(n-1)
    memo[n] = result
    
    return result