"""
QUESTION:
Write a function named `compute_average` that takes a list of numbers as input and returns the average of the list without using the built-in `sum()` function. The function should handle empty lists by returning 0. The list may contain negative numbers.
"""

def compute_average(lst):
    if len(lst) == 0:
        return 0
    total = 0
    for num in lst:
        total += num
    return total / len(lst)