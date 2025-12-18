"""
QUESTION:
Create a function named `sort_by_abs_diff_to_mean` that sorts a list of integers by their absolute difference to the mean value of the list. The function should take a list of numbers as input and return a new list with the numbers sorted according to their absolute difference to the mean value. The function should not modify the original list.
"""

def sort_by_abs_diff_to_mean(numbers):
    mean = sum(numbers) / len(numbers)
    return sorted(numbers, key=lambda x: abs(x - mean))