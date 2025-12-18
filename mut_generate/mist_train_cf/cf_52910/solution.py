"""
QUESTION:
Design a function `generalized_factorial(n, m)` that calculates the generalized factorial of order `m` for a given number `n`. The generalized factorial of order `m` is the product of `n^m` from `n=1` to `n`. The function should handle edge cases, such as negative inputs and non-integer inputs, and implement memoization to optimize performance for large inputs of `n` and `m`. The function should return the result of the generalized factorial or an error message if the inputs are invalid.
"""

def generalized_factorial(n, m, memo={}):
    # Handling negative inputs
    if n < 0 or m < 0:
        return "Error: Inputs should be non-negative."
    
    # Handling non-integer inputs
    if not isinstance(n, int) or not isinstance(m, int):
        return "Error: Inputs should be integers."
    
    # Base Cases
    # Factorial or generalized factorial of 0 and 1 is 1
    if n == 0 or n == 1:
        return 1 

    # Check if computed before and stored in memo
    if (n, m) in memo:
        return memo[(n, m)]

    # Recursive case
    result = n**m * generalized_factorial(n-1, m, memo)

    # Store result to memo
    memo[(n, m)] = result

    return result