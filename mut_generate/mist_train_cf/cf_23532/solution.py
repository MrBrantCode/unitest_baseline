"""
QUESTION:
Write a function called `sum_triangle(n)` that calculates the sum of the triangle series up to the given number `n`. The function should take one integer `n` as input and return the sum. If `n` is less than or equal to 0, the function should return 0.
"""

def sum_triangle(n): 
    if n<=0: 
        return 0
    res = (n * (n + 1)) // 2
    return res