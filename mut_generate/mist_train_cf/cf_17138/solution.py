"""
QUESTION:
Write a function `sum_arrays(a, b)` that takes two arrays of integers `a` and `b` as input and returns an array containing the sum of their corresponding elements. The sum should only be calculated up to the length of the shorter array.
"""

def sum_arrays(a, b):
    result = []
    for i in range(min(len(a), len(b))):
        result.append(a[i] + b[i])
    return result