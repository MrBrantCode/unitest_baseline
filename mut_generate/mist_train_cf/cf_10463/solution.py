"""
QUESTION:
Write a recursive function `foo(x)` that calculates the sum of the cubes of all integers from 1 to `x`, and add 2 to each cube, handling negative input. The function should return "Invalid input" for negative numbers and 0 for 0 input.
"""

def entrance(x):
    if x < 0:
        return "Invalid input"
    elif x == 0:
        return 0
    else:
        return entrance(x-1) + x**3 + 2