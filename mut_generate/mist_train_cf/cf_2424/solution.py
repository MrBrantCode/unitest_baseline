"""
QUESTION:
Write a function called `multiply` that takes two positive integers `x` and `n` as input. The function should return the result of multiplying `x` by itself `n` times using at least three recursion calls. If either `x` or `n` is negative, the function should return an error message.
"""

def multiply(x, n):
    # check if x or n is negative
    if x < 0 or n < 0:
        return "Error: x and n must be positive integers"
    
    # base case: when n is 0, return 1
    if n == 0:
        return 1
    
    # recursive case: multiply x by itself n-1 times
    return x * multiply(x, n-1)