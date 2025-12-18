"""
QUESTION:
Design a recursive function named `sum_of_squares` that calculates the sum of squares of the numbers between 1 and a given integer `n`. The function should convert negative `n` to positive, return an error message if `n` is not an integer, and utilize memoization to store previously calculated results. The function should also optimize for large `n` by minimizing recursive calls and memory usage.
"""

# Global dictionary to store previously calculated results
memo = {0: 0, 1: 1}

def sum_of_squares(n):
    # Check for non-integer input values
    if not isinstance(n, int):
        return "Error: Input value is not an integer."
    
    # Convert negative input values to positive
    if n < 0:
        n = -n
    
    # Check if result is already calculated and stored in memo
    if n in memo:
        return memo[n]
    
    # Recursive case: calculate sum of squares
    result = n*n + sum_of_squares(n-1)
    
    # Store result in memo for future use
    memo[n] = result
    
    return result