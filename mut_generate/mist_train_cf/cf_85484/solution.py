"""
QUESTION:
Create a function named `sum_two` that takes three parameters: two numbers `a` and `b`, and a multiplier `m`. The function should return the sum of `a` and `b` multiplied by `m`. If `m` is zero, return "Error".
"""

def sum_two(a, b, m):
    if m == 0:
        return "Error"
    else:
        return (a + b) * m