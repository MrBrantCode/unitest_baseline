"""
QUESTION:
Write a function `find_mean_median` that takes a list of positive integers as input, calculates the mean and median of the list, and returns both values. The function should handle cases where the list may contain duplicates or be unsorted, and it should be optimized to reduce time complexity and avoid unnecessary calculations.
"""

def find_mean_median(numbers):
    # Calculate mean
    mean = sum(numbers) / len(numbers)

    # Calculate median
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]

    return mean, median