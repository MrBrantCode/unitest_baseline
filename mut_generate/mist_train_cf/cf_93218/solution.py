"""
QUESTION:
Implement a function `compute_average(arr)` that calculates the average of an array of floating-point numbers without using the built-in `sum()` function or any external libraries. The input array may contain up to 1 million elements.
"""

def compute_average(arr):
    total = 0
    count = 0
    for num in arr:
        total += num
        count += 1
    average = total / count
    return average