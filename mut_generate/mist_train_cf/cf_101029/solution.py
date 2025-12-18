"""
QUESTION:
Write a function `sort_by_abs_diff_to_mean()` that takes a list of integers as input and returns the sorted list based on the absolute difference of each number to the mean value of the list.
"""

def sort_by_abs_diff_to_mean(numbers):
    mean = sum(numbers) / len(numbers)
    return sorted(numbers, key=lambda x: abs(x - mean))