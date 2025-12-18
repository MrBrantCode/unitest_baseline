"""
QUESTION:
Write a recursive function `recursive_range(start, end)` that returns a list of integers in the range from `start` to `end` (exclusive), without using an iterative structure. Note that the function should not use tail recursion optimization due to Python's limitations. Be aware that this recursive approach may lead to a stack overflow for large ranges.
"""

def recursive_range(start, end):
    if start == end:
        return []
    else:
        return [start] + recursive_range(start + 1, end)