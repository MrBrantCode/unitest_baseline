"""
QUESTION:
Implement the `sort_by_abs_diff_to_mean` function that takes a list of integers as input and returns a new list where the numbers are sorted by their absolute difference to the mean value of the series. The function should not modify the original list and should handle the case where the input list is empty.
"""

def sort_by_abs_diff_to_mean(numbers):
    if not numbers:
        return []
    mean = sum(numbers) / len(numbers)
    return sorted(numbers, key=lambda x: abs(x - mean))