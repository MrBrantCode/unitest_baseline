"""
QUESTION:
Compose a function called `find_mean_median` to find the mean and median of a given list of positive integers. The function should handle cases where the list may contain duplicates or be unsorted. The function should return a tuple containing the mean and the median.
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