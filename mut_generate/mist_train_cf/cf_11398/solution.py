"""
QUESTION:
Write a function named `compute_average` that calculates the average of a list of numbers without using the built-in `sum()` function. The function should handle a list that contains negative numbers and return 0 for an empty list.
"""

def compute_average(lst):
    if len(lst) == 0:
        return 0
    total = 0
    for num in lst:
        total += num
    return total / len(lst)