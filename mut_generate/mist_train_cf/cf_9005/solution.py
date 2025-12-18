"""
QUESTION:
Implement a function `calculate_big_o(complexity)` that takes a time complexity as input, where `n` is the input size, and returns a string representation of its Big O notation. The function should handle the following complexities: constant time `O(1)`, linear time `O(n)`, quadratic time `O(n^2)`, exponential time `O(2^n)`, and factorial time `O(n!)`. If the input complexity does not match any of these, return "Cannot determine Big O notation for the given complexity."
"""

import math

def calculate_big_o(complexity):
    if complexity == 1:
        return "O(1)"
    elif complexity == "n":
        return "O(n)"
    elif complexity == "n^2":
        return "O(n^2)"
    elif complexity == "2^n":
        return "O(2^n)"
    elif complexity == "n!":
        return "O(n!)"
    else:
        return "Cannot determine Big O notation for the given complexity."