"""
QUESTION:
Create a function `square_nums(n, m)` that takes two integers `n` and `m` and returns an array containing the squares of the numbers from `n` to `m` (inclusive). The function should ensure that both `n` and `m` are positive integers and `m` is greater than or equal to `n`. If the input is invalid, return an error message.
"""

def entrance(n, m):
    if n <= 0 or m <= 0 or type(n) != int or type(m) != int:
        return "n and m must be positive integers."
    
    if m < n:
        return "m must be greater than or equal to n."
    
    result = [i ** 2 for i in range(n, m+1)]
    return result