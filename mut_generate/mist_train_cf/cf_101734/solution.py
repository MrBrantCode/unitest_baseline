"""
QUESTION:
Create a function `sort_by_abs_diff_to_mean(numbers)` that takes a list of integers as input, calculates the mean value of the list, and returns a new list where the numbers are sorted by their absolute difference to the mean value. The function should use a custom key function to achieve this sorting.
"""

def sort_by_abs_diff_to_mean(numbers):
    mean = sum(numbers) / len(numbers)
    key_func = lambda x: abs(x - mean)
    return sorted(numbers, key=key_func)