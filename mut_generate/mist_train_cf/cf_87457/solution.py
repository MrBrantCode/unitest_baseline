"""
QUESTION:
Write a function named `multiply` that takes two positive integers `x` and `n` as input and returns the result of multiplying `x` by itself `n` times using at least three recursion calls. The function should return an error message if either `x` or `n` is not a positive integer.
"""

def multiply(x, n):
    # check if x or n is not a positive integer
    if not isinstance(x, int) or not isinstance(n, int) or x <= 0 or n <= 0:
        return "Error: x and n must be positive integers"
    
    # base case: when n is 1, return x
    if n == 1:
        return x
    
    # recursive case: multiply x by itself n-1 times
    return x * multiply(x, n-1)