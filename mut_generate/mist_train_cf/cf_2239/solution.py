"""
QUESTION:
Write a function `calculate_sum(a, b)` that takes two arrays of numbers as input and returns an array with the sum of their corresponding elements. If the lengths of `a` and `b` are not equal, the sum should only be calculated up to the length of the shorter array. The function should be able to handle arrays with negative numbers, decimal numbers, and empty arrays.
"""

def calculate_sum(a, b):
    if len(a) == 0 and len(b) == 0:
        return []
    
    length = min(len(a), len(b))
    
    result = []
    
    for i in range(length):
        sum = a[i] + b[i]
        result.append(sum)
    
    return result