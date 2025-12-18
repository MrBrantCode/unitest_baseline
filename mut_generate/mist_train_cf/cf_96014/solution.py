"""
QUESTION:
Design a recursive function `sum_of_squares(n)` that calculates the sum of the squares of the numbers between 1 and `n`. The function should handle negative input values of `n` by converting them to positive values, and return an error message for non-integer input values. The function must use memoization to store previously calculated results and minimize redundant computations.
"""

def sum_of_squares(n):
    # Check for non-integer input values
    if not isinstance(n, int):
        return "Error: Input value is not an integer."
    
    # Convert negative input values to positive
    if n < 0:
        n = -n
    
    # Global dictionary to store previously calculated results
    if not hasattr(sum_of_squares, "memo"):
        sum_of_squares.memo = {}
    
    # Check if result is already calculated and stored in memo
    if n in sum_of_squares.memo:
        return sum_of_squares.memo[n]
    
    # Base case: sum of squares of 0 or 1 is the number itself
    if n == 0 or n == 1:
        return n
    
    # Recursive case: calculate sum of squares
    result = n*n + sum_of_squares(n-1)
    
    # Store result in memo for future use
    sum_of_squares.memo[n] = result
    
    return result