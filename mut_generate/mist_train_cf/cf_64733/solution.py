"""
QUESTION:
Implement a function called `babylonian_sqrt(n)` that calculates the square root of a given number `n` without using the built-in square root function. The function should be accurate to a certain degree, which is defined by the variable `e` (a small positive number representing the acceptable margin of error).
"""

def babylonian_sqrt(n):
    x = n
    y = 1
    e = 0.000001  # This defines the accuracy level
    while (x - y > e):
        x = (x + y)/2
        y = n/x
    return x