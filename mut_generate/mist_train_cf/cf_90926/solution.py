"""
QUESTION:
Write a function `square_nums(n, m)` that takes two integers `n` and `m` and returns an array of squares of the numbers from `n` to `m` (inclusive). The function should ensure that `n` and `m` are positive integers and `m` is greater than or equal to `n`. If these conditions are not met, the function should return an error message.
"""

def entrance(n, m):
    # Check if n and m are positive integers
    if n <= 0 or m <= 0 or type(n) != int or type(m) != int:
        return "n and m must be positive integers."
    
    # Check if m is greater than or equal to n
    if m < n:
        return "m must be greater than or equal to n."
    
    # Calculate the squares of the numbers from n to m
    result = [i ** 2 for i in range(n, m+1)]
    return result