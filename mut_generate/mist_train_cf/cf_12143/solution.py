"""
QUESTION:
Write a function `find_maximum` that takes three numbers as input and returns the maximum of the three numbers. The function can only use a maximum of two conditional statements (if, else if, else).
"""

def find_maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c