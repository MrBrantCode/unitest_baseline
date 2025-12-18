"""
QUESTION:
Write a function `find_max` that takes three integers as input and returns the maximum number among them. The function should only use conditional statements (if, else if, else) a maximum of two times and should not use any built-in comparison operators (such as >) or functions (such as max()).
"""

def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c