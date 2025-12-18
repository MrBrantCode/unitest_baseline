"""
QUESTION:
Implement a function named `compute_average` that takes an array of floating-point numbers as input and returns the average of the numbers. The function should not use the built-in `sum()` function or any external libraries. The input array may contain up to 1 million elements.
"""

def compute_average(arr):
    total = 0
    count = 0
    for num in arr:
        total += num
        count += 1
    average = total / count
    return average