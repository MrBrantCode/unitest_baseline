"""
QUESTION:
Create a function named `largest` that takes two numbers as input and returns the larger of the two numbers. The function should not modify the input numbers and should work for any pair of comparable numbers.
"""

def largest(a, b):
    """Returns the larger number from two numbers provided."""
    if a > b:
        return a
    else:
        return b