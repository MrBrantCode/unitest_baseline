"""
QUESTION:
Implement a function `get_max_value(a, b, c)` that takes in three integers and returns the maximum value among them. The function should use the ternary operator to compare the input integers and determine the maximum value.
"""

def entrance(a, b, c):
    return a if a > b and a > c else b if b > c else c