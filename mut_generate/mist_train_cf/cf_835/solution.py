"""
QUESTION:
Write a single ternary expression function `max_of_three(a, b, c)` that returns the maximum of three input numbers without using logical operators within the ternary expression itself, if-else statements, or arithmetic operators.
"""

def entrance(a, b, c):
    return a if a > b and a > c else b if b > c else c