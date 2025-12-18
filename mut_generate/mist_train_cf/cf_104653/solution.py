"""
QUESTION:
Write a Python function named `create_array` that takes one argument `n`, creates an array of length `n` where each element at index `i` is `2 * i`, and returns this array.
"""

def create_array(n):
    return [2 * i for i in range(n)]