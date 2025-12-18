"""
QUESTION:
Write a function `find_next_perfect_square(n)` that checks if a given integer `n` is a perfect square and returns the next perfect square if it is, otherwise return a message indicating that the number is not a perfect square. The function should have a time complexity of O(1) to efficiently handle large inputs.
"""

import math

def find_next_perfect_square(n):
    root = math.sqrt(n)
    if int(root + 0.5) ** 2 == n:
        next_square = (root + 1) ** 2
        return int(next_square)
    else:
        return "Number is not a perfect square"