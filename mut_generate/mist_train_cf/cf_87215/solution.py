"""
QUESTION:
Write a function named `sum_elements` that takes a list or array of non-negative integers as input and returns the sum of its elements. The input list or array must have a length between 3 and 10 (inclusive). The function must be implemented recursively.
"""

def entance(data):
    if len(data) == 0:
        return 0
    else:
        return data[0] + entance(data[1:])