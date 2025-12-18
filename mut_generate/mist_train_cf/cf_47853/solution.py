"""
QUESTION:
Compute the mean of an array of integers. The function should be optimized for large inputs (n <= 10^7) and return a result accurate to the nearest two decimal places. Implement a function `compute_mean(numbers)` that takes an array of integers as input and returns the calculated mean.
"""

def compute_mean(numbers):
    if not numbers:
        return 0.0
    return round(sum(numbers) / len(numbers), 2)