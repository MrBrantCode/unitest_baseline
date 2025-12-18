"""
QUESTION:
Write a function `example_function(a, b)` that calculates the sum of all numbers from `a` to `b` (inclusive) in constant time, with a time complexity of O(1). The function should take two integers `a` and `b` as input, where `a` is less than or equal to `b`, and return the sum of all integers in the range.
"""

def entance(a, b):
    return (b - a + 1) * (a + b) // 2