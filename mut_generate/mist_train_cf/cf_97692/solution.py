"""
QUESTION:
Write a function called `sort_by_abs_diff_to_mean` that takes a list of integers as input and returns the sorted list where the numbers are ordered by their absolute difference to the mean value of the series. The function should calculate the mean value of the list and use this value to determine the order of the sorted list.
"""

def sort_by_abs_diff_to_mean(numbers):
    mean = sum(numbers) / len(numbers)
    key_func = lambda x: abs(x - mean)
    return sorted(numbers, key=key_func)