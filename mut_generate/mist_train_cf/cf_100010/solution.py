"""
QUESTION:
Create a function named `sort_by_abs_diff_to_mean` that takes a list of integers as input and returns a new list with the same integers sorted by their absolute difference to the mean value of the list.
"""

def sort_by_abs_diff_to_mean(numbers):
    mean = sum(numbers) / len(numbers)
    key_func = lambda x: abs(x - mean)
    return sorted(numbers, key=key_func)