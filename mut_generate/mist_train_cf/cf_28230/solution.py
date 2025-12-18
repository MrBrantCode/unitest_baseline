"""
QUESTION:
Write a function `count_rectangles(A, B)` that calculates the number of rectangles that can be formed within an A x B grid such that the sides of the rectangles are aligned with the grid lines and the rectangles do not cover the entire grid. The function should take two integers A and B as input and return the number of rectangles that can be formed.
"""

def count_rectangles(A, B):
    return (A - 1) * (B - 1)