"""
QUESTION:
Write a function `calculate_difference(a, c)` that takes two integer inputs `a` and `c` and returns the difference between them without using the subtraction operator `-`.
"""

def calculate_difference(a, c):
    return a + (~c + 1)