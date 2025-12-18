"""
QUESTION:
Write a function `fun` that takes an integer `n` as input and returns a value based on the following conditions: if `n` is less than 2, return `n`; otherwise, return the sum of `fun(n-1)` and `fun(n-2)`. The function should not take any additional parameters and should only use recursive calls to calculate the result.
"""

def fun(n):
    if n < 2:
        return n
    else:
        return fun(n-1) + fun(n-2)