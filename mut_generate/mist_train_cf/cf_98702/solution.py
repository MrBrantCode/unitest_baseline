"""
QUESTION:
Implement a function named `sort_by_abs_diff_to_mean` that sorts a list of integers by their absolute difference to the mean value of the series. The function should take a list of integers as input and return a sorted list of integers.
"""

def sort_by_abs_diff_to_mean(numbers):
    mean = sum(numbers) / len(numbers)
    key_func = lambda x: abs(x - mean)
    return sorted(numbers, key=key_func)