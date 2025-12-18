"""
QUESTION:
Create a function named `total_sum` that takes three parameters: two integers `a` and `b`, and a list of integers `c`. The function should return the sum of `a`, `b`, and all elements in the list `c`. If any of the parameters are missing, the function should return "Error: Missing parameters". The function should also handle non-integer inputs, returning "Error: a and b must be integers" if `a` or `b` is not an integer, and "Error: c must be a list of integers" if `c` is not a list of integers.
"""

def entrance(a=None, b=None, c=None):
    if a is None or b is None or c is None:
        return "Error: Missing parameters"
        
    if not isinstance(a, int) or not isinstance(b, int):
        return "Error: a and b must be integers"

    if isinstance(c, list) and all(isinstance(i, int) for i in c):
        return a + b + sum(c)
    else:
        return "Error: c must be a list of integers"