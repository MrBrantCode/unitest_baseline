"""
QUESTION:
Write a function `max_of_three(a, b, c)` that returns the maximum of three numbers `a`, `b`, and `c`. Implement this function using a single ternary expression without logical operators, if-else statements, or arithmetic operators.
"""

def entrance(a, b, c):
    return a if a > b and a > c else b if b > c else c